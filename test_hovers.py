from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_hovers_simple():
    # Set up the driver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(2)  # Wait for the page to load

        # Find all hoverable elements
        hover_boxes = driver.find_elements(By.CLASS_NAME, "figure")
        print(f"Found {len(hover_boxes)} hover boxes.")

        # Check if the correct number of boxes is present
        if len(hover_boxes) != 3:
            print("Test Failed: Incorrect number of hover boxes.")
            return

        # Hover over each box and check if user info appears
        for i in range(len(hover_boxes)):
            print(f"Hovering over box {i + 1}...")
            action = ActionChains(driver)
            action.move_to_element(hover_boxes[i]).perform()  # Hover over the box
            time.sleep(2)  # Wait to observe the hover effect

            # Verify that the user info is visible
            user_info = hover_boxes[i].find_element(By.CLASS_NAME, "figcaption")
            if user_info.is_displayed():
                print(f"Test Passed: User info for box {i + 1} is visible.")
            else:
                print(f"Test Failed: User info for box {i + 1} is not visible.")
                return

    except Exception as e:
        print(f"Test Failed: An error occurred - {str(e)}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_hovers_simple()
