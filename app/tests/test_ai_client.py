from app.ai_client import generate_ai_response


prompt = "Reply with exactly this text: Gemini connection OK"

response = generate_ai_response(prompt)

print(response)