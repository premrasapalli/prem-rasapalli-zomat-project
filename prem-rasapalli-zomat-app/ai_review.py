import vertexai
from vertexai.generative_models import GenerativeModel
import os
import sys

def ai_review():
    try:
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
        location = "asia-south1"

        # Initialize Vertex AI properly
        vertexai.init(project=project_id, location=location)

        model = GenerativeModel("gemini-1.5-flash")

        prompt = "Review this FastAPI code:\n@app.get('/')\ndef home(): return {'msg':'hello'}"

        response = model.generate_content(prompt)

        print("AI Review Output:\n")
        print(response.text)

    except Exception as e:
        print(f"AI Review Failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    ai_review()
