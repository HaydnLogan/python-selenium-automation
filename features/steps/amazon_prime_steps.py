# Lesson 6

from selenium.webdriver.common.by import By
from behave import given, then


@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {box_count} benefit boxes are displayed')
def verify_benefit_boxes(context, box_count):
    print(type(box_count))
    boxes = context.driver.find_elements(By.CSS_SELECTOR, 'div.benefit-box')
    print(boxes)
    print('\nAmount: ', len(boxes))
    print(type(len(boxes)))
#   assert len(boxes) == box_count, f'Expected 8 boxes, but got {len(boxes)}'
    #   #integer compared with string will likely fail
    assert len(boxes) == int(box_count), f'Expected {box_count} boxes, but got {len(boxes)}'
