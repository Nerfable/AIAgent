import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key="AIzaSyDT_w99-fVgYuKBg7KUwwQsu8SNI6Bz7og")

result = client.models.generate_content(
    model="gemini-2.0-flash-001", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
print(result.text)    
print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
print(f"Response tokens: {result.usage_metadata.candidates_token_count}")