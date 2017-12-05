'''
Created on 5 de dez de 2017

@author: maiconfz
'''
import unittest
from guess_probability.main import GuessProbability


class GuessProbabilityTest(unittest.TestCase):
    app = GuessProbability.App()

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGenerateRandomTestList(self):
        self.app.generateRandomTestList()
        self.assertEqual(self.app.config.testCount, len(self.app.testList), "Generated list doesn't match config test count")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()