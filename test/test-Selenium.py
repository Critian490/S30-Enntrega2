from selenium import webdriver

def test_dynamic_reviews():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))

