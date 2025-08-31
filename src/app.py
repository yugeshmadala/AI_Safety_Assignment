from inference import abuse_inference_cli
from escalation import EscalationDetector
from crisis_detector import crisis_demo_cli
from content_filter import content_filter_cli
import streamlit as st 

abuse_model, _ = abuse_inference_cli(load_model=True)
escalation_detector = EscalationDetector(window_size=3)

st.set_page_config(page_title="AI Safety POC", layout="centered")

st.title("AI Safety POC")
st.write("Test Abuse Detection, Content Filtering, Crisis Detection, and Escalation Monitoring")

option = st.sidebar.radio(
    "Choose a module:",
    ("Abuse Detection", "Content Filter", "Escalation Detector","Crisis Detector")
)

if option == "Abuse Detection":
    st.header("Abuse Detection")
    user_input = st.text_area("Enter your message:",key="abuse_input")
    if st.button("Analyze"):
        if user_input.strip():
            label, prob = abuse_model.predict(user_input)
            st.write(f"Predicted Label: {label}")
            st.write(f"Class Probabilities: {prob}")
        else:
            st.warning("Please enter some text.") 

elif option == "Content Filter":
    st.header("Content Filter")
    user_input = st.text_area("Enter your message:",key="content_input")
    age = st.selectbox("Select Age Group", ["child", "teen", "adult"])
    if st.button("Filter"):
        if user_input.strip():
            label, score = content_filter_cli(user_input, age)
            st.write(f"Filter Result: {label} (score={score:.2f})")
        else:
            st.warning("Please enter some text.")

elif option == "Escalation Detector":
    st.header("Escalation Detector")
    
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_area("Enter message (stream of conversation):",key="escalation_input")

    if st.button("Check Escalation"):
        if user_input.strip():
            st.session_state.conversation.append(user_input)

            last_messages = st.session_state.conversation[-3:]
            escalated, score = False, 0.0
            for msg in last_messages:
                escalated, score = escalation_detector.update(msg)

            if escalated:
                st.error(f"onversation escalating! Avg offensive score: {score:.2f}")
            else:
                st.write(f"Offensive score: {score:.2f}")
            
            st.write("**Recent conversation:**")
            for i, msg in enumerate(last_messages, 1):
                st.write(f"{i}: {msg}")
        else:
            st.warning("Please enter some text.")

elif option == "Crisis Detector":
    st.header("Crisis Detector")
    user_input = st.text_area("Enter your message:",key="crisis_input")
    if st.button("Analyze Crisis"):
        if user_input.strip():
            label, score = crisis_demo_cli(user_input)
            st.write(f"Result: {label}")
            st.write(f"Confidence: {score:.2f}")
        else:
            st.warning("Please enter some text.")

