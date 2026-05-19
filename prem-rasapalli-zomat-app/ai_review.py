import os
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account


def review_code():
    try:
        # ✅ FORCE load credentials from GitHub Actions env
        creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        credentials = service_account.Credentials.from_service_account_file(
            creds_path
        )

        vertexai.init(
            project="project-zomat-app",
            location="us-central1",
            credentials=credentials
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
