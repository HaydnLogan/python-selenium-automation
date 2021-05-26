from selenium.webdriver.common.by import By
from behave import given, when, then

#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://amazon.com/')

@when('Click Orders')
def search_amazon(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'orders')]").click()

@then('Verify signin shown')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    expected_result = 'Sign-In'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"