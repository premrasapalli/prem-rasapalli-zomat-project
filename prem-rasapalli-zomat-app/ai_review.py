import os
import vertexai
from vertexai.generative_models import GenerativeModel

def review_code():
    try:
        # ✅ CRITICAL: Initialize Vertex AI
        vertexai.init(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location="us-central1"   # REQUIRED
        )

        # ✅ Use stable model
        model = GenerativeModel("gemini-1.5-flash")

        prompt = "Review this Python code and suggest improvements:\n\nprint('Hello World')"

        response = model.generate_content(prompt)

        print("\n✅ AI Code Review:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
