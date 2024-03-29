import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

def scrap_data():
    """This function scraps data from otomoto.pl and prints it to the console"""
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
            data_dict = {}
            for div in divs:
                pairs = div.find_all(["p", "a"])
                for i in range(0, len(pairs), 2):
                    key = pairs[i].get_text(strip=True)
                    value = pairs[i+1].get_text(strip=True)
                    data_dict[key] = value
            print_data(data_dict)
            print()

            # To można potem wyjebać na razie jest na testa żeby za szybko nie zapierniczał
            time.sleep(2)

    driver.quit()

def print_data(data_dict):
    """This function is beingused by scrap_data() to print data to the console"""
    for key, value in data_dict.items():
        print(f"{key}: {value}")
    print("-----------------------------------------")