# HW4

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
#   if len(context.driver.find_elements(By.ID, 'native_dropdown_selected_size_name')) == 1:
        # Click on Size dropdown
#       time.sleep(1)
#       context.driver.find_element(By.ID, 'dropdown_selected_size_name').click()
        # Click on size
#       time.sleep(1)
#       context.driver.find_element(By.ID, 'native_dropdown_selected_size_name_2').click()
#        context.driver.find_element(By.ID, 'a[id*="name_2"]').click()
#       time.sleep(3)
    context.driver.find_elements(By.ID, 'add-to-cart-button')

@then('Verify user can click through colors')
def verify_loop_through_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage',
                       'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash',
                       'Washed Black', 'Bright White', 'Dark Khaki', 'Light Khaki', 'Olive', 'Sage Green']
    color_webelements = context.driver.find_elements(By.CSS_SELECTOR, '#variation_color_name li')

    for i in range(len(color_webelements)):
        color_webelements[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, '#variation_color_name .selection').text
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'