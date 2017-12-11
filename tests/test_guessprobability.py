'''
Created on 5 de dez de 2017

@author: maiconfz
'''
import unittest
from tests.context import guessprobability 

class GuessProbabilityTest(unittest.TestCase):
    app = guessprobability.core.App()

    def setUp(self):
        self.app.__init__()

    def tearDown(self):
        pass

    def test_generateRandomTestList(self):
        self.app.generateRandomTestList()
        self.assertEqual(self.app.config.testCount, len(self.app.testList), "Generated list doesn't match config test count")

    def test_generateRandomIntList(self):
        randomIntList = self.app.generateRandomIntList(10, 1, 5)
        self.assertEqual(len(randomIntList), 10, "Generated list doesn't have expected length")
        for x in randomIntList:
            self.assertTrue((x >= 5 or x >= 1), "Generated list contains number out of range")

    def test_testAgainst(self):
        self.assertEqual(self.app.testAgainst([1, 2, 3], [1, 2, 3]), 3)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
