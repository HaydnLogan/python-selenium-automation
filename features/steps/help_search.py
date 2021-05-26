from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time

@given('Open Amazon Help page')
def open_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search Library')
def search_library(context):
    context.driver.find_element(By.XPATH, "//input[@name='help_keywords']").send_keys('Cancel Order')
    time.sleep(1)

@when('Emulate Enter')
def type_enter(context):
    context.driver.find_element(By.XPATH, "//input[@name='help_keywords']").send_keys(Keys.RETURN)

@then('Verify Cancel')
def verify_cancel(context):
#    actual_result = context.driver.find_element(By.XPATH,"//div[@class='help-content']").text
    actual_result = context.driver.find_element(By.XPATH, "//div/p/b[@id='search-help']").text
    expected_result = '"Cancel Items or Orders"'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
driver.find_element(By.CSS_SELECTOR)
