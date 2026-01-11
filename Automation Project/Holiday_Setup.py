import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")  # Open browser in maximized mode
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://devapp.peopledesk.io/")

# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure wait is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}.")

##.............LogIn Feature................##

# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("peopledeskdemo@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("12345")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()

##.............LogIn Feature................##

#Adminstration
Adminstration = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Administration']")))
Adminstration.click()
time.sleep(5)
print("Adminstration Module Click.")

#Time Management
Time_Management = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Time Management']")))
Time_Management.click()
time.sleep(3)
print("Clicked Successfully on the Time_Management.")

#Holiday Setup
Holiday_Setup = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Holiday Setup']")))
Holiday_Setup.click()
time.sleep(2)
print("Successfully Clicked on the Holiday Setup.")

#Holiday Setup Button Click
Holiday_Group = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Holiday group']")))
Holiday_Group.click()
time.sleep(3)
print("Successfully Clicked on the Holiday Group Button.")

# Locate the "Holiday Group Name" field and send data
holiday_group_name_field = driver.find_element(By.XPATH, "//input[@name='holidayGroup']")
holiday_group_name_field.send_keys("Eid-Ul-Adha")
time.sleep(3)
print("Successfully Entered Holiday Group Name.")

# Locate the "Year" field and send data
year_field = driver.find_element(By.XPATH, "//*[@id='year']/div/div/div/div[1]/div[2]")
year_field.click()
time.sleep(3)
year_field = driver.find_element(By.XPATH, "//div[contains(text(), '2025')]")
year_field.click()
time.sleep(3)
print("Successfully entered the year.")

# Locate and click the "Save & Continue" button
save_continue_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Continue']")
save_continue_button.click()
time.sleep(3)
print("Successfully clicked 'Save & Continue'")

# Locate and fill the "From Date" field
from_date_field = driver.find_element(By.XPATH, "//input[@name='fromDate']")
time.sleep(5)
from_date_field.send_keys("05")
time.sleep(2)
from_date_field.send_keys("June")
# time.sleep(2)
# from_date_field.send_keys("2025")
# from_date_field.send_keys("01-05-2025")
print("Successfully Input From Date.")

# Locate and fill the "To Date" field
to_date_field = driver.find_element(By.XPATH, "//input[@name='toDate']")
time.sleep(2)
to_date_field.send_keys("14")
time.sleep(2)
to_date_field.send_keys("June")
# time.sleep(2)
# to_date_field.send_keys("2025")
# to_date_field.send_keys("05-05-2025")
print("Successfully Input From Date.")

# Locate and fill the "Description" field
description_field = driver.find_element(By.XPATH, "//textarea[@name='description']")  # Adjust XPath if needed
description_field.send_keys("Test")
time.sleep(3)
print("Successfully fill the description.")

# Locate and check the "Depend on moon" checkbox (if needed)
depend_on_moon_checkbox = driver.find_element(By.XPATH, "//input[@name='isConfirm']")  # Adjust XPath if needed
depend_on_moon_checkbox.click()  # Check the box
time.sleep(3)
print("Successfully clicked check-box.")

# Locate and click the "Add" button
add_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")  # Adjust XPath if needed
add_button.click()
time.sleep(8)
print("Successfully clicked Add button.")

# Locate and click to "Return"
return_button = driver.find_element(By.XPATH, "//button[@type='button']//*[name()='svg']")  # Adjust XPath if needed
return_button.click()
time.sleep(2)
print("Successfully clicked to Return.")

# Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")

# Locate the Profile button and click it
profile_xpath = "//span[@class='profile-menu-img']//img[1]"
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
profile_button.click()
print("Clicked on Profile Successfully.")
time.sleep(2)

# Logout from the application
logout_xpath = "(//ul[@class='profile-popup-list']//li)[3]"  # Update with the correct XPath
logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logout_xpath)))
logout_button.click()
print("Logout successfully.")
time.sleep(2)

# Close the browser
driver.quit()
print("WebDriver session End.")