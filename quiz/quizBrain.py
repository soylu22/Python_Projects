class QuizBrain():

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        answerGiven = input(f"Q.{self.question_number}, "
                            f"{new_question.text} (answer True or False)")
        self.check_answer(answerGiven, new_question.answer)


    def check_answer(self, answerGiven, correct_answer):
        if answerGiven.lower() == correct_answer.lower():
            self.score += 1
            print(f"correct, {self.score}/{self.question_number}")

        else:
            print("wrong")
            print(f"{self.score}/{self.question_number}")