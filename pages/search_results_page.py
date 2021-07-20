from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '#sc-active-cart h2')

    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_sign_in(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN)

    def verify_empty_cart(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)