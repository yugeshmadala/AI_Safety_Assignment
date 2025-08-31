import pandas as pd
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def train_abuse_model(return_model=False):
    print("Loading dataset...")
    dataset = load_dataset("hate_speech_offensive")
    print("Dataset loaded")

    df = pd.DataFrame(dataset["train"])
    print("DataFrame created with shape:", df.shape)

    x = df["tweet"]
    y = df["class"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    clf = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("lr", LogisticRegression(class_weight="balanced",max_iter=1000))
    ])

    clf.fit(x_train,y_train)

    y_pred=clf.predict(x_test)

    print(classification_report(y_test, y_pred))

    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/abuse_detector.pkl")

    if return_model:
        return clf

if __name__ == "__main__":
    train_abuse_model() 

