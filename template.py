import os

folders = ["models", "src"]

files = [
    "requirements.txt",
    "README.md",
    "src/train.py",
    "src/inference.py",
    "src/escalation.py",
    "src/crisis_detector.py",
    "src/content_filter.py",
    "src/app.py"
]

def create_structure():
    for i in folders:
        os.makedirs(i, exist_ok=True)
    
    for file_path in files:
        with open(file_path, "w") as f:
            pass 
    

if __name__ == "__main__":
    create_structure()

