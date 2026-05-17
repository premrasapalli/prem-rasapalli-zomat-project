import os
import sys
import vertexai
from vertexai.generative_models import GenerativeModel

def ai_review():
    try:
        # Initialize Vertex AI
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
        location = "asia-south1"

        vertexai.init(project=project_id, location=location)

        # Load model
        model = GenerativeModel("gemini-1.5-pro")

        # Sample input (later we will pass PR diff)
        prompt = "Review this Python FastAPI code and suggest improvements:\n\n@app.get('/')\ndef home(): return {'msg':'hello'}"

        # Generate response
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"AI Review Failed: {str(e)}"


if __name__ == "__main__":
    result = ai_review()
    print(result)

    if "Failed" in result:
        sys.exit(1)
    else:
        sys.exit(0)
