# HW2 May 23, 2021

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://amazon.com/')
    context.app.main_page.open_main()


@when('Input {search_word} in search field')
def search_amazon(context, search_word):
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')
    context.app.header.input_search(search_word)



@when('Click on Amazon search icon')
def click_search(context):
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.click_search()


@then('Verify search worked for {expected_text}')
def verify_search_worked(context, expected_text):
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # expected_result = '"Table"'
    # assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
    context.app.search_results_page.verify_search_worked(expected_text)
