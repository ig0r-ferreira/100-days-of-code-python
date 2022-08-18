from random import shuffle
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]
shuffle(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You complete the quiz.\n"
      f"Your final score is: {quiz.score}/{quiz.question_number}")
