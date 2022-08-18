from typing import List
from question_model import Question


class QuizBrain:
    def __init__(self, question_list: List[Question]):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_answer = input(f"Question {self.question_number}: {current_question.text} (True/False)?: ").lower()
            if user_answer in ("true", "false"):
                break
            print("Type only true or false.")

        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You're right!")
        else:
            print("You missed!")

        print(f"The correct answer is: {correct_answer}.\n"
              f"Your current score is: {self.score}/{self.question_number}.\n")
