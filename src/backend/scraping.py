from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_travel_data(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return soup