import os
import google.genai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "   gemini-2.5-flash-lite"
)

response = model.generate_content(
    "Summarize the latest AI developments."
)

print(response.text)