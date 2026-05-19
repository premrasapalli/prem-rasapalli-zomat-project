import google.generativeai as genai
import os

def review_code():
    try:
        # ✅ Use API Key (NOT Vertex AI)
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel("gemini-1.5-flash")

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
