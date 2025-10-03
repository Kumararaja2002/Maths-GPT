# 🔍 Math Solver & Wikipedia Assistant with Groq & Streamlit

This project is a Streamlit-based chatbot that uses LangChain tools to solve math problems, perform logical reasoning, and search Wikipedia. It is powered by Groq's Gemma2-9B model and provides interactive, step-by-step responses.

## 🚀 Features

- Chatbot interface using Streamlit
- Solves arithmetic and logical reasoning problems
- Wikipedia search integration
- Uses LangChain tools and agents
- Displays agent thoughts and responses interactively

## 🧠 Technologies Used

- LangChain
- Groq API (Gemma2-9B)
- Wikipedia API Wrapper
- LLMMathChain
- Streamlit
- Python
- dotenv

## 📁 File Structure

- `app.py`: Main Streamlit application
- `.env`: Stores your Groq API key

## 🔐 Environment Variables

Create a `.env` file with the following key:


GROQ_API_KEY=your_groq_api_key

## 🛠️ How to Run

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/math-wiki-chatbot.git
   cd math-wiki-chatbot
   ```
2. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
3. Add your .env file with API keys.

4. Run the Streamlit app:
  ```
  streamlit run app.py
  ```
