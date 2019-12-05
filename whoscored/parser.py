from bs4 import BeatifulSoup

class ParseGame:
    def __init__(self, url):
        self._url = url
    
    def __str__(self):
        '''
        Return name of the game
        '''
        return self._name