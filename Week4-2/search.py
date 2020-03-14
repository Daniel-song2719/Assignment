import requests
from bs4 import BeautifulSoup

url = input('여러분이 검색하기 원하는 페이지는? (형식 : www.abcd.com): ')
response = requests.get('https://' + url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))