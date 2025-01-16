from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_drag_and_drop():
    # Set up the driver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(2)  # Optional delay for visual confirmation

        # Locate the draggable elements
        column_a = driver.find_element(By.ID, "column-a")
        column_b = driver.find_element(By.ID, "column-b")

        # Verify initial positions
        assert column_a.text == "A", "Column A is not in its initial position."
        assert column_b.text == "B", "Column B is not in its initial position."
        print("Test 1 Passed: Initial positions are correct.")

        # Perform drag and drop using JavaScript
        drag_and_drop_script = """
            const dragEvent = new DataTransfer();
            const source = arguments[0];
            const target = arguments[1];

            // Fire drag start event
            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer: dragEvent }));

            // Fire drop event
            target.dispatchEvent(new DragEvent('drop', { dataTransfer: dragEvent }));

            // Fire drag end event
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer: dragEvent }));
        """
        driver.execute_script(drag_and_drop_script, column_a, column_b)
        time.sleep(1)  # Optional delay for visual confirmation

        # Verify final positions
        assert column_a.text == "B", "Column A did not move to the position of Column B."
        assert column_b.text == "A", "Column B did not move to the position of Column A."
        print("Test 2 Passed: Drag and drop action performed successfully.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    except Exception as e:
        print(f"Test Failed: An unexpected error occurred: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_drag_and_drop()
