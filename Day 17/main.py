from art import logo
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

print(logo)
questionBank = []
for i in question_data:
    questionBank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(questionBank)
while quiz.still_has_questions():
    quiz.next_question()
print("\nQuiz completed!")
print("Final Score: {}/{}".format(quiz.score, quiz.questionNumber))
