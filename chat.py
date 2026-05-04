from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()

language = input("Enter the programming language: ")
requirement = input("Write the coding problem: ")
system_propmt = "You are a coding bot who only writes code to solve the given problem" \
"in given language according to the requirements of client. Generate easy to understand code and follow the programming conventions.If" \
"you don't know the programming language, just say I don't know this programming language."
api = os.getenv("GEMINI_API_KEY")
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config = types.GenerateContentConfig(
        system_instruction=system_propmt
    ),
    contents=f"""Programming language: {language}
    Problem: {requirement}"""
)
if "i don't know" or "i don't know this programming language" in response.text.lower():
    print(response.text) 
else:
    file = "code.py"
    with open (file, "w") as f:
        f.write(response.text)

