# Lesson 6 HW4

from selenium.webdriver.common.by import By
from behave import given, then


@given('open Best Sellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify {bsl_count} best seller links are displayed')
def verify_bsl(context, bsl_count):
    bsl = context.driver.find_elements(By.CSS_SELECTOR, "a[href*='zg_bs_tab']")
    print(bsl)
    print('\nAmount: ', len(bsl))
    assert len(bsl) == int(bsl_count), f'Expected {bsl_count} boxes, but got {len(bsl)}'
