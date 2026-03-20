from selenium import webdriver
import time  # Import the time module for adding delays
from selenium.webdriver.common.by import By  # Import the By class for locating elements on the page
# Instantiate the web driver for Chrome
driver = webdriver.Chrome()

# Navigate to the Masterschool website
driver.get("https://www.saucedemo.com")

# Wait for 3 seconds to allow the page to load completely
time.sleep(3)

element = driver.find_element(By.ID, "user-name")
time.sleep(5)
print(element)
element.send_keys("standard_user")
time.sleep(3)
element = driver.find_element(By.ID, "password")
element.send_keys("secret_sauce")
time.sleep(5)
element = driver.find_element(By.ID, "login-button")
element.click()
time.sleep(5)
assert driver.find_element(By.CLASS_NAME, "inventory_details_name").text == "Sauce Labs Backpack"

# Close the browser and end the WebDriver session
driver.quit()


