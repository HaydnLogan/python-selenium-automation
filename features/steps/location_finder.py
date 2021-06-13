# HW2 May 23, 2021
# HW3 add on


from selenium.webdriver.common.by import By
from behave import when, then
import time


# @given('Open Amazon page')
# def open_amazon(context):
#    context.driver.get('https://amazon.com/')


@when('Navigate to sign in page')
def sign_in(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'nav-link-accountList').click()


@when('Navigate to register page')
def sign_in(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'nav-link-accountList').click()
#    context.driver.find_element(By.CSS_SELECTOR, '#nav-flyout-ya-newCust').click()
#    context.driver.find_element(By.CSS_SELECTOR, "#nav-flyout-ya-newCust a[href*='register']").click()
    #    ## How can I click on the link inside a flyout nav area?
    context.driver.find_element(By.ID, 'createAccountSubmit').click()
#    time.sleep(2)


@when('Click on Amazon logo')
def click_logo(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.CSS_SELECTOR, '.a-icon-logo').click()
#    context.driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']").click() #old way


@when('Verify Create Account text')
def verify_create_text(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    expected_result = 'Create account'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"


@when('Go back')
def go_back(context):
    context.driver.implicitly_wait(5)
    context.driver.back()


@when('Wait and See')
def wait_and_see(context):
    time.sleep(3)


@when('Enter Name')
def enter_name(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'ap_customer_name').send_keys('Test Name')


@when('Click on email field')
def click_email(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'ap_email').send_keys('test email@')
#    context.driver.find_element(By.XPATH, "//input[@type='email']").send_keys('test name') # old way
# time.sleep(3)


@when('Enter Password')
def enter_password(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'ap_password').send_keys('Test Pass Word')


@when('ReEnter Password')
def re_enter_password(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'ap_password_check').send_keys('Test Pass Word 222')


@when('Verify Password text')
def verify_password_text(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-alert-inline-info .a-alert-content').text
    expected_result = 'Passwords must be at least 6 characters.'
    assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"


@when('Click on continue')
def click_continue(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()


@when('Click help')
def click_help(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
    time.sleep(1)


@when('Click forget')
def click_forget(context):
    context.driver.find_element(By.ID, 'auth-fpp-link-bottom').click()


@when('Click other')
def click_other(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
    context.driver.find_element(By.ID, 'ap-other-signin-issues-link').click()


@when('Click create')
def click_create(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']").click()


@when('Click create on Registry')
def click_create_from_registry(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'continue').click()


@when('Click conditions')
def click_conditions(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.CSS_SELECTOR, 'a[href*="condition"]').click()
#   context.driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'condition')]").click()
#                                              old way


@when('Click privacy')
def click_privacy(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href*="privacy"]').click()
#   context.driver.find_element(By.XPATH, "//a[contains(@href, 'privacy')]").click()  # Old way


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href*="signin"]').click()


@then('close page')
def close_page(context):
    context.driver.close()
