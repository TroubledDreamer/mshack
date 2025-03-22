import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import AzureOpenAI

app = Flask(__name__)

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")


client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-05-01-preview",
)

@app.route("/createassessment", methods=["POST"])
def scores():
    print("SUp")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
