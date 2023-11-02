"""Question"""
import random


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()


q1 = Question(
    "En İyi Programlama Dili Hangisidir?",
    ["C#", "Python", "Javascript", "Java"],
    "Python",
)

q2 = Question(
    "En Popüler Programlama Dili Hangisidir?",
    ["C#", "Python", "Javascript", "Java"],
    "Python",
)
q3 = Question(
    "En Çok Kazandıran Programlama Dili Hangisidir?",
    ["C#", "Python", "Javascript", "Java"],
    "Python",
)

liste = [q1, q2, q3]
questions = [q1, q2, q3]

quiz = Quiz(questions)
question = quiz.getQuestion()

question = quiz.questions[quiz.questionIndex]

""" print(question)

print(question.text) """

quiz.displayQuestion()
