# Lesson 6

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import when, then


@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.ENTER)


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    items_in_cart = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert items_in_cart == int(expected_count), f'Expected {expected_count}, but got {items_in_cart}'


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    context.driver.find_element(By.ID, 'nav-hamburger-menu')
#   print('USING find element')
#   element = context.driver.find_element(By.ID, 'n2av-hamburger-menu')
#   print(element)

#   print('USING find elementSSS')
#   elements = context.driver.find_elements(By.ID, '22n2av-hamburger-menu')
#   print(elements)
