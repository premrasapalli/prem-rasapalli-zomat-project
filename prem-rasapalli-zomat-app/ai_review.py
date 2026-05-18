import vertexai
from vertexai.generative_models import GenerativeModel
import os

vertexai.init(
    project="project-zomat-app",
    location="us-central1" 
)
)

model = GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Review this code")

print(response.text)
