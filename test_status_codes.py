from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_status_codes():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/status_codes")
        time.sleep(2)  # Optional: Wait for the page to load

        # Locate all status code links
        status_code_links = driver.find_elements(By.CSS_SELECTOR, "ul li a")
        expected_status_codes = ["200", "301", "404", "500"]

        # Verify the correct number of status code links
        if len(status_code_links) != len(expected_status_codes):
            print(f"Test Failed: Expected {len(expected_status_codes)} links, but found {len(status_code_links)}.")
            return
        print("Test Passed: All status code links are present.")

        # Iterate through each link
        for i, link in enumerate(status_code_links):
            status_code = expected_status_codes[i]
            print(f"Clicking on status code {status_code}...")

            # Click the link
            link.click()
            time.sleep(2)  # Wait for the new page to load

            # Verify the status code in the response message
            response_message = driver.find_element(By.TAG_NAME, "p").text
            if status_code in response_message:
                print(f"Test Passed: Status code {status_code} is displayed correctly.")
            else:
                print(f"Test Failed: Status code {status_code} is not displayed correctly.")
                return

            # Navigate back to the main page
            driver.back()
            time.sleep(2)  # Wait for the main page to load again

    except Exception as e:
        print(f"Test Failed: An error occurred - {str(e)}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_status_codes()
