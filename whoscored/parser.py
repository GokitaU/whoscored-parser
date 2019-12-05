from bs4 import BeatifulSoup
from request import get_page

class ParseGame:
    def __init__(self, url):
        self._url = url
    
    def parse(self):
        page = get_page(self._url)
        soup = BeautifulSoup(page, 'html.parser')
    
    def __str__(self):
        '''
        Return name of the game
        https://1xbet.whoscored.com/Matches/1376071/Live/England-Premier-League-2019-2020-Crystal-Palace-Bournemouth
        '''
        return self._name