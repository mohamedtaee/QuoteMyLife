from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from utils.mongo_db import MongoDB
# from scripts import openai_prompt

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/ai')
# def ai_prompt():
#     userid = request.args.get('userid')
#     holy_book = request.args.get('holybook')
#     holy_figure = request.args.get('holyfigure')
#     question = request.args.get('question')

#     openai_response = openai_prompt.ai_prompt(question=question, holybook=holy_book, holyfigure=holy_figure)
#     response_id = openai_response.id

#     print(openai_response)

#     answer = openai_response.choices[0].text.strip()

#     mongo = MongoDB()
#     mongo.store_openai_response(openai_response)

#     mongo.store_qa(user_id=userid,
#                    question=question,
#                    answer=answer,
#                    holybook=holy_book,
#                    holyfigure=holy_figure,
#                    response_id=response_id)

#     print("The answer", answer)
#     return jsonify(answer)


# @app.route('/mongo')
# def add_user():
#     userid = request.args.get('userid')
#     first_name = request.args.get('firstname')
#     last_name = request.args.get('lastname')
#     email = request.args.get('email')

#     user = {"user_id": userid,
#             "first_name": first_name,
#             "last_name": last_name,
#             "email": email
#             }

#     mongo = MongoDB()

#     if mongo.add_user(user):
#         return jsonify({"status": "success"})
#     else:
#         return jsonify({"status": "error"})


# @app.route('/questions_remaining')
# def questions_remaining():
#     userid = request.args.get('userid')

#     mongo = MongoDB()

#     return jsonify(mongo.get_questions_remaining(userid))


# @app.route('/questions_remaining_decrement')
# def questions_remaining_decrement():
#     userid = request.args.get('userid')

#     mongo = MongoDB()

#     return jsonify(mongo.decrement_questions_remaining(userid))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')