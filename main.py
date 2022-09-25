from question_model import Question
from data import question_data

from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    # in the above line the new_question.text and new_question.answer is created
    question_bank.append(new_question)
#     now a list of objects is created, every object has new_question.text and new_question.answer

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've competed the quiz")
print(f"Your final score was: {quiz.score}")






