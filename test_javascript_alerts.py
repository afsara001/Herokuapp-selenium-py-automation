from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_javascript_alerts_slowly():
    # Set up the driver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)  # Wait to observe the page load

        # Locate the buttons
        js_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        js_confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        js_prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        result_text = driver.find_element(By.ID, "result")

        # Scenario 1: Verify button presence
        assert js_alert_button.is_displayed(), "JS Alert button is not visible."
        assert js_confirm_button.is_displayed(), "JS Confirm button is not visible."
        assert js_prompt_button.is_displayed(), "JS Prompt button is not visible."
        print("Test 1 Passed: All buttons are visible.")
        time.sleep(2)  # Pause to observe

        # Scenario 2: Handle JS Alert
        print("Clicking JS Alert button...")
        js_alert_button.click()
        time.sleep(2)  # Wait for the alert to appear
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()
        time.sleep(2)  # Wait to observe the result
        assert "You successfully clicked an alert" in result_text.text, "Unexpected result message after JS Alert."
        print("Test 2 Passed: JS Alert handled successfully.")
        time.sleep(2)  # Pause to observe

        # Scenario 3: Handle JS Confirm
        # Accept the alert
        print("Clicking JS Confirm button and accepting...")
        js_confirm_button.click()
        time.sleep(2)  # Wait for the alert to appear
        alert = driver.switch_to.alert
        print(f"Confirm text: {alert.text}")
        alert.accept()
        time.sleep(2)  # Wait to observe the result
        assert "You clicked: Ok" in result_text.text, "Unexpected result message after accepting JS Confirm."
        print("Test 3.1 Passed: JS Confirm accepted successfully.")
        time.sleep(2)  # Pause to observe

        # Dismiss the alert
        print("Clicking JS Confirm button and dismissing...")
        js_confirm_button.click()
        time.sleep(2)  # Wait for the alert to appear
        alert = driver.switch_to.alert
        alert.dismiss()
        time.sleep(2)  # Wait to observe the result
        assert "You clicked: Cancel" in result_text.text, "Unexpected result message after dismissing JS Confirm."
        print("Test 3.2 Passed: JS Confirm dismissed successfully.")
        time.sleep(2)  # Pause to observe

        # Scenario 4: Handle JS Prompt
        # Accept the prompt with input
        print("Clicking JS Prompt button and entering text...")
        js_prompt_button.click()
        time.sleep(2)  # Wait for the prompt to appear
        alert = driver.switch_to.alert
        alert.send_keys("Test Input")
        time.sleep(2)  # Observe the input process
        alert.accept()
        time.sleep(2)  # Wait to observe the result
        assert "You entered: Test Input" in result_text.text, "Unexpected result message after entering text in JS Prompt."
        print("Test 4.1 Passed: JS Prompt accepted with input successfully.")
        time.sleep(2)  # Pause to observe

        # Dismiss the prompt
        print("Clicking JS Prompt button and dismissing...")
        js_prompt_button.click()
        time.sleep(2)  # Wait for the prompt to appear
        alert = driver.switch_to.alert
        alert.dismiss()
        time.sleep(2)  # Wait to observe the result
        assert "You entered: null" in result_text.text, "Unexpected result message after dismissing JS Prompt."
        print("Test 4.2 Passed: JS Prompt dismissed successfully.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    except Exception as e:
        print(f"Test Failed: An unexpected error occurred: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_javascript_alerts_slowly()
