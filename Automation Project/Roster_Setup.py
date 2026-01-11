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
time.sleep(3)
print("Adminstration Module Click.")

#Time Management
Time_Management = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Time Management']")))
Time_Management.click()
time.sleep(2)
print("Clicked Successfully on the Time_Management.")

#Roster Setup
Holiday_Setup = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Roster Setup']")))
Holiday_Setup.click()
time.sleep(2)
print("Successfully Clicked on the Roster Setup.")

C

#Select Workplace_group
workplace_group = driver.find_element(By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[1]")
workplace_group.click()
workplace_group.send_keys("PeopleDesk Demo")
workplace_group.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Workplace Group.")

#Select Workplace
workplace= driver.find_element(By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[2]")
workplace.click()
workplace.send_keys("PeopleDesk Demo")
workplace.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Workplace.")

#Enter Roster Name
roster_name = driver.find_element(By.XPATH, "//input[@name='rosterGroupName']")  # Adjust XPath
roster_name.send_keys("Test Roster-00")
roster_name.send_keys(Keys.ENTER)
time.sleep(2)
print("Roster Name Entered Successfully.")

#First_Calendar
first_calendar= driver.find_element(By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[3]")
first_calendar.click()
first_calendar.send_keys("Inbound Shift A")
first_calendar.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered First Calendar.")

#No. of change days
change_days = driver.find_element(By.XPATH, "//input[@name='noOfChangeDays']")  # Adjust XPath
change_days.send_keys("15")
change_days.send_keys(Keys.ENTER)
time.sleep(2)
print("No. of change days Entered Successfully.")

#Next_Calendar
next_calendar= driver.find_element(By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[4]")
next_calendar.click()
next_calendar.send_keys("iBOS")
next_calendar.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Next Calendar.")

# Click Add button
add_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")  # Adjust XPath
add_button.click()
time.sleep(2)
print("Add button Successfully.")

#Next_Calendar
next_calendar= driver.find_element(By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[4]")
next_calendar.click()
next_calendar.send_keys("Inbound Shift A")
next_calendar.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Next Calendar.")

# Click Add button
add_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")  # Adjust XPath
add_button.click()
time.sleep(2)
print("Add button Successfully.")

# Save the roster
save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")  # Adjust XPath
save_button.click()
time.sleep(5)
print("Save button Successfully.")

# Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(2)
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
