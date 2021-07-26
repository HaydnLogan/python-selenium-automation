from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, 'variation_color_name li')
    SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BTN)
        self.click(*self.SIZE_OPTION_0)
        self.wait_for_element_appear(*self.PRICE_BUY_BOX)
