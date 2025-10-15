
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    driver = webdriver.Chrome()
    print("Browser opened successfully.")

    # Open Google
    driver.get("https://www.google.com")
    print("Navigated to Google.")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")
    print("Found search box.")

    # Type in the search query
    search_box.send_keys("youtube")

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(15)

    print("Search successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
