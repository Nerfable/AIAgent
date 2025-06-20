import os
from dotenv import load_dotenv
from google import genai
import sys
if len(sys.argv) < 2:
    print("Script needs a  Prompt to run.")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key="AIzaSyDT_w99-fVgYuKBg7KUwwQsu8SNI6Bz7og")
user_prompt = sys.argv[1]
result = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=user_prompt
    )
response_tokens = result.usage_metadata.candidates_token_count
prompt_tokens = result.usage_metadata.prompt_token_count
print(result.text)    
if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

