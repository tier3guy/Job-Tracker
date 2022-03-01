
from bs4 import BeautifulSoup

def get_price(cards, name):

  price = "Course not found"
  for card in cards:
    if card.h5.text == name:
      price = card.a.text
      break

  return price

def __main__():

  with open('./Web/main.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    cards = soup.find_all('div', class_ = 'card')
    
    print(get_price(cards, "Django"))

__main__()