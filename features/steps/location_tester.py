from selenium.webdriver.common.by import By
from behave import given, when, then
import time

#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://amazon.com/')

@when('Navigate to sign in page')
def sign_in(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, 'nav-link-accountList').click()
    time.sleep(2)

@when('Click on Amazon logo')
def click_logo(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']").click()

@when('Go back')
def go_back(context):
    context.driver.implicitly_wait(5)
    context.driver.back()

@when('Click on email field')
def click_email(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//input[@type='email']").send_keys('test name')

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

@when('Click conditions')
def click_conditions(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'condition')]").click()

@when('Click privacy')
def click_privacy(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'privacy')]").click()

@then('close page')
def close_page(context):
    context.driver.close()


