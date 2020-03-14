from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.melon.com/chart/index.htm')

data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')

    
notices = soup.find_all(class_ = 'ellipsis rank01')

for n in notices:
    print(n.text.strip())