from google import genai

# ⚠️ TEMPORARY: hard-coded API key (DO NOT COMMIT THIS)
API_KEY = "AIzaSyA8q-u9b6qqm8DfM5X-CYlDpDN308ZDwcE"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="hello gemini "
)

print(response.text)
