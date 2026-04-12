import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_questions(profile_text):
    model = genai.GenerativeModel("gemini-1.5-flash")

    profile_text = profile_text[:1200]  # trim

    prompt = f"""
    Generate 3 short interview questions from this:

    {profile_text}
    """

    response = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 120
        }
    )

    return response.text