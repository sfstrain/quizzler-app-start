from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import html

open_trivia_api_url = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(url=open_trivia_api_url)
response.raise_for_status()
data = response.json()
# print(data)

questions = data["results"]
question_bank = []
for question in questions:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for question in question_bank:
#     print(f"{question.answer}: {question.text}")

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
