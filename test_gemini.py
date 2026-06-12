import os
from dotenv import load_dotenv
import google.genai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Test prompt
response = model.generate_content(
    "Summarize the latest advancements in Artificial Intelligence in 5 bullet points."
)

print("\n===== GEMINI RESPONSE =====\n")
print(response.text)