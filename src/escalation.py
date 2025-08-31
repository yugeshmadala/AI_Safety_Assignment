from collections import deque 
import joblib 

class EscalationDetector:
    def __init__(self, model_path="models/abuse_detector.pkl", window_size=3):
        self.model = joblib.load(model_path)
        self.window_size = window_size
        self.recent_scores = deque(maxlen=window_size)

    def update(self,text):
        probability = self.model.predict_proba([text])[0]
        offensive_score = probability[0] + probability[1]  
        self.recent_scores.append(offensive_score)

        if len(self.recent_scores) == self.window_size:
            avg_score = sum(self.recent_scores) / self.window_size
            if avg_score > 0.4: 
                return True, avg_score
        return False, offensive_score
    
    



