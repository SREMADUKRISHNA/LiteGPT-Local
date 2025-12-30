# LiteGPT-Local 🤖

LiteGPT-Local is a lightweight, CPU-optimized, ChatGPT-inspired local chatbot designed to run entirely on a laptop without a GPU.  
It answers small and simple questions correctly, handles greetings and names properly, and avoids hallucinated conversations.

This project is intended for academic demos, GitHub portfolios, and learning real-world AI system limitations.

---

## ✨ Features

- Fully local chatbot (no cloud APIs, no paid services)
- Runs on CPU-only systems (8GB RAM supported)
- ChatGPT-like responses for small questions
- Correct handling of greetings and user names
- No fake multi-turn conversations
- No SYSTEM / USER / ASSISTANT role leakage
- FastAPI backend + simple frontend UI
- TinyLlama model via Ollama

---

## 🧠 Architecture

User (Browser)
→ Frontend (HTML/CSS/JS)
→ FastAPI Backend
→ Ollama (TinyLlama)
→ Response returned to UI

The chatbot always responds only to the latest user input.

---

## 🛠 Tech Stack

Backend:
- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- Ollama

Model:
- TinyLlama (CPU-friendly)

Frontend:
- HTML
- CSS
- JavaScript

Platform:
- Ubuntu Linux
- CPU-only (no GPU)

---

## 📂 Project Structure

LiteGPT-Local/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md

---

## 🚀 FULL SETUP, RUN & GITHUB COMMANDS (COPY & RUN IN ORDER)

### Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

### Pull TinyLlama model
ollama pull tinyllama

### (Optional) Test model
ollama run tinyllama

### Go to backend
cd LiteGPT-Local/backend

### Create virtual environment
python3 -m venv venv

### Activate virtual environment
source venv/bin/activate

### Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

### Run backend server
uvicorn main:app --reload

### Open a new terminal and run frontend
cd LiteGPT-Local/frontend
xdg-open index.html

---

## ✅ Recommended Test Questions

hello  
my name is sremadukrishna  
what is phishing in cybersecurity  
what is linux  
linux command to create a directory  

---

## ⚠️ Limitations

- No real-time data (weather, news)
- No deep reasoning or complex math
- No long-term memory across sessions
- Optimized for correctness over creativity

These limitations are expected for local CPU-based LLMs.

---

## 🎓 Learning Outcomes

- Local LLM deployment using Ollama
- CPU-based inference optimization
- Prompt alignment and hallucination control
- FastAPI backend development
- Frontend-backend integration
- Realistic AI system design under constraints

---

## 🏁 Conclusion

LiteGPT-Local demonstrates how a ChatGPT-inspired chatbot can be built and stabilized on limited hardware while maintaining correct behavior for simple queries.

---

## 👤 Author

Sremadukrishna  
Cybersecurity & AI Enthusiast

---

## 🔼 GitHub Push Commands

git init
git add .
git commit -m "Initial commit: LiteGPT-Local chatbot"
git branch -M main
git remote add origin https://github.com/USERNAME/LiteGPT-Local.git
git push -u origin main
