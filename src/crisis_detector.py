from transformers import pipeline

_crisis_classifier = pipeline("text-classification", model="sentinet/suicidality")

def crisis_demo_cli(text):
    result = _crisis_classifier(text)[0]
    raw_label = result['label']
    score = result['score']

    label = "Suicidal" if raw_label.startswith("LABEL_1") else "Non-Suicidal"
    return label, score




    

