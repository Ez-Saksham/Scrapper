import requests
from bs4 import BeautifulSoup

news1 = 'https://kathmandupost.com/'
response1 = requests.get(news1)



soup = BeautifulSoup(response1.text,'html.parser')


# match0 = soup.find('article',class_='1')
# main_headline = match0.h2.a.text
# print(main_headline)
 

# match1 = soup.find('article',class_='article-image article-image--left 3')
# news_headline = match1.h3.a.text
# print(news_headline)


# match2 = soup.find('article',class_='article-image article-image--left 2')
# news_headline = match2.h3.a.text
# print(news_headline)



# match3 = soup.find('article',class_='article-image article-image--left 4')
# news_headline = match3.h3.a.text
# print(news_headline)


trending = soup.find('ul',class_='trending-topics-list')
trending_list = trending.find_all('a')
whats_new =[]
for a in range(len(trending_list)):
#   print(trending_list[a].get('href'))
  whats_new = "https://kathmandupost.com"+trending_list[a].get('href')
#   whats_new=a.get('href')
  print(whats_new)
   
  news2 = whats_new
  response2 = requests.get(news2)
  soup1 = BeautifulSoup(response2.text,'html.parser')
  
  match5 = soup1.find('div',class_='col-sm-8')
  main_headline = match5.h1.text
  print(main_headline)