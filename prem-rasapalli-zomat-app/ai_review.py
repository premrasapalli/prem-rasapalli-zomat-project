import os
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location="us-central1"
)

model = GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Review this code")

print(response.text)
