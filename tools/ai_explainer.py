"""
AICraft AI Code Explainer

Use AI to explain source code.
"""

import os
import sys

from openai import OpenAI


def explain_code(filename):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:
        code = file.read()


    client = OpenAI(
        api_key=os.environ.get(
            "OPENAI_API_KEY"
        )
    )


    response = client.responses.create(
        model="gpt-5",
        input=f"""
Explain this Python code
for a beginner developer:

{code}
"""
    )


    print(response.output_text)



if __name__ == "__main__":

    if len(sys.argv) < 2:

        print(
            "Usage: python ai_explainer.py <file>"
        )

    else:

        explain_code(
            sys.argv[1]
        )
