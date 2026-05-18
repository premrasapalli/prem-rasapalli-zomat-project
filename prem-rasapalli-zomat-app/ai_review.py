import vertexai
from vertexai.generative_models import GenerativeModel


def review_code():
    try:
        # ✅ Initialize Vertex AI (IMPORTANT: project must match GCP)
        vertexai.init(
            project="project-zomat-app",
            location="us-central1"
        )

        # ✅ Use Gemini model
        model = GenerativeModel("gemini-1.5-flash")

        # ✅ Send prompt
        response = model.generate_content(
            "Review this Python FastAPI code and suggest improvements:\n\n"
            "from fastapi import FastAPI\n"
            "app = FastAPI()\n"
            "@app.get('/')\n"
            "def home(): return {'msg':'hello'}"
        )

        print("\n✅ AI Code Review Output:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)


if __name__ == "__main__":
    review_code()
