import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

from dictionaries_fucntions import filter_data
from database_functions import save_to_mongodb

def scrap_data(num_pages):
    """This function scraps data from otomoto.pl and saves it to MongoDB"""
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=service, options=options)

    for page_number in range(1, num_pages + 1):
        print("next page")
        url = f"https://www.otomoto.pl/osobowe?page={page_number}"
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
                        if i + 1 < len(pairs):  # Check if pairs[i+1] exists
                            key = pairs[i].get_text(strip=True)
                            value = pairs[i+1].get_text(strip=True)
                            data_dict[key] = value
                
                filtered_data = filter_data(data_dict)
                save_to_mongodb(filtered_data) 
                
                time.sleep(1)

    driver.quit()

