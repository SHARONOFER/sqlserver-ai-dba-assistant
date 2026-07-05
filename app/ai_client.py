

from google import genai

from app.config import GEMINI_API_KEY


def generate_ai_response(prompt):
    """
    Sends the final DBA prompt to the Gemini LLM
    and returns the AI-generated response text.
    """
    print("[AI-1] Starting Gemini AI response generation...")

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

    client = genai.Client(api_key=GEMINI_API_KEY)
    print("[AI-2] Gemini client created.")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("[AI-3] Gemini response received.")

    return response.text