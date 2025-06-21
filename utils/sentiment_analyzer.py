# utils/sentiment_analyzer.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

# Load FinBERT model and tokenizer from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

labels = {0: "Negative", 1: "Neutral", 2: "Positive"}

def analyze_sentiment(text):
    """
    Predict sentiment of a given financial news text using FinBERT.
    Returns: label and score (confidence)
    """
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = softmax(outputs.logits, dim=1)
            predicted_class = torch.argmax(probs).item()
            confidence = round(float(probs[0][predicted_class]), 4)
            return labels[predicted_class], confidence
    except Exception as e:
        print(f"[Error] Sentiment analysis failed: {e}")
        return "Unknown", 0.0
