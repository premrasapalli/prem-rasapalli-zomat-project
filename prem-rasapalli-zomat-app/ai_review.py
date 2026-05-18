import vertexai
from vertexai.generative_models import GenerativeModel

def review_code():
    try:
        vertexai.init(
            project="project-zomat-app",
            location="us-central1"
        )

        model = GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            "Review this FastAPI code and suggest improvements"
        )

        print("\n✅ AI Code Review Output:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
