# Personal Portfolio with Integrated AI Chatbot

A modern, responsive personal portfolio website featuring an **interactive AI chatbot**.  
The chatbot is powered by a backend API and embedded seamlessly on the portfolio, allowing visitors to learn more about you, your projects, and your skills in a conversational way.

---

## 📌 Features

### 🌐 Portfolio
- **Clean, modern, and responsive design**
- **About Me** section with personal introduction
- **Projects showcase** with descriptions, screenshots, and links
- **Contact section** with email, social media, and form submission

### 🤖 AI Chatbot
- **Fixed position** at the bottom-left corner of the site
- **Interactive chat window** with styled bubbles
- **Smooth open/close animations**
- **Backend integration** to process and return AI-generated answers
- **Supports multi-turn conversation** (remembers context within the chat session)

---

## 🛠️ Tech Stack

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript (Vanilla)**
- **Responsive design techniques** for mobile & desktop

### Backend
- **FastAPI** (or Flask) for API handling
- **Python** for AI integration
- **OpenAI / GPT-OSS** models for chatbot responses

---

## 📂 Folder Structure
project/
│
├── index.html # Main portfolio page
├── style.css # Styling for portfolio & chatbot
├── script.js # Chatbot and UI interactions
│
├── backend/
│ ├── main.py # FastAPI/Flask backend
│ ├── requirements.txt
│ └── ...
│
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/portfolio-chatbot.git
cd portfolio-chatbot
2️⃣ Backend Setup
Navigate to the backend folder:

bash
Copy
Edit
cd backend
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your API keys (OpenAI or GPT-OSS) to .env:

env
Copy
Edit
OPENAI_API_KEY=your_api_key_here
Run the backend server:

bash
Copy
Edit
uvicorn main:app --reload
3️⃣ Frontend Setup
Simply open index.html in a browser, or serve it locally using:

bash
Copy
Edit
python -m http.server 8000
🎯 How It Works
User clicks chatbot icon → The chat window opens.

User types a message → Message is sent to the backend via API.

Backend processes the request → AI model generates a reply.

Reply is sent back to frontend → Displayed as a chatbot message.

📸 Screenshots
Portfolio Main Page

AI Chatbot in Action

📌 To-Do / Future Improvements
 Add dark/light mode toggle

 Improve chatbot styling with avatars

 Add markdown rendering in chatbot replies

 Store chat history on backend for analytics

 Deploy backend & frontend to Fly.io or Vercel

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.





---

