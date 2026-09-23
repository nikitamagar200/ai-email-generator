# ✍️ AI Content & Email Generator

A Generative AI application built with **Python, Streamlit, LangChain, and Groq** that generates different types of content based on user instructions.

## Features

* 📧 Generate Emails
* 💼 Generate LinkedIn Posts
* 📝 Generate Blogs
* 🛍️ Generate Product Descriptions
* Select **Tone**: Professional, Friendly, Formal
* Select **Length**: Short, Medium, Long
* Edit generated content
* Copy content to clipboard
* Download generated content
* Input validation and error handling

## Technologies

* Python
* Streamlit
* LangChain
* Groq LLM
* Prompt Engineering

## Project Structure

```text
AI Content Generator/
├── app.py
├── email_generator.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

```text
User Input
    ↓
Streamlit UI
    ↓
PromptTemplate
    ↓
LangChain
    ↓
Groq LLM
    ↓
Generated Content
```

## Deployment

The application can be deployed using **Streamlit Community Cloud**.

## Author

**Nikita Magar**
