from selenium import webdriver  # Import the Selenium WebDriver
import time  # Import the time module for adding delays
from selenium.webdriver.common.by import By  # Import the By class for locating elements on the page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setup webdriver
driver = webdriver.Chrome()
# Navigate to https://automationexercise.com
driver.get("https://automationexercise.com")
wait = WebDriverWait(driver, 10)
# Verify that home page is visible successfully
home_page = wait.until(EC.visibility_of_element_located((By.ID,"slider-carousel")))
home_page.is_displayed()
assert home_page.is_displayed(), "Home page is not visible"
consent = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent")))
consent.click()
sign_up = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
sign_up.click()
all_h2 = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "h2")))
print(all_h2[0].text)
all_h2[1].is_displayed()
assert all_h2[1].is_displayed(), "New Sign  Up is not visible"


