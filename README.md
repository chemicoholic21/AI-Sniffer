# 🕵️‍♂️ AI Sound Integrity Detector

A real-time browser-based audio integrity detection system for online hiring.

This system continuously listens to the candidate’s microphone during a remote interview and classifies whether the audio environment is **clean** or **suspicious**.

---

## 🎯 Goal

Detect and label audio conditions such as:

| Condition        | Example                                    |
|------------------|---------------------------------------------|
| Normal speech    | one human voice speaking                    |
| Typing sounds    | candidate actively searching / typing answers |
| Paper rustling   | reading notes / printed cheat sheets        |
| Whispering       | someone feeding answers nearby              |
| Multiple voices  | more than one speaker present               |
| Long silence     | mic muted to compute / query AI             |

Final output: **Real-time integrity status**

---

## ✅ Functional Flow

1. Capture mic audio in browser
2. Split audio into 1 second frames
3. Convert frames → mel spectrograms
4. Feed features to ML classifier
5. Display live integrity label in the UI

---

## 🧰 Tech Stack

| Component | Used For |
|----------|----------|
| **Streamlit** | web UI + browser microphone capture |
| **Librosa** | audio preprocessing + spectrograms |
| **TensorFlow / Keras** | sound classification model |
| **WebRTC** | real-time audio streaming |

---

## 🚀 How to Run

### Clone repo
```bash
git clone https://github.com/chemicoholic21/AI-Sniffer.git
cd AI-Sniffer
