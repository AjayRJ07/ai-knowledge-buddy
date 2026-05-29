"""
AI Knowledge Buddy — Data
==========================
Quiz questions and lesson content for the Data Scientist role.
Edit this file to customise or extend the curriculum.
"""

# ── Quiz ──────────────────────────────────────────────────────────────────────
# Each question: question, options (list of 4), answer (0-indexed), topic, explanation

QUIZ = [
    {
        "question": "What is the main difference between supervised and unsupervised learning?",
        "options": [
            "Supervised uses GPUs; unsupervised uses CPUs",
            "Supervised trains on labeled data; unsupervised finds patterns without labels",
            "Supervised is faster; unsupervised is more accurate",
            "Supervised uses Python; unsupervised uses R",
        ],
        "answer": 1,
        "topic": "ML Fundamentals",
        "explanation": (
            "Supervised learning trains on labeled examples (e.g. spam/not-spam emails). "
            "Unsupervised learning discovers hidden structure in unlabeled data — "
            "like clustering customers into segments."
        ),
    },
    {
        "question": "Which Python library is the go-to choice for classical machine learning (random forests, SVMs, etc.)?",
        "options": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras"],
        "answer": 2,
        "topic": "Python for DS",
        "explanation": (
            "Scikit-learn (sklearn) is the standard library for classical ML in Python. "
            "TensorFlow and PyTorch are used for deep learning. "
            "Keras is a high-level API built on top of TensorFlow."
        ),
    },
    {
        "question": "What does 'overfitting' mean in machine learning?",
        "options": [
            "The model is too small to learn anything",
            "The model memorises training data but fails on new data",
            "The model trains too slowly",
            "The model uses too much GPU memory",
        ],
        "answer": 1,
        "topic": "Model Evaluation",
        "explanation": (
            "Overfitting happens when a model learns the training data too well — "
            "including its noise — and therefore performs poorly on unseen data. "
            "Solutions include regularisation, dropout, and getting more data."
        ),
    },
    {
        "question": "What does LLM stand for?",
        "options": [
            "Large Learning Module",
            "Layered Language Machine",
            "Large Language Model",
            "Linear Logic Method",
        ],
        "answer": 2,
        "topic": "Generative AI",
        "explanation": (
            "LLM = Large Language Model. These are neural networks trained on massive text corpora "
            "to understand and generate language. GPT-4, Claude, and Gemini are all LLMs."
        ),
    },
    {
        "question": "In the context of neural networks, what is a 'transformer'?",
        "options": [
            "A device that converts AC to DC power",
            "An architecture using attention mechanisms — the foundation of modern LLMs",
            "A function that scales input features",
            "A technique for reducing model size",
        ],
        "answer": 1,
        "topic": "Deep Learning",
        "explanation": (
            "The Transformer architecture (introduced in 'Attention Is All You Need', 2017) "
            "uses self-attention to process entire sequences in parallel. "
            "It powers virtually every modern LLM including GPT, Claude, and BERT."
        ),
    },
    {
        "question": "What is 'feature engineering'?",
        "options": [
            "Building GPU hardware for ML",
            "The process of creating or transforming input variables to improve model performance",
            "Selecting which ML framework to use",
            "Writing unit tests for ML pipelines",
        ],
        "answer": 1,
        "topic": "Data Science",
        "explanation": (
            "Feature engineering is the craft of creating, selecting, or transforming raw data "
            "into informative inputs for a model. For example: extracting 'day of week' from a timestamp, "
            "or log-transforming a skewed variable. Good features often matter more than algorithm choice."
        ),
    },
    {
        "question": "What is 'RAG' in the context of LLM applications?",
        "options": [
            "Random Activation Graph",
            "Retrieval-Augmented Generation",
            "Recursive Algorithm for Generation",
            "Regularised Attention Gradient",
        ],
        "answer": 1,
        "topic": "LLM Applications",
        "explanation": (
            "RAG = Retrieval-Augmented Generation. Instead of relying only on a model's training knowledge, "
            "RAG retrieves relevant documents at query time and feeds them into the prompt. "
            "This gives LLMs access to fresh or private data without retraining."
        ),
    },
    {
        "question": "Which metric is most appropriate when your dataset has a severe class imbalance?",
        "options": ["Accuracy", "F1-Score", "Mean Squared Error", "R-squared"],
        "answer": 1,
        "topic": "Model Evaluation",
        "explanation": (
            "With class imbalance (e.g., 99% negatives), accuracy is misleading — a model that always "
            "predicts 'negative' scores 99%. F1-Score balances precision and recall, making it far more "
            "informative. AUC-ROC is another strong choice."
        ),
    },
    {
        "question": "What is the purpose of 'cross-validation' in machine learning?",
        "options": [
            "To speed up model training",
            "To reliably estimate model performance on unseen data",
            "To convert data between different formats",
            "To visualise decision boundaries",
        ],
        "answer": 1,
        "topic": "Model Evaluation",
        "explanation": (
            "Cross-validation (e.g., k-fold) splits data into multiple train/validation sets "
            "and averages results across them. This gives a more reliable estimate of how the model "
            "will perform on truly unseen data than a single train/test split."
        ),
    },
    {
        "question": "In AI ethics, what is 'algorithmic bias'?",
        "options": [
            "When an algorithm runs slower on certain hardware",
            "When a model produces systematically unfair outcomes due to biased training data or design",
            "When two algorithms disagree on a prediction",
            "When a model is biased toward faster computation over accuracy",
        ],
        "answer": 1,
        "topic": "AI Ethics",
        "explanation": (
            "Algorithmic bias occurs when a model inherits or amplifies human prejudices from its training data "
            "or problem framing — leading to unfair outcomes for certain groups. "
            "It's a critical issue in hiring tools, credit scoring, and healthcare AI."
        ),
    },
]

