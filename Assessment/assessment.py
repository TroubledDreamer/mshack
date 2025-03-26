import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import AzureOpenAI
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enables CORS for all routes

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
def generate_response():
    data = request.get_json()
    speak = data.get("speak")
    learn = data.get("learn")
    job = data.get("job")
    score = data.get("score")

    def choose_difficulty(score):
        return max(1, min(10, score // 10))

    difficulty = choose_difficulty(score)

    if not speak or not learn or not job:
        return jsonify({"error": "You need to put in the language you speak, the language you want to learn, the job that you are interested in or the score"}), 400

    
    chat_prompt = [
        {
            "role": "system",
            "content":"\nYou are a friendly language teacher, that teaches users a target language in their native language. Your job is to first teach a topic, create an assessment of 5 questions and explain answers. Your response should be in json format. Questions should be based on the language that they speak, the language they want to learn, and also the job that they would like to be hired to do. \n\nYour assessment should have questions primarily related to the job. The assessment should have 2 multiple choice, 2 true or false and 1 short answer.\n\nFirst, teach the student an aspect of the language depending on the job that they are interested in. Then, give them the assessment. The assessment difficulty is out of 10. 1 is the easiest, 10 is the hardest. The difficulty for this assessment is" "{difficulty}" "Explain why the answers are correct.\n"
        },
        {
            "role": "user",
            "content": f'"Speak": "{speak}"\n"Learn": "{learn}"\n"Job": "{job}"\n"Difficulty": "2"\n',
        },
        {
        "role": "assistant",
        "content": "{\n  \"teaching\": \"As a zookeeper, it's important to be able to communicate with visitors and colleagues in Spanish to ensure the safety and well-being of the animals under your care. One key phrase you can learn is '¿Dónde está el elefante?' which means 'Where is the elephant?' This phrase can help you locate animals and provide information to visitors.\",\n  \"assessment\": {\n    \"questions\": [\n      {\n        \"question\": \"¿Dónde está el elefante? translates to:\",\n        \"choices\": [\n          \"How are you?\",\n          \"Where is the elephant?\",\n          \"What time is it?\",\n\"What is your name?\"\n\t\n        ],\n        \"answer\": \"Where is the elephant?\",\n        \"type\": \"multiple choice\"\n      },\n      {\n        \"question\": \"Tigre is the Spanish word for 'lion'.\",\n        \"answer\": false,\n        \"type\": \"true or false\"\n      },\n        \"answer\": true,\n        \"type\": \"true or false\"\n      },\n      {\n        \"question\": \"What is the Spanish word for 'giraffe'?\",\n        \"answer\": \"jirafa\",\n        \"type\": \"short answer\"\n      },\n      {\n        \"question\": \"Which animal is 'el oso' in Spanish?\",\n        \"choices\": [\n          \"Elephant\",\n          \"Bear\",\n          \"Zebra\",\n\t\"Cow\"\n\n        ],\n        \"answer\": \"Bear\",\n        \"type\": \"multiple choice\"\n      }\n    ],\n\n\n    \"answers_explanation\": {\n      \"question_1\": \"The correct translation of '¿Dónde está el elefante?' is 'Where is the elephant?' This phrase can help you locate specific animals.\",\n      \"question_2\": \"The statement is false. 'Tigre' in Spanish translates to 'tiger', not 'lion'.\",\n      \"question_3\": \"The statement is true. Monkeys are commonly found in zoos around the world as part of the animal exhibits.\",\n      \"question_4\": \"The Spanish word for 'giraffe' is 'jirafa'.\",\n      \"question_5\": \"'El oso' in Spanish refers to a 'bear'.\"\n    }\n  }\n}\n\n"
    }
    ]

    try:
        completion = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=chat_prompt,
            max_tokens=1000,
            temperature=0.9,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False,
        )

        return jsonify(completion.to_dict()['choices'][0]['message']['content']), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)