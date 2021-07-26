# Lesson 6

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.ENTER)

@when('Move mouse over flag icon')
def hover_flag_icon(context):
    context.app.header.hover_flag_icon()

@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    items_in_cart = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert items_in_cart == int(expected_count), f'Expected {expected_count}, but got {items_in_cart}'


@when('Click Sign In from popup')
def click_sign_in_btn(context):
 #  context.driver.find_element(By.ID, 'nav-orders').click()
    e = context.driver.wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))
    e.click()


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    context.driver.find_element(By.ID, 'nav-hamburger-menu')
#   print('USING find element')
#   element = context.driver.find_element(By.ID, 'n2av-hamburger-menu')
#   print(element)

#   print('USING find elementSSS')
#   elements = context.driver.find_elements(By.ID, '22n2av-hamburger-menu')
#   print(elements)


@then('Verify Sign in popup is clickable')
def verify_signin_popup_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))


@when('Wait for {sec_count} sec')
def sleep_sec(context, sec_count):
    sleep(int(sec_count))


@then('Verify Sign in popup disappears')
def verify_signin_popup__disappears(context):
#   context.driver.wait.until(EC.invisibility_of_element((
#       By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))
#   context.driver.wait.until_not(condition == False)
    context.driver.wait.until_not(EC.visibility_of_element_located((
        By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')))

@then('Spanish language selection is visible')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()