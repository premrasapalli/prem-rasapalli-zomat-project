import os
import vertexai
from vertexai.generative_models import GenerativeModel

def review_code():
    try:
        vertexai.init(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location="us-central1"
        )

        model = GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            "Review this Python code and suggest improvements:\n\nprint('Hello World')"
        )

        print("\n✅ AI Code Review:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
