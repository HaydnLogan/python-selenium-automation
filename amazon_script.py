from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

# open the url
driver.get('https://www.amazon.com/')

search_field = driver.find_element(By.ID, 'twotabsearchtextbox') # create variable
search_field.clear()
search_field.send_keys('Table')

search_icon = driver.find_element(By.ID, 'nav-search-submit-button')
search_icon.click()
# driver.find_element(By.ID, 'nav-search-submit-button').click() also works without variable

# verify
actual_result = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
print(f'Actual result: {actual_result}')

expected_result = '"Table..."'

assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"

driver.quit()
#assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#print('Test Passed')
