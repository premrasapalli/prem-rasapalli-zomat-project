import vertexai
from vertexai.generative_models import GenerativeModel

def review_code():
    try:
        # Initialize Vertex AI
        vertexai.init(
            project="project-zomat-app",
            location="us-central1"
        )

        # Load Gemini model
        model = GenerativeModel("gemini-1.5-flash")

        # Prompt
        response = model.generate_content(
            "Review this FastAPI project and suggest improvements"
        )

        print("\n✅ AI Code Review Output:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
