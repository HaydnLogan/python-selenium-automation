from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# HW 6, Task 1
# Create a window handling test case from the class
#    and verify that user can open amazon applications from Terms of Conditions

PNfromTC = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
PnLine = (By.XPATH, "//h1[text()='Amazon.com Privacy Notice']")


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/'
                       'display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_from_tc(context):
    context.driver.find_element(*PNfromTC).click()


@then('Verify Amazon Privacy Notice page is opened')
def verify_new_PN_page(context):
    actual_text = context.driver.find_element(*PnLine).text
    expected_text = 'Amazon.com Privacy Notice'
    print(actual_text)
    assert actual_text == expected_text, f'Got {actual_text}, but expected {expected_text}'
