from random import choice
from bs4 import BeautifulSoup
import requests

def BBC_News():
    url = "https://www.bbc.com"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    dic = [item 
       for item in soup.select(".media__summary")]

    elem = choice(dic)

    c = elem.select(".media__summary")

    print(f'{elem}')



BBC_News()