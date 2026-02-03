from data import question_data
from questionModel import Question
from quizBrain import QuizBrain

question_bank = []
for question in question_data:
    questionText = question["text"]
    questionAnswer = question["answer"]
    newQuestion = Question(questionText, questionAnswer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("complete!")
print(f"your final score is {quiz.score}/{quiz.question_number}")