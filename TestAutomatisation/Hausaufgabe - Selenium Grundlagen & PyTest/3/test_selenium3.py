from selenium import webdriver  # Import the Selenium WebDriver
import time  # Import the time module for adding delays
from selenium.webdriver.common.by import By  # Import the By class for locating elements on the page
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest  # Import the pytest framework for writing test cases

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_automation_exercise_registration(driver):
    wait = WebDriverWait(driver, 10)

    # 1,2.start browser find url
    driver.get("https://automationexercise.com/")


    consent = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent")))
    consent.click()
    # 3. validate, side be seen
    assert "Automation Exercise" in driver.title
    print("Title is correct")

    # 4.click Signup / Login
    driver.find_element(By.CSS_SELECTOR,  "a[href='/login']").click()

    # 5.Check:"New User Signup" is seen"
    sign_up_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
    assert sign_up_header.is_displayed(), "New User Signup! header is not visible"

    # 6,7. fill in name and click "Signup"
    driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-name']").send_keys("TestUser12327")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys("testuser12327@example.com")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']").click()

    # 8. check, "ENTER ACCOUNT INFORMATION" is been seen
    account_info_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Enter Account Information')]")))
    assert account_info_header.is_displayed(), "Enter Account Information header is not visible"

    # 9. fill in all details and click "Create Account"
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("SicheresPasswort123")

        # birthdate
    Select(driver.find_element(By.ID, "days")).select_by_visible_text("10")
    Select(driver.find_element(By.ID, "months")).select_by_visible_text("May")
    Select(driver.find_element(By.ID, "years")).select_by_visible_text("1990")


    # 10,11. Newsletter, checkboxes
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    # 12. fill in more details
    driver.find_element(By.ID, "first_name").send_keys("Max")
    driver.find_element(By.ID, "last_name").send_keys("Mustermann")
    driver.find_element(By.ID, "company").send_keys("TestfirmaGmbH")  
    driver.find_element(By.ID, "address1").send_keys("Testweg123")
    driver.find_element(By.ID, "address2").send_keys("Testweg982")
    driver.find_element(By.ID, "country").send_keys("Testland")
    driver.find_element(By.ID, "state").send_keys("Testbundesland")
    driver.find_element(By.ID, "city").send_keys("Teststadt")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("+491234567890")

    # 13. create account
    driver.find_element(By.CSS_SELECTOR, "[data-qa='create-account']").click()

    # 14. check, "ACCOUNT CREATED!" is been seen
    account_created_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'ACCOUNT CREATED!')]")))
    assert account_created_header.is_displayed(), "Account Created! header is not visible"

    # 15. click "Continue"
    driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']").click()

    # 16. check, "Logged in as username" is been seen
    logged_in_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]")))
    assert logged_in_header.is_displayed(), "Logged in as username header is not visible"

    # 17. click "Delete Account"
    driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']").click()

    # 18. check, "ACCOUNT DELETED!" is been seen
    account_deleted_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Account Deleted!')]")))
    assert account_deleted_header.is_displayed(), "Account Deleted! header is not visible"
    