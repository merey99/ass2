from bs4 import BeautifulSoup
from selenium import webdriver

class Scrap:
    def pullData(self, cryptocurrency):
        url = 'https://coinmarketcap.com/currencies/' + cryptocurrency + '/news/'
        driver = webdriver.Firefox()
        driver.get(url)
        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')
        print(cryptocurrency.capitalize(), end=':\n')
        title = page_soup.findAll("h3", {"class": "sc-1q9q90x-0", "class": "gEZmSc"})
        text = page_soup.findAll("p", {"class": "sc-1eb5slv-0", "class": "svowul-3", "class": "ddtKCV"})
        for i in range(0, min(len(title), len(text))):
            print(title[i].text.strip(), '\n', 'More:', text[i].text.strip(), '\n')

scrapper = Scrap()
scrapper.pullData('bitcoin')
scrapper.pullData('lightning')