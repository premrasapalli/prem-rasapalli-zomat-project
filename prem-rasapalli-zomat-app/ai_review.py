import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

def review_code():
    try:
        # ✅ FORCE credentials from GitHub runner
        credentials = service_account.Credentials.from_service_account_file(
            "key.json"
        )

        vertexai.init(
            project="project-zomat-app",
            location="us-central1",
            credentials=credentials
        )

        model = GenerativeModel("gemini-1.5-flash")

        response = model.generate_content("Review this code")

        print("\n✅ AI Code Review:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
