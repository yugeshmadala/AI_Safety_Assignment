AI SAFETY POC:

Project Overview:
This project is a Proof of Concept (POC) for AI-based safety tools in conversational platforms. The main goal is to help identify harmful or inappropriate content, detect potential crisis situations, and monitor conversation escalation, all in real-time.

The POC demonstrates four key features:
1.Abuse Detection – Identifies hate speech, offensive language, or neutral messages.
2.Content Filtering – Blocks content that may be inappropriate for children or teens.
3.Escalation Detection – Tracks conversations and alerts if messages become increasingly aggressive.
4.Crisis Detection – Detects signs of severe emotional distress or self-harm in messages.

Features
1. Abuse Detection

   Classifies messages into Hate Speech, Offensive, or Neither.
   Shows the probability for each category.
   Helps moderators quickly identify and handle harmful content.

2. Content Filter

   Blocks messages containing content not suitable for specific age groups: children, teens, or adults.
   Categories include drugs, sexual content, violence, and general safe content.

3. Escalation Detector

   Monitors the last few messages in a conversation.
   Alerts when the conversation is becoming aggressive or escalating.
   Keeps a small rolling history of messages for context.

4. Crisis Detection

   Identifies messages that indicate severe emotional distress or suicidal thoughts.
   Provides confidence scores to help prioritize urgent situations.

HOW TO RUN:

1.Clone the repository :https://github.com/yugeshmadala/AI_Safety_Assignment.git
2.Set up a virtual environment.
3.Install dependencies using the requirements.txt 
4.Run the app using streamlit: streamlit run src/app.py 
5.Open browser at :http://localhost:8501/

HOW TO USE:
   Select a module from the sidebar (Abuse Detection, Content Filter, Escalation Detector, Crisis Detector).
   Enter your message in the text box.
   Press the button to analyze the message.
   Results will appear below, including labels, scores, or alerts.

PROJECT STRUCTURE:

            AI_SAFTEY_ASSIGNMENT/
            |
            |--models/
            |
            |--src/
            |     |--app.py
            |     |--content_filter.py
            |     |--crisis_detector.py
            |     |--escalation.py
            |     |--inference.py
            |     |--train.py
            |
            |--venv/
            |
            |--.gitignore
            |
            |--LICENSE
            |
            |--README.md
            |
            |--requirements.txt
            |
            |--template.py

Notes:

   This is a Proof of Concept, so the app is not yet optimized for production.
   The models are lightweight for demo purposes, focusing on real-time functionality.
   No personal or sensitive data is used; all datasets are public and anonymized.
   Ethical considerations like fairness and bias have been considered in model design.

Future Improvements:

   Add multi-language support for abuse detection.
   Improve escalation detection with more complex conversation context.
   Deploy models in a cloud environment for real-time multi-user support.
   Add notifications for crisis detection to alert human moderators immediately.



            


        



