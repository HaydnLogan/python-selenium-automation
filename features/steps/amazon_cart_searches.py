# HW3

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import when, then
import time


@when('Click on Cart from Amazon home')
def click_cart_from_home(context):
    # context.driver.implicitly_wait(5)
    # context.driver.find_element(By.ID, 'nav-cart').click()
    # time.sleep(1)
    context.app.header.click_cart()

@then('Verify Amazon Cart is empty')
def verify_amazon_cart_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row h2').text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"


@then('"{expected_text}" message is displayed')
def verify_empty_cart_msg(context, expected_text):
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    # assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'
    context.app.search_results_page.verify_empty_cart(expected_text)    #lesson 12 HW7 update

@when('Search Danish Butter Cookies')
def search_danish_butter_cookies(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Danish butter cookies', Keys.ENTER)


@when('Click on the second product')
def click_second_product(context):
#   context.driver.find_element(By.CSS_SELECTOR, "div[data-index='2']\[data-component-type='s-search-result']").click()
    context.driver.find_element(By.XPATH, "//div[@data-index='2']").click()

# @when('Search for {search_word}')
# def search_for_product(context, search_word):
#     context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('{search_word}', Keys.ENTER)


@when('Click Amazons Choice')
def click_amazons_choice(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.CSS_SELECTOR, "span[id*='amazons-choice-label']").click()


@when('Add one time to cart')
def add_one_to_cart(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'buyNew_cbb').click()
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify Amazon Cart new item')
def verify_amazon_cart_new_item(context):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    expected_result = '1'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
