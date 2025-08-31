from transformers import pipeline

def crisis_demo():
    print("Loading crisis detection model...")
    classifier = pipeline("text-classification", model="sentinet/suicidality")

    print("\nCrisis Detection Demo")
    print("Type 'exit' to quit\n")

    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break

        result = classifier(message)[0]
        label = result['label']
        score = result['score']

        interpretation = "Crisis Detected" if label.startswith("LABEL_1") else "Non-Suicidal"
        print(f"{interpretation}: {label}, Confidence: {score:.2f}\n")

if __name__ == "__main__":
    crisis_demo()

    

