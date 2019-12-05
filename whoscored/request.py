import requests

def get_page(url):
    '''
        returns text representation of html page
    '''
    return requests.get(url).text