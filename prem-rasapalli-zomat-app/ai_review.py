import requests
import os

OLLAMA_URL = "http://localhost:11434/api/generate"


def get_code():
    code = ""
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                try:
                    with open(os.path.join(root, file), "r") as f:
                        code += f"\n# File: {file}\n" + f.read()
                except:
                    pass
    return code


def review_code():
    try:
        code = get_code()

        if not code.strip():
            print("⚠️ No Python files found")
            return

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3:8b",
                "prompt": f"Review this code and suggest improvements:\n{code}",
                "stream": False
            },
            timeout=120
        )

        result = response.json()

        print("\n✅ AI REVIEW RESULT:\n")
        print(result.get("response", "No response"))

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        # IMPORTANT: Don't fail pipeline
        print("⚠️ Continuing pipeline...")


if __name__ == "__main__":
    review_code()
