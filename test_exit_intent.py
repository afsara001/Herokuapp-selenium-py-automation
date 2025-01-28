from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_exit_intent():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/exit_intent")
        time.sleep(2)  # Optional: Wait for the page to load

        # Trigger the exit intent by moving the mouse outside the viewport
        print("Moving the mouse to trigger the exit intent...")
        action = ActionChains(driver)
        action.move_by_offset(-1000, 0).perform()  # Move the mouse to the left of the viewport
        time.sleep(2)  # Wait to see if the popup appears

        # Check if the modal popup is displayed
        modal = driver.find_element(By.ID, "ouibounce-modal")
        if modal.is_displayed():
            print("Test Passed: Exit intent popup is displayed.")
            
            # Close the popup
            close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer > p")
            close_button.click()
            print("Popup closed successfully.")
        else:
            print("Test Failed: Exit intent popup is not displayed.")

    except Exception as e:
        print(f"Test Failed: An error occurred - {str(e)}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_exit_intent()
