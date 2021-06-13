# HW2 May 23, 2021
# HW3 Task 2 of 4

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time


@given('Open Amazon Help page')
def open_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search Library')
def search_library(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')
#   context.driver.find_element(By.XPATH, "//input[@name='help_keywords']").send_keys('Cancel Order')  # old way
    time.sleep(1)


@when('Emulate Enter')
def type_enter(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)
#   context.driver.find_element(By.XPATH, "//input[@name='help_keywords']").send_keys(Keys.RETURN)   # old way


@then('Verify Cancel')
def verify_cancel(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.help-content h1').text
#   actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text  # old way
    expected_result = 'Cancel Items or Orders'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
