from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_context_menu():
    # Set up the driver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/context_menu")
        time.sleep(2)  # Optional delay for visual confirmation

        # Locate the context menu box
        context_box = driver.find_element(By.ID, "hot-spot")

        # Verify the context menu box is displayed
        if not context_box.is_displayed():
            print("Test Failed: Context menu box is not displayed.")
            return
        print("Test 1 Passed: Context menu box is present.")

        # Perform a right-click on the context menu box
        actions = ActionChains(driver)
        actions.context_click(context_box).perform()
        time.sleep(1)  # Optional delay for alert visibility

        # Handle the alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        if alert_text == "You selected a context menu":
            print("Test 2 Passed: Alert triggered with correct message.")
        else:
            print(f"Test Failed: Unexpected alert text: {alert_text}")

        # Dismiss the alert
        alert.accept()
        print("Test 3 Passed: Alert dismissed successfully.")

    except Exception as e:
        print(f"Test Failed: An error occurred: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_context_menu()
