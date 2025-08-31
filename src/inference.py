import joblib
import os 

Model_path = os.path.join(os.path.dirname(__file__), "..", "models", "abuse_detector.pkl")
Model_path = os.path.abspath(Model_path)

Label_Mapping = {
    0: "Hate Speech",
    1: "Offensive",
    2: "Neither"
}

def abuse_inference_cli(load_model=False):
    if load_model:
        model = joblib.load(Model_path)
        return AbuseModelWrapper(model), model
    
class AbuseModelWrapper:
    def __init__(self, model):
        self.model = model

    def predict(self, text):
        pred = self.model.predict([text])[0]
        probability = self.model.predict_proba([text])[0]
        label_text = Label_Mapping.get(pred, f"Unknown ({pred})")
        return label_text, probability
    
