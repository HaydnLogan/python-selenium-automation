from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-types='s-search-r]")
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '#sc-active-cart h2')
    BOOKS_SUBNAV = (By.CSS_SELECTOR, '#nav-subnav[data-category="books"]')
    APPLIANCES_SUBNAV = (By.CSS_SELECTOR, '#nav-subnav[data-category="appliances"]')

    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_sign_in(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN)

    def verify_empty_cart(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)

    def verify_books_department(self):
        self.wait_for_element_appear(*self.BOOKS_SUBNAV)

    def verify_appliances_department(self):
        self.wait_for_element_appear(*self.APPLIANCES_SUBNAV)