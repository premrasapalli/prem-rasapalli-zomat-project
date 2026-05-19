from google import genai
import os

def review_code():
    try:
        # Initialize Gemini client using API key
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        # ✅ Use stable working model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Review this FastAPI project and suggest improvements"
        )

        print("\n✅ AI Code Review Output:\n")
        print(response.text)

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        exit(1)

if __name__ == "__main__":
    review_code()
