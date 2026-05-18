import os
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

def review_code():
    try:
        # ✅ Explicit credentials loading (CRITICAL FIX)
        creds = service_account.Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        )

        vertexai.init(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location="us-central1",
            credentials=creds   # 🔥 THIS FIXES 401
        )

        model = GenerativeModel("gemini-1.5-flash")

        response = model.generate_content("Review this Python code")

        print("\n✅ AI Code Review:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
