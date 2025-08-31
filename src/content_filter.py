from transformers import pipeline

def load_filter():
    print("Loading content filter model...")
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

def filter_demo():
    classifier = load_filter()

    age_groups = {
        "child": ["safe", "violent", "sexual", "drugs"],
        "teen": ["safe", "violent", "sexual", "drugs"],
        "adult": ["safe", "violent", "sexual", "drugs"]
    }

    print("\nContent Filter Demo")
    print("Type 'exit' to quit\n")

    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break

        age = input("Enter user age group (child/teen/adult): ").strip().lower()

        if age not in age_groups:
            print("Invalid age group. Use child/teen/adult.\n")
            continue

        labels = age_groups[age]
        result = classifier(message, candidate_labels=labels)
        top_label = result["labels"][0]
        score = result["scores"][0]

        if age == "child" and top_label in ["violent", "sexual", "drugs"]:
            print(f"Blocked for child: {top_label} content (score={score:.2f})\n")
        elif age == "teen" and top_label in ["sexual", "drugs"]:
            print(f"Restricted for teen: {top_label} content (score={score:.2f})\n")
        else:
            print(f"llowed ({top_label}, score={score:.2f})\n")

if __name__ == "__main__":
    filter_demo()

    
