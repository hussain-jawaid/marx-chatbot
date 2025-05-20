import streamlit as st
from groq import Groq


class ChatBot:
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.chatbot_ui()


    def chatbot_ai(self, prompt):
        client = Groq(api_key=self.API_KEY)
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            response_text += content
        return response_text


    def chatbot_ui(self):
        with st.sidebar:
            # Info section
            st.markdown("# About")
            st.markdown("""
            MarsX is an AI chatbot powered by Groq's 
            ultra-fast LLM inference engine.
            """)

            st.markdown("---")

            st.markdown("### Resources")
            st.markdown("""
            - [Get API Key](https://console.groq.com/keys)
            - [Source Code](https://github.com/hussain-jawaid/marx-chatbot)
            - [Groq Documentation](https://groq.com/docs)
            """)

            st.markdown("---")

            if st.button("Clear Chat"):
                st.session_state.chat_history = []

        st.markdown("<h1 style='text-align: center;'>Hi, I'm MarsX.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>How can I help you today?</p>", unsafe_allow_html=True)

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for speaker, message in st.session_state.chat_history:
            with st.chat_message(name=speaker):
                st.write(message)

        user_input = st.chat_input("Ask anything")

        if user_input:
            with st.chat_message("user"):
                st.write(user_input)

            response = self.chatbot_ai(user_input)
            with st.chat_message("assistant"):
                st.write(response)

            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("assistant", response))


if __name__ == '__main__':
    api_key = st.secrets["groq"]["api_key"]
    ChatBot(api_key)