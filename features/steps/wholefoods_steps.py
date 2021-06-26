from selenium.webdriver.common.by import By
from behave import given, then

# HW5 question 3 solution
# Verify that every product on the Wholefoods page has a text ‘Regular’ and a product name

BEST_DEALS_ITEMS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class, 'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")


@given ('Open Amazon Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that Wholefoods products have regular prices and names')
def verify_best_deals(context):
    best_deals_items= context.driver.find_elements(*BEST_DEALS_ITEMS)
    #Go thru every web element
    for e in best_deals_items:
        # Verify Regular
        assert 'Regular' in e.text, f'Expected Regular price not found in {e.text}'
        # Verify name
        product_name = e.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, 'Product name is missing'

# element = driver.find_element(By.ID, '')
# element.find_element(By.ID, '')
