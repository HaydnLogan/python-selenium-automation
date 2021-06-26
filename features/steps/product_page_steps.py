# HW4

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

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
    color_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(color_webelements)):
        color_webelements[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name .selection").text
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'

@when('Click on Best Sellers')
def click_BestSellers_from_home(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']").click()


@then('Verify user can click through top 5')  #HW6 Task 2
def verify_loop_through_top5(context):
    expected_links = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers', 'Amazon Most Wished For', 'Amazon Gift Ideas']
    top5_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#zg_tabs li")

    for i in range(len(top5_webelements)):
        top5_webelements[i].click()
        actual_text = context.driver.find_element(By.ID, 'zg_banner_text_wrapper').text
        print(actual_text)
        assert actual_text == expected_links[i], f'Error, link is {actual_text}, but expected {expected_links[i]}'
#       context.driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']").click()

"""  HW6 Task 2
This test will find the 1st element if I leave it as 'Best Sellers' and show the error message link is 
Amazaon Best Sellers by expected Best Sellers.   When I change the expected text to Amazon Best Sellers, then the test
doesn't work, it gives the stale element reference.  
I tried to slow it down with hard sleep, I tried to refresh... i haven't figured it out yet.  
"""
