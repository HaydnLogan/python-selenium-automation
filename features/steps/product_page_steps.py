# HW4

from selenium.webdriver.common.by import By
from behave import when, then
import time


@when('Click on Add to cart button')
def click_add_to_cart(context):
    if len(context.driver.find_elements(By.ID, 'native_dropdown_selected_size_name')) == 1:
        # Click on Size dropdown
        time.sleep(1)
        context.driver.find_element(By.ID, 'dropdown_selected_size_name').click()
        # Click on size
        time.sleep(1)
        context.driver.find_element(By.ID, 'native_dropdown_selected_size_name_2').click()
#        context.driver.find_element(By.ID, 'a[id*="name_2"]').click()
        time.sleep(3)
    context.driver.find_elements(By.ID, 'add-to-cart-button')
