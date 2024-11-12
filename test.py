from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Verify the page title contains "Google"
    assert "Google" in driver.title
    print("Google page title verified!")

    # Find the search bar element by name and perform a search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(2)

    # Check that the results contain expected text
    results = driver.find_elements(By.XPATH, "//h3")
    if results:
        print("Search results are displayed!")
        print(f"First result title: {results[0].text}")
    else:
        print("No search results found.")

finally:
    # Close the browser
    driver.quit()
