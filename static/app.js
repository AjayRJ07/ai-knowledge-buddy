// ── Tab switching ──────────────────────────────────────────────────────────

document.querySelectorAll(".nav-item").forEach(btn => {
  btn.addEventListener("click", () => {
    const tab = btn.dataset.tab;
    document.querySelectorAll(".nav-item").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById("tab-" + tab).classList.add("active");
    if (tab === "quiz"    && !quizLoaded)    loadQuiz();
    if (tab === "lessons" && !lessonsLoaded) loadFirstLesson();
  });
});

// ── Chat ───────────────────────────────────────────────────────────────────

let chatHistory = [];

function sendChip(btn) {
  document.getElementById("chatInput").value = btn.textContent;
  document.getElementById("chips").style.display = "none";
  sendChat();
}

async function sendChat() {
  const input = document.getElementById("chatInput");
  const btn   = document.getElementById("sendBtn");
  const text  = input.value.trim();
  if (!text) return;

  input.value = "";
  input.style.height = "auto";
  btn.disabled = true;

  appendMsg("user", text);
  chatHistory.push({ role: "user", content: text });

  const typingEl = appendTyping();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ history: chatHistory, message: text })
    });

    if (!res.ok) {
      typingEl.remove();
      appendMsg("buddy", "⚠️ Server error " + res.status + ". Make sure app.py is running.");
      btn.disabled = false;
      return;
    }

    typingEl.remove();
    const buddyEl  = appendMsg("buddy", "");
    const bodyEl   = buddyEl.querySelector(".message-body");
    let   fullText = "";
    let   buffer   = "";

    const reader  = res.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop(); // keep incomplete last line for next chunk

      for (const line of lines) {
        if (!line.startsWith("data: ")) continue;
        const payload = line.slice(6).trim();
        if (payload === "[DONE]") break;
        try {
          const parsed = JSON.parse(payload);
          if (parsed.error) {
            bodyEl.textContent = "⚠️ " + parsed.error;
            break;
          }
          if (parsed.text) {
            fullText += parsed.text;
            bodyEl.textContent = fullText;
            scrollChat();
          }
        } catch (_) {}
      }
    }

    if (fullText) chatHistory.push({ role: "model", content: fullText });

  } catch (err) {
    typingEl.remove();
    appendMsg("buddy", "⚠️ Could not connect. Is app.py running? (" + err.message + ")");
  }

  btn.disabled = false;
  input.focus();
}

function appendMsg(role, text) {
  const box = document.getElementById("chatMessages");
  const div = document.createElement("div");
  div.className = "message " + role;
  const avatar = role === "buddy" ? "B" : "U";
  div.innerHTML = `
    <div class="message-avatar">${avatar}</div>
    <div class="message-body">${text}</div>`;
  box.appendChild(div);
  scrollChat();
  return div;
}

function appendTyping() {
  const box = document.getElementById("chatMessages");
  const div = document.createElement("div");
  div.className = "message buddy";
  div.id = "typing-indicator";
  div.innerHTML = `
    <div class="message-avatar">B</div>
    <div class="message-body"><div class="typing-dots"><span></span><span></span><span></span></div></div>`;
  box.appendChild(div);
  scrollChat();
  return div;
}

function scrollChat() {
  const box = document.getElementById("chatMessages");
  box.scrollTop = box.scrollHeight;
}

// ── Quiz ───────────────────────────────────────────────────────────────────

let quizData    = [];
let quizIndex   = 0;
let quizScore   = 0;
let quizLoaded  = false;

async function loadQuiz() {
  quizLoaded = true;
  const res  = await fetch("/api/quiz");
  quizData   = await res.json();
  showQuizStart();
}

function showQuizStart() {
  document.getElementById("quizContainer").innerHTML = `
    <div class="quiz-start">
      <h2>Ready to test yourself?</h2>
      <p>
        ${quizData.length} questions covering ML fundamentals, model evaluation,
        deep learning, LLMs, RAG, and AI ethics.<br>
        Take your time — explanations are shown after each answer.
      </p>
      <button class="start-btn" onclick="startQuiz()">Start Quiz →</button>
    </div>`;
}

function startQuiz() {
  quizIndex = 0; quizScore = 0;
  showQuestion();
}

function showQuestion() {
  const q   = quizData[quizIndex];
  const pct = ((quizIndex + 1) / quizData.length * 100).toFixed(0);

  document.getElementById("quizContainer").innerHTML = `
    <div class="quiz-card">
      <div class="quiz-meta">
        <span class="quiz-topic">${q.topic}</span>
        <span class="quiz-score-live">Score: ${quizScore}</span>
        <span class="quiz-counter">${quizIndex + 1} / ${quizData.length}</span>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="quiz-question">${q.question}</div>
      <div class="quiz-options">
        ${q.options.map((opt, i) => `
          <button class="quiz-opt" onclick="answerQuiz(${i})" data-idx="${i}">
            <span class="opt-key">${String.fromCharCode(65+i)}</span>
            ${opt}
          </button>`).join("")}
      </div>
      <div class="quiz-feedback" id="quizFeedback"></div>
      <button class="next-btn" id="nextBtn" style="display:none" onclick="nextQuestion()">
        ${quizIndex + 1 < quizData.length ? "Next question →" : "See results →"}
      </button>
    </div>`;
}

