from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class mercadolibreSearch(BasePage):
    SEARCH_BOX = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button')

    def search(self, search):
        self.enter_text(self.SEARCH_BOX, search)
        self.click(self.SEARCH_BUTTON)

class mercadolibreResults(BasePage):
    PRODUCT_TITLES = (By.CLASS_NAME, 'poly-component__title')

    def get_product_titles(self):
        return self.find_element(self.PRODUCT_TITLES)