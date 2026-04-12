import openai

openai.api_key = "GOOGLE_API_KEY"

def evaluate_answer(question, answer):
    prompt = f"""
    Question: {question}
    Answer: {answer}

    Evaluate based on:
    - STAR Method
    - Clarity
    - Professional tone

    Give:
    1. Score out of 10
    2. 2 improvement tips

    Format:
    Score: X/10
    Tips:
    - tip1
    - tip2
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']