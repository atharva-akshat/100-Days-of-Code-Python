class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.questionNumber = 0
        self.questionList = q_list

    def checkAnswer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's the wrong answer.")
            print("The correct answer was {}".format(answer))
        print("Score: {}/{}".format(self.score, self.questionNumber + 1))

    def next_question(self):
        self.checkAnswer(input(
            "\nQ.{}. {} (True/False): ".format(self.questionNumber + 1,
                                               self.questionList[self.questionNumber].text)), self.questionList[
            self.questionNumber].answer)

        self.questionNumber += 1

    def still_has_questions(self):
        return self.questionNumber < len(self.questionList)
