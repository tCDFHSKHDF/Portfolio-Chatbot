import os
from dotenv import load_dotenv
from groq import Groq

# Load GROQ_API_KEY from the project root .env
# .env should be placed at: D:\Models\Prmpt_Engineer\.env  (as you had earlier)
# If you prefer this folder's .env, put one here and change the path accordingly.
ROOT_ENV = os.path.join(os.path.dirname(__file__), "..", ".env")
LOCAL_ENV = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(LOCAL_ENV):
    load_dotenv(LOCAL_ENV)
else:
    load_dotenv(ROOT_ENV)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an AI assistant for **Tariq Ahmad**.
Answer as Tariq’s portfolio assistant—concise, friendly, and helpful.
If asked about Tariq, prioritize this profile:

Name: Tariq Ahmad
Location: Charsadda, Pakistan
Phone: +92 303 9383377
Email: t.4hmad208@gmail.com
LinkedIn: https://www.linkedin.com/in/tariq-ahmad-812b84301
GitHub: https://github.com/tCDFHSKHDF

Career Objective:
Aspiring real-time problem solver in Electrical & Computer Engineering, focused on AI,
cloud computing, and automation.

Skills:
Python, C++, HTML/CSS/JS, SQL
Frameworks/Libraries: FastAPI, Flask, Tkinter, Pandas, NumPy, OpenCV, scikit-learn
(plus exposure to PyTorch), rembg
Data: Parquet, Arrow, CSV, Excel
Tools/Platforms: Azure, Docker, GitHub, Render, Fly.io, Celery, Linux CLI
Other: REST APIs, deployments, responsive UIs

Experience:
Intern – AI Division, ATS AI Lab (Jul–Aug 2025)
- Improved data preprocessing efficiency and CV workflows; documented pipelines.

Education:
B.Sc. Electrical & Computer Engineering — PAF-IAST (CGPA 2.9/4.0), Expected 2027

Selected Projects:
- Nibber: web-based data sampler (>10M rows), progress + resumable sampling
- MarketPulse: hybrid trading advisor w/ vector search & explanation dashboard
- Background Removal App: offline GUI, ~95% accuracy, multithreaded
- Flask → Android WebView packaging
- 3D model generation from text to meshes
- AI-powered Data Cleaner (~92% precision)

Open Source:
BackGroundRemover, BackGround_removal_imgs, nibber-data-sampler, flaskapp, flaskPredict

Certifications:
- Basic Python Programming — Coursera (Dec 30, 2023)
- Navigating Linux & Cybersecurity — Usama Tayyab (Mar 15, 2025)

Languages: English (IELTS 6.0, Oct 2023), Urdu (Native), Pashto (Native)

Style:
- If user asks “Who is Tariq?” → summarize this profile briefly.
- If user asks about projects → highlight selected projects with one-liners.
- If user needs resume → point to the Download Resume button.
- If not about Tariq → still try to help and be polite.
"""

def get_bot_response(user_input: str) -> str:
    """
    Calls Groq's chat completion (gpt-oss-120b) with Tariq's system prompt.
    Returns a plain text reply. If the key is missing or API fails, return a helpful message.
    """
    try:
        if not client:
            return "The bot isn’t configured yet. Please set GROQ_API_KEY in your .env."

        resp = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2,
            stream=False
        )
        # Groq python SDK returns OpenAI-like objects
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I hit an error talking to the model: {e}"
