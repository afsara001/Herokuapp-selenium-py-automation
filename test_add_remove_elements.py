from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_remove_elements():
    # Set up the driver (Chrome in this case)
    driver = webdriver.Chrome()
    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        
        # Scenario 1: Verify adding an element
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        add_button.click()
        time.sleep(1)  # Adding a delay to visually confirm (optional)
        added_elements = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(added_elements) == 1, "Failed to add the element."

        print("Test 1 Passed: Adding an element works correctly.")

        # Scenario 2: Verify removing an element
        delete_button = added_elements[0]
        delete_button.click()
        time.sleep(1)  # Adding a delay to visually confirm (optional)
        added_elements_after_delete = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(added_elements_after_delete) == 0, "Failed to remove the element."

        print("Test 2 Passed: Removing an element works correctly.")

        # Scenario 3: Add and remove multiple elements
        for _ in range(5):
            add_button.click()
        time.sleep(1)  # Adding a delay to visually confirm (optional)
        added_elements = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(added_elements) == 5, "Failed to add multiple elements."

        for element in added_elements:
            element.click()
            time.sleep(0.5)  # Optional delay for visual confirmation

        added_elements_after_removing_all = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(added_elements_after_removing_all) == 0, "Failed to remove all elements."

        print("Test 3 Passed: Adding and removing multiple elements works correctly.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_add_remove_elements()
