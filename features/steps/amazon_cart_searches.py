# HW3

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time

@when('Click on Cart from Amazon home')
def click_cart_from_home(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'nav-cart').click()
    time.sleep(1)

@then('Verify Amazon Cart is empty')
def verify_amazon_cart_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row h2').text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"

@when('Search for Danish Butter Cookies')
def search_Danish_Butter_Cookies(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Danish butter cookies', Keys.ENTER)

@when('Click Amazons Choice')
def click_Amazons_Choice(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.CSS_SELECTOR, "span[id*='amazons-choice-label']").click()

@when('Add one time to cart')
def add_one_to_cart(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'buyNew_cbb').click()
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@Then('Verify Amazon Cart new item')
def verify_amazon_cart_new_item(context):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    expected_result = '1'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
