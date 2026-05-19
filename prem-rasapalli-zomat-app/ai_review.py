import requests
import os
import subprocess

OLLAMA_URL = "http://localhost:11434/api/generate"


def get_changed_code():
    try:
        files = subprocess.getoutput("git diff --name-only HEAD~1").split("\n")
    except:
        files = []

    code = ""

    for file in files:
        if file.endswith(".py") and os.path.exists(file):
            try:
                with open(file, "r") as f:
                    code += f"\n# File: {file}\n" + f.read()
            except:
                pass

    return code


def review_code():
    try:
        code = get_changed_code()

        if not code.strip():
            print("⚠️ No changed Python files found")
            return

        print("⏳ Sending code to Ollama...")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3:8b",
                "prompt": f"Review this FastAPI code and suggest improvements:\n{code}",
                "stream": False
            },
            timeout=300
        )

        result = response.json()

        print("\n✅ AI REVIEW RESULT:\n")
        print(result.get("response", "No response"))

    except Exception as e:
        print("❌ AI Review Failed:", str(e))
        print("⚠️ Skipping AI and continuing pipeline...")


if __name__ == "__main__":
    review_code()
