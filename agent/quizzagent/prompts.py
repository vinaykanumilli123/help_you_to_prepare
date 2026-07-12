QUIZ_PROMPT = """
You are an expert quiz generator.

Using the study notes below, generate exactly 10 multiple-choice questions.

Requirements:

- Cover the important concepts.
- Each question must have exactly 4 options.
- Only one option is correct.
- Add a short explanation.
- Return ONLY valid JSON.

Format:

[
    {{
        "question": "...",
        "options": [
            "...",
            "...",
            "...",
            "..."
        ],
        "answer": "...",
        "explanation": "..."
    }}
]

Study Notes:

{notes}
"""