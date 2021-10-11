# Scrapping a webpage
## Install

pip install -U selenium


pip install bs4

## Usage
Open Firefox and run this code
### Example

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://coinmarketcap.com/currencies/' + cryptocurrencyname + '/news/'
driver = webdriver.Firefox()
driver.get(url)

page = driver.page_source
page_soup = BeautifulSoup(page, 'html.parser')
        
result = page_soup.findAll("section", "wrapper")

print(result[0].text)
