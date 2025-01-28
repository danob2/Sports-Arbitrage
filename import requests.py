from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the target website
driver.get("https://www.nike.sk/tipovanie")

# Accept cookies
try:
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
    )
    accept_button.click()
    print("Accepted cookies.")
except Exception as e:
    print("No cookie banner found or clickable:", e)

# Locate the parent div and extract odds
try:
    # Find all parent divs with the class 'bet-table-left ellipsis'
    parent_divs = driver.find_elements(By.CLASS_NAME, "flex.flex-1")

    for i, parent_div in enumerate(parent_divs):

        try:
        # Extract event details (team names or event name)
            event_div = parent_div.find_element(By.CLASS_NAME, "bet-table-left.ellipsis")
            event_details = parent_div.get_attribute("data-participants")  # Adjust based on actual structure
            print(f"Event {i + 1}: {event_details}")

        # Extract odds
            odds_links = parent_div.find_elements(By.TAG_NAME, "a")
            for j, link in enumerate(odds_links):
                odd_value = link.text if link.text else link.find_element(By.TAG_NAME, "span").text
                print(f"  Odd {j + 1}: {odd_value}")
        except Exception as e:
            print(f"Event {i + 1}: Error extracting details - {e}")
        
except Exception as e:
    print("An error occurred while extracting odds:", e)

# Close the browser
driver.quit()




