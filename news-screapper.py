import requests
from bs4 import BeautifulSoup

news1 = 'https://kathmandupost.com/'
response1 = requests.get(news1)



soup = BeautifulSoup(response1.text,'lxml')
print(soup.prettify())

print(soup.h1.text)