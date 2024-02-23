import requests
from bs4 import BeautifulSoup   
url = 'https://www.youtube.com/'
response = requests.get(url=url)
 
soup = BeautifulSoup(response.text, 'lxml')
print(soup.title.text)


