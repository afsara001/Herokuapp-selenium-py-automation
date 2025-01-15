from selenium import webdriver
from selenium.webdriver.common.by import By
#import requests

def test_broken_images():
    # Set up the driver (Chrome in this case)
    driver = webdriver.Chrome()
    try:
        # Open the target page
        driver.get("https://the-internet.herokuapp.com/broken_images")

        # Locate all image elements on the page
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Total images found: {len(images)}")

        # Check each image's status
        broken_images = 0
        for image in images:
            image_url = image.get_attribute("src")
            try:
                response = requests.get(image_url)
                if response.status_code != 200:
                    print(f"Broken Image: {image_url} (Status Code: {response.status_code})")
                    broken_images += 1
            except Exception as e:
                print(f"Error checking image {image_url}: {str(e)}")
                broken_images += 1

        # Assert no broken images
        assert broken_images == 0, f"Test Failed: {broken_images} broken images found."
        print("Test Passed: All images loaded successfully.")

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_broken_images()
