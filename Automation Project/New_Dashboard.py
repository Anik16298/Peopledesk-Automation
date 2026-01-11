import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

# Initialize Edge WebDriver with options
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("start-maximized")  # Open browser in maximized mode
# Launch Edge browser with specified options
driver = webdriver.Edge(options=edge_options)

# # Initialize Chrome WebDriver with options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("start-maximized")  # Open browser in maximized mode
# # Launch Chrome browser with specified options
# driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://devapp.peopledesk.io/")
# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

# Locate the username field and input text
username_xpath = "//input[@placeholder='Enter your id']"
username_field = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, username_xpath)))
username_field.send_keys("dailystar@ibos.io")  # Replace with the desired username

# Locate the password field and input text
password_xpath = "//input[@placeholder='Enter your password']"
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
password_field.send_keys("dailystar@ibos")  # Replace with the desired password

# Locate the Login button and click it
submit_xpath = "//button[@type='submit']"
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
submit_button.click()
time.sleep(2)  # Allow the next page to load
print("Login successfully.")

# Wait for the dropdown to appear and click to open it
dropdown_xpath = "//*[@id='topNav']/div/div[2]/div[2]/div[2]/div/div"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
time.sleep(2)
print("1st Dropdown clicked successfully.")

# Select the desired option
option_xpath = "//li[normalize-space()='The Daily Star']"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()
time.sleep(2)
print("1st Dropdown Option selected successfully.")

# Wait for the 2nd dropdown to appear and click to open it
dropdown_xpath = "//*[@id='topNav']/div/div[2]/div[2]/div[3]/div/div"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
time.sleep(2)
print("2nd Dropdown clicked successfully.")

# Select the desired option
option_xpath = "//li[normalize-space()='Head Office']"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()
time.sleep(2)
print("2nd Dropdown Option selected successfully.")

# Locate the Dashboard button and click it
dashboard_menu = "//img[@alt='Dashboard']"
dashboard_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dashboard_menu)))
dashboard_menu.click()
time.sleep(2)
print("successfully Accessed To The Dashboard Menu.")

# Define the XPath for Notice Board element
nb_xpath = "//div[@class='noticeCardStyle']"
# Wait for the Notice Board element to be present and scroll into view
target_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, nb_xpath)))
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)
print("Scrolled to the Notice Board element.")
# Wait for the element to be clickable and click
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, nb_xpath))).click()
print("Successfully clicked the Notice.")
time.sleep(3)

# Locate the X Button and click it
cb_xpath = "//button[@type='button']//img[@alt='iBOS']"
cb_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, cb_xpath)))
cb_button.click()
print("Successfully clicked the Cancel Button.")

# Define the XPath for Company Policy element
cp_xpath = "//p[normalize-space()='1.2. SOP HR-004 Child Protection Procedure_compressed.pdf']"
cp_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, cp_xpath)))
cp_button.click()
print("Successfully clicked the Company Policy.")
time.sleep(8)

# Locate the Cancle Button and click it
cb_xpath = "//button[normalize-space()='Cancel']"
cb_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, cb_xpath)))
cb_button.click()
print("Successfully clicked the Cancel Button.")
time.sleep(3)

# Select Supervisor and click it
sup_xpath = "//a[normalize-space()='Supervisor']"
sup_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sup_xpath)))
sup_button.click()
print("successfully Accessed To The Supervisor Dashboard.")
time.sleep(5)

# Select Management and click it
mgt_xpath = "//a[normalize-space()='Management']"
mgt_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mgt_xpath)))
mgt_button.click()
print("successfully Accessed To The Supervisor Dashboard.")
time.sleep(5)

# Select Employee Lifecycle and click it
eldrop_xpath = "//a[normalize-space()='Employee Lifecycle']"
eldrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, eldrop_xpath)))
eldrop_button.click()
print("successfully Access To The Employee Lifecycle Dashboard.")
time.sleep(5)

#Click on Search
search_xpath = "//input[@id='PeopleDeskForm_search']"
search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
search_field.send_keys()
time.sleep(2)
search_field.send_keys("Ahmed Deepto")
print("Successfully Entered Employee Name in Search Field.")
time.sleep(3)

# Employee Lifecycle open
elc_xpath = "//span[normalize-space()='Ahmed Deepto']"
elc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, elc_xpath)))
elc_button.click()
print("successfully Access To The Employee Lifecycle.")
time.sleep(5)

# Click on Next Page Button
np_xpath = "//span[text()='Next Page']"
# Click the Next Page button 13 times
for _ in range(13):
    np_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, np_xpath)))
    np_button.click()
    time.sleep(2)  # Wait for the page to load before the next click
#Print only once after all next page clicked
print("Next Page Button Clicked Successfully.")

# Click on Previous Page Button
pp_xpath = "//span[text()='Prev Page']"
# Click the Previous Page button 13 times
for _ in range(13):
   pp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pp_xpath)))
   pp_button.click()
   time.sleep(2)  # Wait for the page to load before the next click
# Print only once after all prrevious page clicked
print("Previous Page Button Clicked Successfully.")

# Locate the X button and click it
x_button = "(//button[@class='ant-modal-close']//span)[2]"
x_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_button)))
x_button.click()
print("'X' Button Clicked Successfully.")
time.sleep(2)

# # Out from the Employee Lifecycle using ESC button
# action = ActionChains(driver)
# action.send_keys(Keys.ESCAPE).perform()
# print("ESC key pressed successfully to close the Employee Lifecycle.")
# time.sleep(2)

# Locate the Home button and click it
homeb_xpath = "//div[@class='company-logo pointer']//img[1]"
homeb_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, homeb_xpath)))
homeb_button.click()
print("Home Button Clicked Successfully.")
time.sleep(3)

# Locate the Profile button and click it
profile_xpath = "//img[@alt='Profile']"
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
profile_button.click()
print("Clicked on Profile Successfully.")
time.sleep(3)

# Logout from the application
logout_xpath = "//div[@id='simple-popover']//li[3]"  # Update with the correct XPath
logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logout_xpath)))
logout_button.click()
print("Logout successfully.")
time.sleep(5)

# Session_End
driver.quit()
print("WebDriver session closed.")