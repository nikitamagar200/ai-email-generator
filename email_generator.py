from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b", temperature=0.7)

CONTENT_INSTRUCTIONS = {

    "Email": """
Create a properly structured email.

Include:
- A suitable subject line
- Appropriate greeting
- Clear and concise body
- Professional closing
""",

    "LinkedIn Post": """
Create an engaging LinkedIn post.

Include:
- An attention-grabbing opening
- Clear and useful content
- Professional and natural language
- A strong conclusion
- Relevant hashtags when appropriate
""",
 "Blog": """
Create a well-structured blog article.

Include:
- An appropriate title
- Introduction
- Relevant headings and sections
- Useful and easy-to-understand content
- Conclusion
""",

    "Product Description": """
Create an attractive product description.

Include:
- Product overview
- Key features
- Customer benefits
- Persuasive but natural language
- A suitable call to action
"""
}



prompt = PromptTemplate(
    input_variables=["content_type", "tone", "length", "content_instruction","instruction"],
    template = """
    You are an expert AI content writer.

Your task is to generate high-quality content based on the user's instruction.

Content Type:
{content_type}

Tone:
{tone}

Length:
{length}

Content Requirements:
{content_instruction}

User Instruction:
{instruction}

Important rules:
1. Follow the requested content type.
2. Maintain the requested tone.
3. Follow the requested length.
4. Correct grammar and spelling mistakes.
5. Do not invent unnecessary facts.
6. Make the content clear and natural.
7. Return only the final generated content.
"""
)

chain = prompt | llm

