from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_basic_auth():
    # Set up the driver (Chrome in this case)
    driver = webdriver.Chrome()
    try:
        # Valid credentials
        username = "admin"
        password = "admin"
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        
        # Open the target page with authentication
        driver.get(url)
        time.sleep(2)  # Optional delay for visual confirmation

        # Scenario 1: Verify successful login
        success_message = driver.find_element(By.TAG_NAME, "p").text
        assert "Congratulations!" in success_message, "Failed to log in with valid credentials."
        print("Test 1 Passed: Successful login with valid credentials.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_basic_auth()
