from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_LINK = (By.ID, 'nav-orders')
    CART_LOGO = (By.ID, 'nav-cart')
    CART = (By.ID, 'nav-cart-count')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.CART_LOGO)

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_department(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')
        # sleep(5)

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

