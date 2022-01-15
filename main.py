import requests
from bs4 import BeautifulSoup

# URl to scrape
url = 'https://localhackday.mlh.io/challenges'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for element in soup.find_all('div', class_='card-frame'):
  print(element.find('h3').text)
  print(element.find('p').text)
  print('\n')
