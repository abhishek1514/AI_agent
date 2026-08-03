# 🔬 Agentic AI · Multi-Agent Deep Research System

A production-ready, autonomous Multi-Agent Deep Research platform built with **Python**, **LangChain**, and **Streamlit**. The system coordinates independent LLM specialized entities working sequentially to scan the live web, scrape in-depth context, compile markdown reports, and critique factual consistency—completely bypassing expensive proprietary search API locks.

🚀 **[Live Demo Link]( https://aiagent-eflu2vnshwu9pb2p5dzru8.streamlit.app/#results)**

---

## 🛠️ System Architecture & Workflow

Instead of a standard single-prompt system, this framework breaks the research workload down into a distributed pipeline of specialized agents to eliminate AI hallucinations:

1. **Search Agent**: Receives the query and scans the live web using a pure Python extraction mechanism.
2. **Reader Agent**: Targets identified reference URLs and scrapes raw textual content (up to 3,000 characters) for deep parsing.
3. **Writer Chain**: Synthesizes the extracted multi-source context into a structured, production-grade Markdown report.
4. **Critic Chain**: Executes an independent audit on the compiled paper, outputting an objective quality score out of 10 along with key strengths and vulnerabilities.

---

## ⚡ Tech Stack & Ecosystem

- **Backend Logic & AI Framework**: Python, LangChain, LangGraph, Pydantic
- **Core LLM Processing Engine**: Groq Cloud Engine (`llama-3.3-70b-versatile`)
- **Web UI & Streaming Architecture**: Streamlit, Custom CSS Injection, Session State Tracking
- **Scraping Infrastructure**: BeautifulSoup4, Requests, Python-Dotenv

---

## 💻 Local Installation & Setup

If you want to run this application locally on your system, follow these execution commands:

### 1. Clone the Repository
```bash
git clone https://github.com/abhishek1514/AI_agent.git
cd AI_agent
```

### 2. Configure Environment Variables
Create a clean `.env` file in the root directory:
```text
GROQ_API_KEY="your_gsk_private_api_key_here"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Interface
```bash
streamlit run app.py
```

---

## 💡 Production Deployment & Optimizations
- **Cost Efficiency**: Migrated successfully from standard commercial OpenAI pipelines onto high-throughput open-weight models managed securely via the Groq ecosystem.
- **Dependency Freedom**: Eliminated reliance on paid specialized AI search layers (like Tavily) by developing a customized network fallback scraper utilizing raw Python formatting.
