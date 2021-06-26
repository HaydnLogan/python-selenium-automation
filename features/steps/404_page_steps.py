from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#  Lesson 10 classwork


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on the dog image')
def click_dog_img(context):
    context.driver.find_element(By.CSS_SELECTOR, 'img#d').click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Blog url')
def verify_blog_url(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url, \
        f'Url https://www.aboutamazon.com/ not in {context.driver.current_url}'


@then('Close new window')
def close_window(context):
    context.driver.close()


@when('Return to original window')
def switch_to_orig_window(context):
    context.driver.switch_to.window(context.original_window)


@then('Verify Amazon url')
def verify_base_url(context):
    assert 'https://www.amazon.com/' in context.driver.current_url, \
        f'Url https://www.amazon.com/ not in {context.driver.current_url}'