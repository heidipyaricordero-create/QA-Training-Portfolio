import pytest
from selenium import webdriver
import time  # Import the time module for adding delays
from selenium.webdriver.common.by import By  # Import the By class for locating elements on the page

#  driver fixture for 
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

 @pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user"
    "error_user"
    "visual_user""
     
 ])

def test_saucedemo_login(driver, username):
# Navigate to the Masterschool website
driver.get("https://www.saucedemo.com")
# Wait for 3 seconds to allow the page to load completely
time.sleep(3)

# login data
driver.find_element(By.ID, "user-name").send_keys(username)
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)


#login check
if username == "locked_out_user":
    # check the error message 
    error_text = driver.find_element(By.CSS_SELECTOR, [Data-test='error`]").text
    assert "locked-out" in error error_text
    print(f"Check {username} wurde korrekt blockiert.")")
else:  
# check successfull login                                                
    assert "Swag Labs" in driver.title
    assert "inventory.html" in driver.current_url
    
    # find the product name element by its class name
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_name == "Sauce Labs Backpack"
    print(f"Ceck: {username} eingeloggt, Produkt '{product_name}' gefunden.") 
    time.sleep(3)
# Close the browser and end the WebDriver session
driver.quit()