function answerQuiz(chosen) {
  const q    = quizData[quizIndex];
  const btns = document.querySelectorAll(".quiz-opt");
  btns.forEach(b => b.disabled = true);
  btns[q.answer].classList.add("correct");

  const fb = document.getElementById("quizFeedback");
  if (chosen === q.answer) {
    quizScore++;
    fb.textContent = "✓ Correct!  " + q.explanation;
    fb.className   = "quiz-feedback correct show";
  } else {
    btns[chosen].classList.add("wrong");
    fb.textContent = `✗ The answer was: ${q.options[q.answer]}.  ${q.explanation}`;
    fb.className   = "quiz-feedback wrong show";
  }

  document.getElementById("nextBtn").style.display = "inline-block";
}

function nextQuestion() {
  quizIndex++;
  if (quizIndex >= quizData.length) showScore();
  else showQuestion();
}

function showScore() {
  const pct  = Math.round(quizScore / quizData.length * 100);
  const msgs = [
    "Keep going — review the lessons to strengthen your foundations.",
    "Good effort! A few more sessions and you'll nail it.",
    "Solid work! You've got strong AI/DS fundamentals.",
    "Excellent! You're a data science knowledge powerhouse 🏆"
  ];
  const msgIdx = pct <= 40 ? 0 : pct <= 60 ? 1 : pct <= 85 ? 2 : 3;

  document.getElementById("quizContainer").innerHTML = `
    <div class="score-card">
      <div class="score-big">${quizScore}/${quizData.length}</div>
      <div class="score-label">${pct}% correct</div>
      <div class="score-msg">${msgs[msgIdx]}</div>
      <button class="retry-btn" onclick="startQuiz()">Try again</button>
    </div>`;
}

// ── Lessons ────────────────────────────────────────────────────────────────

let lessonsLoaded   = false;
let activeLessonIdx = 0;

function loadFirstLesson() {
  lessonsLoaded = true;
  showLesson(0, document.querySelector(".lesson-item"));
}

async function showLesson(idx, btn) {
  activeLessonIdx = idx;
  document.querySelectorAll(".lesson-item").forEach(b => b.classList.remove("active"));
  if (btn) btn.classList.add("active");

  const detail = document.getElementById("lessonDetail");
  detail.innerHTML = `<div class="lesson-placeholder">Loading...</div>`;

  const res    = await fetch(`/api/lessons/${idx}`);
  const lesson = await res.json();

  const points = lesson.points.map(p => `
    <div class="key-point"><div class="kp-dot"></div><span>${p}</span></div>`).join("");

  const nextBtn = idx + 1 < document.querySelectorAll(".lesson-item").length
    ? `<button class="lesson-next-btn" onclick="showLesson(${idx+1}, document.querySelectorAll('.lesson-item')[${idx+1}])">Next lesson →</button>`
    : "";

  detail.innerHTML = `
    <div class="lesson-content">
      <div class="lesson-title-row">
        <h2>${lesson.title}</h2>
        <div class="lesson-subtitle">${lesson.subtitle}</div>
      </div>
      <p class="lesson-text">${lesson.intro}</p>
      <p class="lesson-text">${lesson.body}</p>
      <div class="key-points">
        <div class="key-points-label">Key points</div>
        ${points}
      </div>
      <div class="code-block">
        <div class="code-header">
          <span class="code-lang">python</span>
          <button class="copy-btn" onclick="copyCode(this)">copy</button>
        </div>
        <pre id="codeBlock">${escapeHtml(lesson.code)}</pre>
      </div>
      <div class="lesson-actions">
        <button class="lesson-ask-btn" onclick="askAboutLesson('${lesson.title.replace(/'/g,"\\'")}')">
          Ask Buddy about this →
        </button>
        ${nextBtn}
      </div>
    </div>`;
}

function askAboutLesson(title) {
  document.querySelector('[data-tab="chat"]').click();
  document.getElementById("chatInput").value = `Tell me more about "${title}" with a data science example`;
  sendChat();
}

function copyCode(btn) {
  const code = document.getElementById("codeBlock").textContent;
  navigator.clipboard.writeText(code).then(() => {
    btn.textContent = "copied!";
    setTimeout(() => btn.textContent = "copy", 2000);
  });
}

function escapeHtml(str) {
  return str.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}
