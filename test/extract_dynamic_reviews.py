from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from unittest.mock import patch
import pytest
from main import extract_dynamic_reviews

def test_extract_dynamic_reviews():
    # Configurar Selenium en modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Mock del controlador Chrome
    with patch('main.webdriver.Chrome') as MockWebDriver:
        mock_driver = MockWebDriver.return_value
        mock_driver.find_elements.return_value = [
            Mock(text="Reseña 1"),
            Mock(text="Reseña 2"),
            Mock(text="Reseña 3"),
        ]
        reviews = extract_dynamic_reviews("mock_url")

    assert len(reviews) == 3
    assert reviews == ["Reseña 1", "Reseña 2", "Reseña 3"]
