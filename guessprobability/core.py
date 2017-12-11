'''
Created on 5 de dez de 2017

@author: maiconfz
'''

import logging
from guessprobability.app_config import AppConfig
from guessprobability.answers_strategy import AnswersStrategy
from random import randint, seed
from builtins import Exception


class App:
    config = None
    testList = None
    testAnswers = None

    def __init__(self):
        logging.debug("Initializing")

        self.config = AppConfig()
        self.config.testCount = 1000
        self.config.testQuestionCount = 10
        self.config.testQuestionAnswersCount = 5
        self.config.testAnswersCount = 100

        self.testList = []
        self.testAnswers = { AnswersStrategy.RANDOM: [] }

    def runTests(self):
        logging.debug("App started running")
        successRate = 0

        self.generateRandomTestList()
        self.generateRandomStrategyTestAnswers()

        for testAnswerList in self.testAnswers[AnswersStrategy.RANDOM]:
            for questions in self.testList:
                successRate += self.testAgainst(testAnswerList, questions)

        successRate /= (len(self.testList) * len(self.testAnswers[AnswersStrategy.RANDOM]))
        print(str(successRate / self.config.testQuestionAnswersCount * 100) + "%")

    def testAgainst(self, answers, questionAnswers):
        if len(answers) != len(questionAnswers):
            raise Exception("Arg lists doesn't match in size")

        correctAnswersCount = 0

        for x, i in zip(answers, questionAnswers):
            if x == i:
                correctAnswersCount += 1

        return correctAnswersCount

    def generateRandomTestList(self):
        logging.debug("Generating new random test list")
        i = self.config.testCount
        while i != 0:
            self.testList.append(self.generateRandomIntList(self.config.testQuestionCount, 1, self.config.testQuestionAnswersCount))
            i -= 1
        logging.debug("Generated a list containing %s tests", len(self.testList))

    def generateRandomStrategyTestAnswers(self):
        i = self.config.testAnswersCount
        while i != 0:
            self.testAnswers[AnswersStrategy.RANDOM].append(self.generateRandomIntList(self.config.testQuestionCount, 1, self.config.testQuestionAnswersCount))
            i -= 1

    def generateRandomIntList(self, listSize, minValue, maxValue):
        generatedList = []
        i = listSize

        while i != 0:
            generatedList.append(randint(minValue, maxValue))
            i -= 1

        return generatedList


if __name__ == '__main__':
    app = App()
    for i in range(100):
        app.runTests()
