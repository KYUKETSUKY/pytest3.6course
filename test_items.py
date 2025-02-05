
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    
    add_to_card_button=browser.find_elements(By.CSS_SELECTOR, '[class="btn "]')
    assert len(add_to_card_button) is not 0, 'Кнопка добавления товара в корзину отсутствует'