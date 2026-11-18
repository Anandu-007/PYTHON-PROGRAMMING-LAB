from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

driver.maximize_window()

# Enter full name
driver.find_element(By.ID, "userName").send_keys("John")

# Enter email
driver.find_element(By.ID, "userEmail").send_keys("john@gmail.com")

# Enter current address
driver.find_element(By.ID, "currentAddress").send_keys("Kerala")

# Enter permanent address
driver.find_element(By.ID, "permanentAddress").send_keys("India")

# Click submit button
driver.find_element(By.ID, "submit").click()

time.sleep(2)

# Verify output
result = driver.find_element(By.ID, "output")

print(result.text)

driver.quit()