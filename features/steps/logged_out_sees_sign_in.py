# HW2 May 23, 2021
# HW7 Lesson 7 Update

from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Orders')
def search_amazon(context):
#   context.driver.find_element(By.XPATH, "//a[contains(@href, 'orders')]").click()
#     orders_link = context.driver.find_element(By.ID, 'nav-orders')
#     print(orders_link)
#     context.driver.refresh()
#     # grab link again to avoid stale element errors
#     orders_link = context.driver.find_element(By.ID, 'nav-orders')
#     print(orders_link)
#     orders_link.click()
    context.app.header.click_orders()   # Lesson 12 update, HW7


@then('Verify {expected_text} shown')
def verify_search_worked(context, expected_text):
    # actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    # expected_result = 'Sign-In'
    # assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
    context.app.search_results_page.verify_sign_in(expected_text)