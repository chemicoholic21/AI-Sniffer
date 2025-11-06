import streamlit as st
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
MODEL_NAME = "gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# Streamlit app setup
st.set_page_config(page_title="Interview Transcript AI Detection", page_icon="🤖", layout="wide")

st.title("🧠 AI vs Human Transcript Analyzer")
st.markdown("""
Upload or paste an **interview transcript (in JSON or text format)** below.
The app will analyze whether the responses seem **AI-generated, human, or AI-assisted** using the Gemini 2.5 Flash model.
""")

# Input area
uploaded_file = st.file_uploader("Upload transcript file (.json or .txt)", type=["json", "txt"])
text_input = st.text_area("Or paste transcript JSON/text here", height=250)

transcript_content = None

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".json"):
            transcript_content = json.load(uploaded_file)
            transcript_text = json.dumps(transcript_content, indent=2)
        else:
            transcript_text = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        transcript_text = None
elif text_input.strip():
    transcript_text = text_input.strip()
else:
    transcript_text = None

# Button to analyze
if st.button("🔍 Analyze Transcript", type="primary"):
    if not transcript_text:
        st.warning("Please upload or paste a transcript first.")
    else:
        with st.spinner("Analyzing transcript using Gemini..."):
            prompt = f"""
You are an expert in multimodal cheating detection for online interviews, inspired by research on anti-cheating
systems that use face detection, object tracking, and behavioral analysis.

Analyze the following interview transcript as if it were the "audio" component of a remote interview.
Your goal is to detect irregularities or external assistance analogous to cheating events in audio/video systems.

Evaluate and provide:

1. **AI-Assistance Probability (0-100%)** — likelihood that the candidate’s responses were generated or guided by AI tools.
2. **Behavioral Integrity Classification** — label as one of:
   - "Human (Clean)"
   - "AI-Assisted (Suspicious)"
   - "AI-Generated (Cheating)"
3. **Evidence and reasoning** — consider linguistic, coherence, latency, spontaneity, tone consistency, and context alignment
   (comparable to visual cues like multiple faces, device presence, or candidate absence).
4. **Behavioral Metrics (optional)** — mention any indicators resembling:
   - *Another Person / Device*: multiple stylistic voices, abrupt changes in phrasing, unnatural vocabulary shifts.
   - *Absence*: loss of conversational continuity, blank or filler responses.
   - *Face/Voice Tracking Confidence*: coherence between question and answer.
5. **Final One-Line Verdict** — concise summary of your detection.

Transcript:
{transcript_text}
"""


            try:
                response = model.generate_content(prompt)
                result = response.text.strip()

                st.success("✅ Analysis complete!")
                st.markdown("### 🧩 Gemini Analysis Result")
                st.write(result)

            except Exception as e:
                st.error(f"Error analyzing transcript: {e}")
