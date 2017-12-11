'''
Created on 5 de dez de 2017

@author: maiconfz
'''
from enum import IntEnum, auto

class AnswersStrategy(IntEnum):
    '''
    classdocs
    '''
    RANDOM = auto()
    SEQUENCE = auto()

    def __init__(self, params):
        '''
        Constructor
        '''
