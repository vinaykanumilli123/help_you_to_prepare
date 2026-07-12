WEAK_CONCEPT_PROMPT = """
You are an educational evaluator.

Below are the questions answered incorrectly by a student.

{wrong_answers}

Identify only the concepts the student is weak in.

Return ONLY JSON.

Example:

{{
    "weak_concepts":[
        "JSON-RPC",
        "Client Server Architecture"
    ]
}}
"""