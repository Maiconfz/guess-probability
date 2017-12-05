'''
Created on 5 de dez de 2017

@author: maiconfz
'''

import logging
from .AppConfig import AppConfig
from .AnswersStrategy import AnswersStrategy 
from random import randint

if __name__ == '__main__':
    pass


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
        self.testAnswers = []
        self.testAnswers.insert(AnswersStrategy.RANDOM, [])

    def run(self):
        logging.debug("App started running")

    def generateRandomTestList(self):
        logging.debug("Generating new random test list")
        i = self.config.testCount
        while i != 0:
            self.testList.append(self.generateRandomIntList(self.config.testQuestionCount, 1, self.config.testQuestionAnswersCount))
            i -= 1
        logging.debug("Generated a list containing", len(self.testList), "tests")
    
    def generateRandomStrategyTestAnswers(self):
        i = self.config.testAnswersCount
        while i != 0:
            self.testAnswers[AnswersStrategy.RANDOM].append(self.generateRandomIntList(self.config.testAnswersCount, 1, self.config.testQuestionAnswersCount))
            i -= 1
    
    def generateRandomIntList(self, listSize, minValue, maxValue):
        generatedList = []
        i = listSize
        
        while i != 0:
            generatedList.append(randint(minValue, maxValue))
            i -= 1
        
        return generatedList