# ── Lessons ───────────────────────────────────────────────────────────────────
# Each lesson: title, subtitle, intro, body, points (list), code (str)

LESSONS = [
    {
        "title": "AI & ML Landscape",
        "subtitle": "How AI, ML, and Deep Learning relate",
        "intro": (
            "Artificial Intelligence is the broad field of making machines intelligent. "
            "Machine Learning is a subset where systems learn from data. "
            "Deep Learning is a subset of ML using multi-layered neural networks."
        ),
        "body": (
            "Think of it as concentric circles: AI ⊃ ML ⊃ Deep Learning. "
            "Classical ML algorithms (decision trees, SVMs) work well with structured tabular data and limited samples. "
            "Deep learning shines with unstructured data (images, text, audio) and massive datasets. "
            "As a data scientist, you'll use both depending on the problem."
        ),
        "points": [
            "AI = any technique making machines mimic human intelligence",
            "ML = systems that learn patterns from data automatically",
            "Deep Learning = ML using neural networks with many layers",
            "Choose algorithms based on data type, size, and interpretability needs",
            "Scikit-learn for classical ML; PyTorch/TensorFlow for deep learning",
        ],
        "code": """\
# Classical ML with Scikit-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

df = pd.read_csv("data.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))
""",
    },
    {
        "title": "Data Wrangling with Pandas",
        "subtitle": "Cleaning & transforming data like a pro",
        "intro": (
            "80% of a data scientist's time is spent on data cleaning and preparation. "
            "Pandas is the essential Python library for structured data manipulation — "
            "think of it as a programmable spreadsheet with superpowers."
        ),
        "body": (
            "Key operations: loading data, handling missing values, merging datasets, "
            "groupby aggregations, and feature creation. "
            "Always explore your data first: check dtypes, nulls, distributions, and duplicates "
            "before touching any model. The quality of your data directly determines your model's ceiling."
        ),
        "points": [
            "df.info() and df.describe() are your first stop",
            "Handle nulls: drop, fill with mean/median/mode, or model-impute",
            "Use .groupby() for aggregations across categories",
            "merge() and join() combine datasets — understand inner/left/outer joins",
            "Apply lambda functions for quick column transformations",
        ],
        "code": """\
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# Quick overview
print(df.shape, df.dtypes, df.isnull().sum())

# Fill missing numerics with median
df["age"].fillna(df["age"].median(), inplace=True)

# Create new feature
df["age_group"] = pd.cut(df["age"], bins=[0,18,35,60,100],
                          labels=["teen","young","mid","senior"])

# Aggregate
summary = df.groupby("age_group")["salary"].agg(["mean","median","count"])
print(summary)
""",
    },
    {
        "title": "Model Evaluation & Metrics",
        "subtitle": "Choosing and interpreting the right metrics",
        "intro": (
            "Picking the wrong metric is one of the most common mistakes in ML. "
            "A model with 99% accuracy on a fraud detection dataset might be completely useless "
            "if fraud represents only 1% of transactions."
        ),
        "body": (
            "Classification metrics: accuracy, precision, recall, F1, AUC-ROC. "
            "Regression metrics: MAE, MSE, RMSE, R². "
            "Use cross-validation to get reliable estimates. "
            "Always align your metric with the business problem — in medical diagnosis, "
            "false negatives (missing disease) are far costlier than false positives."
        ),
        "points": [
            "Accuracy = correct / total — misleading with class imbalance",
            "Precision = TP / (TP + FP) — how many predicted positives are real",
            "Recall = TP / (TP + FN) — how many actual positives were caught",
            "F1 = harmonic mean of precision & recall — good for imbalanced data",
            "AUC-ROC measures model's ability to discriminate classes across thresholds",
        ],
        "code": """\
from sklearn.metrics import (classification_report, roc_auc_score,
                              confusion_matrix, ConfusionMatrixDisplay)
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")

# Full report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# AUC-ROC
y_prob = model.predict_proba(X_test)[:, 1]
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.3f}")

# Confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()
""",
    },
    {
        "title": "Neural Networks & Deep Learning",
        "subtitle": "From perceptrons to transformers",
        "intro": (
            "Neural networks are loosely inspired by the brain — layers of connected nodes "
            "that learn to transform inputs into outputs. "
            "Deep learning = many layers, enabling models to learn hierarchical representations."
        ),
        "body": (
            "Architecture: input layer → hidden layers → output layer. "
            "Each neuron applies a weighted sum then an activation function (ReLU, sigmoid, softmax). "
            "Training uses backpropagation + gradient descent to minimise a loss function. "
            "PyTorch is the dominant research framework; TensorFlow/Keras for production pipelines."
        ),
        "points": [
            "Activation functions introduce non-linearity (ReLU is the default choice)",
            "Loss functions: CrossEntropy for classification, MSE for regression",
            "Optimisers: Adam is the most widely used starting point",
            "Regularisation: dropout, batch normalisation, weight decay",
            "CNNs for images, RNNs/Transformers for sequences",
        ],
        "code": """\
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)

model = SimpleNet(input_dim=20, hidden_dim=64, output_dim=2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
print(model)
""",
    },
    {
        "title": "LLMs & Prompt Engineering",
        "subtitle": "Working with large language models effectively",
        "intro": (
            "LLMs like Claude and GPT-4 are trained on internet-scale text and can perform "
            "a remarkable range of tasks — writing, coding, summarising, reasoning — "
            "just by following instructions in plain language."
        ),
        "body": (
            "As a data scientist, you'll use LLMs via APIs for text analysis, data extraction, "
            "report generation, and building AI-powered pipelines. "
            "Prompt engineering — crafting effective instructions — is a core skill. "
            "Key techniques: few-shot examples, chain-of-thought, role assignment, and output format constraints."
        ),
        "points": [
            "System prompt sets the LLM's role and constraints",
            "Few-shot prompting: show 2-3 input→output examples in the prompt",
            "Chain-of-thought: ask the model to 'think step by step'",
            "Structured output: ask for JSON so you can parse programmatically",
            "Temperature controls randomness: 0 = deterministic, 1 = creative",
        ],
        "code": """\
import anthropic
import json

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

# Structured extraction from unstructured text
text = "Revenue grew 23% YoY to $4.2B. Net margin improved to 18%."

prompt = f\"\"\"Extract financial metrics from this text as JSON.
Return ONLY valid JSON, no explanation.
Format: {{"metric": "value", ...}}

Text: {text}\"\"\"

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    messages=[{"role": "user", "content": prompt}]
)

data = json.loads(response.content[0].text)
print(data)
# {'Revenue growth': '23% YoY', 'Revenue': '$4.2B', 'Net margin': '18%'}
""",
    },
    {
        "title": "RAG — Retrieval-Augmented Generation",
        "subtitle": "Giving LLMs access to your own data",
        "intro": (
            "LLMs are limited by their training cutoff and cannot access private data. "
            "RAG solves this: retrieve relevant documents at query time and inject them "
            "into the prompt as context — no retraining required."
        ),
        "body": (
            "RAG pipeline: 1) Chunk documents into passages. "
            "2) Embed each chunk into a vector space. "
            "3) Store vectors in a vector database (FAISS, Chroma, Pinecone). "
            "4) At query time, embed the question and retrieve the most similar chunks. "
            "5) Pass retrieved chunks + question to the LLM. "
            "This gives you a 'private ChatGPT' over your own documents."
        ),
        "points": [
            "Embeddings turn text into dense vectors capturing semantic meaning",
            "Cosine similarity measures how related two embeddings are",
            "Chunk size matters: too small = no context; too large = noise",
            "FAISS is fast and free for local vector search",
            "HuggingFace sentence-transformers provides great embedding models",
        ],
        "code": """\
# Minimal RAG with FAISS + Anthropic
# pip install faiss-cpu sentence-transformers anthropic

import faiss, numpy as np
from sentence_transformers import SentenceTransformer
import anthropic

docs = [
    "Claude is an AI assistant made by Anthropic.",
    "RAG stands for Retrieval-Augmented Generation.",
    "Python is the dominant language for data science.",
]

embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(docs, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

query = "What is RAG?"
q_emb = embedder.encode([query], convert_to_numpy=True)
_, I = index.search(q_emb, k=2)
context = "\n".join(docs[i] for i in I[0])

client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    messages=[{"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}]
)
print(resp.content[0].text)
""",
    },
    {
        "title": "MLOps & Model Deployment",
        "subtitle": "Taking models from notebook to production",
        "intro": (
            "Building a model is only half the job. MLOps covers the practices and tools "
            "for reliably deploying, monitoring, and maintaining ML models in production — "
            "where real users depend on them."
        ),
        "body": (
            "Key components: experiment tracking (MLflow, W&B), model versioning (DVC), "
            "serving (FastAPI, BentoML, SageMaker), and monitoring (data drift, performance decay). "
            "A model in production can degrade silently as the real world changes. "
            "Monitoring is not optional."
        ),
        "points": [
            "MLflow tracks experiments, parameters, metrics, and artefacts",
            "DVC versions large datasets and models alongside your git history",
            "FastAPI is the fastest way to serve a model as a REST API",
            "Monitor data drift: production inputs may diverge from training data",
            "CI/CD pipelines automate testing and redeployment of retrained models",
        ],
        "code": """\
# Experiment tracking with MLflow
import mlflow
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score

mlflow.set_experiment("churn-prediction")

with mlflow.start_run():
    params = {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 4}
    mlflow.log_params(params)

    model = GradientBoostingClassifier(**params)
    model.fit(X_train, y_train)

    f1 = f1_score(y_test, model.predict(X_test))
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(model, "model")

    print(f"F1: {f1:.4f} — logged to MLflow")
""",
    },
    {
        "title": "AI Ethics & Responsible ML",
        "subtitle": "Building fair, transparent, and safe systems",
        "intro": (
            "Every model you build will affect real people. "
            "Responsible ML means thinking proactively about fairness, transparency, "
            "privacy, and unintended consequences — not as an afterthought, but as part of the design."
        ),
        "body": (
            "Key concerns: algorithmic bias (models inheriting societal prejudices from data), "
            "explainability (can you justify a prediction?), privacy (does training on personal data "
            "expose individuals?), and misuse (could this model be used to harm?). "
            "Tools like SHAP and LIME make black-box models more interpretable."
        ),
        "points": [
            "Audit training data for representation imbalances before modelling",
            "Use fairness metrics: demographic parity, equalised odds, calibration",
            "SHAP values explain feature contributions for any model",
            "Differential privacy adds noise to protect individuals in training data",
            "Document your model with a Model Card (Google's standard)",
        ],
        "code": """\
# Model explainability with SHAP
# pip install shap

import shap
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier().fit(X_train, y_train)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Summary plot — feature importance
shap.summary_plot(shap_values[1], X_test, feature_names=X_test.columns)

# Explain a single prediction
shap.force_plot(
    explainer.expected_value[1],
    shap_values[1][0],
    X_test.iloc[0],
    feature_names=X_test.columns
)
""",
    },
]
