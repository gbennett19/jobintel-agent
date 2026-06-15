import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("FOUNDRY_ENDPOINT"),
    api_key=os.getenv("FOUNDRY_API_KEY"),
    api_version="2024-12-01-preview"
)

with open("job.txt", "r") as f:
    job_description = f.read()

print("Analyzing job description...")

response = client.chat.completions.create(
    model=os.getenv("AZURE_DEPLOYMENT"),
    messages=[
        {
            "role": "system",
            "content": "You are a career advisor using Foundry IQ grounded knowledge retrieval. Be concise and specific."
        },
        {
            "role": "user",
            "content": f"Analyze this job description. List: required skills, experience level, and 3 preparation tips.\n\n{job_description}"
        }
    ],
    max_tokens=400
)

print("\n--- JobIntel Agent ---")
print(response.choices[0].message.content)