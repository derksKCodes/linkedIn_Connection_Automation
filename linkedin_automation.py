from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from getpass import getpass
import time

# Setup undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)


# --- Setup WebDriver ---
driver = uc.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(5)  # wait for page to load

# --- Ask for Login Credentials ---
email = input("Enter your LinkedIn email: ")
password = getpass("Enter your LinkedIn password (input hidden): ")


# --- Log In ---
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)

# Click the login button
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(5)  # wait for login

# --- Check if login failed ---
try:
    error_box = driver.find_element(By.CLASS_NAME, "alert")
    print("❌ Login failed: Incorrect email or password.")
    driver.quit()
    exit()
except NoSuchElementException:
    print("✅ Login successful!")

# --- Navigate to Network Page ---
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)

# --- Find Connect Buttons ---
connect_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "Connect")]')

for btn in connect_buttons:
    try:
        btn.click()
        time.sleep(2)

        # Check if a "Add a note" popup appears
        try:
            add_note_btn = driver.find_element(By.XPATH, '//button/span[text()="Add a note"]')
            add_note_btn.click()
            time.sleep(1)

            # Type your note here
            note_box = driver.find_element(By.ID, 'custom-message')
            note_box.send_keys("Hi, I'd love to connect with you!")

            # Click Send
            driver.find_element(By.XPATH, '//button/span[text()="Send"]').click()
            print("Connection sent with note.")
        except NoSuchElementException:
            # If there's just a Send button, click it
            try:
                driver.find_element(By.XPATH, '//button/span[text()="Send"]').click()
                print("Connection sent without note.")
            except NoSuchElementException:
                print("Send button not found.")

    except ElementClickInterceptedException:
        print("Skipped one due to popup or overlay.")
        continue

    time.sleep(2)

# --- Finish ---
print("Done sending requests.")
driver.quit()
