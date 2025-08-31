from transformers import pipeline

def load_filter():
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

def content_filter_cli(text,age='adult'):
    classifier = load_filter()

    labels = ["safe", "violent", "sexual", "drugs"]

    result = classifier(text, candidate_labels=labels)
    top_label = result["labels"][0]
    score = result["scores"][0]

    return top_label, score


