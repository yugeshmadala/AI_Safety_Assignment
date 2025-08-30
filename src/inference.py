import joblib

def load_model(model_path="models/abuse_detector.pkl"):
    model = joblib.load(model_path)
    print("Model Loaded")
    return model

def predict_text(model, text):
    pred = model.predict([text])[0]
    probability = model.predict_proba([text])[0]
    return pred, probability 

if __name__ == "__main__":
    model = load_model()
    print("Abuse Detection Demo")
    print("Type 'exit' to quit\n")

    while True:
        text = input("Enter text: ")
        if text.lower() == "exit":
            break 
        label, probability = predict_text(model, text)
        print(f"Predicted label: {label}")
        print(f"Class probabilities: {probability}\n")

        