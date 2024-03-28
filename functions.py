import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

service = Service(GeckoDriverManager().install())
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)

url = "https://www.otomoto.pl/osobowe"
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
articles = soup.find_all("article", class_="ooa-yca59n")

for article in articles:
    link = article.find("a", href=True)
    if link:
        article_url = link['href']
        driver.get(article_url)
        article_soup = BeautifulSoup(driver.page_source, "html.parser")
        divs = article_soup.find_all("div", {"data-testid": "advert-details-item"})
        for div in divs:
            paragraphs = div.find_all(["p", "a"])
            for element in paragraphs:
                print(element.text.strip())
            print()
        print("-----------------------------------------")
        
        # To jest test, na razie
        time.sleep(8)

driver.quit()
