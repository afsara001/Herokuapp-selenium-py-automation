from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    # Set up the driver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)  # Optional delay for visual confirmation

        # Scenario 1: Verify login page presence
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

        assert username_field.is_displayed(), "Username field is not visible."
        assert password_field.is_displayed(), "Password field is not visible."
        assert login_button.is_displayed(), "Login button is not visible."
        print("Test 1 Passed: Login page elements are visible.")

        # Scenario 2: Successful login
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()
        time.sleep(2)  # Wait for login to complete

        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        logout_button = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")

        assert success_message.is_displayed(), "Success message is not visible."
        assert "You logged into a secure area!" in success_message.text, "Unexpected success message."
        assert logout_button.is_displayed(), "Logout button is not visible after login."
        print("Test 2 Passed: Successfully logged in with valid credentials.")

        # Logout for the next test
        logout_button.click()
        time.sleep(2)  # Wait for logout to complete

        # Scenario 3: Unsuccessful login (Invalid credentials)
        username_field = driver.find_element(By.ID, "username")  # Re-locate elements after page reload
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

        username_field.send_keys("invalid_user")
        password_field.send_keys("invalid_password")
        login_button.click()
        time.sleep(2)  # Wait for the error message to appear

        error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
        assert error_message.is_displayed(), "Error message is not visible."
        assert "Your username is invalid!" in error_message.text, "Unexpected error message."
        print("Test 3 Passed: Proper error message displayed for invalid credentials.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    except Exception as e:
        print(f"Test Failed: An unexpected error occurred: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_login()
