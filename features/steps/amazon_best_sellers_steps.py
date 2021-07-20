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

"""  HW6 Task 2
This test will find the 1st element if I leave it as 'Best Sellers' and show the error message link is 
Amazaon Best Sellers by expected Best Sellers.   When I change the expected text to Amazon Best Sellers, then the test
doesn't work, it gives the stale element reference.  
I tried to slow it down with hard sleep, I tried to refresh... i haven't figured it out yet.  
"""

@when('Click on Best Sellers')
def click_BestSellers_from_home(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']").click()

TOP_LINKS = (By.CSS_SELECTOR, 'zg_tabs a')
HEADER = (By.CSS_SELECTOR, 'zg_banner_text_wrapper')

@then('Verify user can click through top 5')  # HW6 Task 2
def verify_loop_through_top5(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'
    #
    # expected_links = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers', 'Amazon Most Wished For', 'Amazon Gift Ideas']
    # top5_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#zg_tabs li")
    #
    # for i in range(len(top5_webelements)):
    #     top5_webelements[i].click()
    #     actual_text = context.driver.find_element(By.ID, 'zg_banner_text_wrapper').text
    #     print(actual_text)
    #     assert actual_text == expected_links[i], f'Error, link is {actual_text}, but expected {expected_links[i]}'
#       context.driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']").click()