# MarsX - AI Chatbot

MarsX is an AI-powered chatbot built with [Streamlit](https://streamlit.io/) and [Groq's LLM API](https://groq.com/). It features a modern chat interface and streams responses using Groq's ultra-fast inference engine.

---

## Features

- Built with Python and Streamlit
- Uses Groq’s `llama-4-scout` model
- Fast and responsive chat interface
- Clean chat history and clear chat option
- API key management using Streamlit Secrets

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hussain-jawaid/marsx-chatbot.git
   cd marsx-chatbot
   ```

2. **Install dependencies:**
   ``` commandline
   pip install -r requirements.txt
   ```

3. **Get API Key:**
   ```Browser
    https://console.groq.com/keys
   ```

4. **Run the Streamlit app:**
   ```commandline
    streamlit run app.py
   ```