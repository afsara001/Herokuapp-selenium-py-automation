from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_checkboxes():
    # Set up the driver (Chrome in this case)
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(2)  # Optional delay for visual confirmation

        # Locate all checkboxes on the page
        checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']/input")
        print(f"Total checkboxes found: {len(checkboxes)}")

        # Scenario 1: Verify initial state of checkboxes
        assert not checkboxes[0].is_selected(), "Checkbox 1 should initially be unchecked."
        assert checkboxes[1].is_selected(), "Checkbox 2 should initially be checked."
        print("Test 1 Passed: Initial states verified.")

        # Scenario 2: Toggle checkbox states
        checkboxes[0].click()  # Check the first checkbox
        checkboxes[1].click()  # Uncheck the second checkbox
        time.sleep(1)  # Optional delay for visual confirmation
        assert checkboxes[0].is_selected(), "Checkbox 1 should now be checked."
        assert not checkboxes[1].is_selected(), "Checkbox 2 should now be unchecked."
        print("Test 2 Passed: Checkbox states toggled correctly.")

        # Scenario 3: Ensure states persist after toggling
        assert checkboxes[0].is_selected(), "Checkbox 1 is still checked after toggling."
        assert not checkboxes[1].is_selected(), "Checkbox 2 is still unchecked after toggling."
        print("Test 3 Passed: Final states verified.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_checkboxes()
