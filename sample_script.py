from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# Implicit wait
# Checks 100 ms for web element (1/10 sec)
# only works with find_element commands
driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')


search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# Explicit Wait
# Checks 500 ms for condition (0.5 sec)
driver.wait = WebDriverWait(driver, 15)
e = driver.wait.until(EC.elemenet_to_be_clickable((By.NAME, 'btnk')), message='Error, search button not clickable')
# EC = Expected Condtions library

# click search
# driver.find_element(By.NAME, 'btnK').click()
e.click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
