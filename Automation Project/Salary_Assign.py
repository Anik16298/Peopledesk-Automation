import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import re

# Initialize Edge WebDriver with options
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("start-maximized")  # Open browser in maximized mode
# Launch Edge browser with specified options
driver = webdriver.Edge(options=edge_options)

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

# Locate the Compensation & Benefits Menu and click it
CB_xpath = "//img[@alt='Compensation & Benefits']"
CB_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, CB_xpath)))
CB_menu.click()
time.sleep(2)
print("successfully Accessed To The Compensation & Benefits Menu.")
#....................................................................................
# Locate the  Not Assign button and click it
assign_xpath = "(//div[@label='Not Assigned'])[1]"
assign_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, assign_xpath)))
assign_button.click()
time.sleep(5)

# XPath for the Salary Type dropdown and option
sd_xpath = "//div[@name='salaryType']//div[@class='ant-select-selector']"
# Wait for the Salary Type dropdown to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sd_xpath))).click()
st_xpath = "//div[@class='ant-select-item-option-content'][normalize-space()='Non-Grade']"
# Wait for the specific option to be clickable and select it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, st_xpath))).click()
print("Salary Type Selected successfully.")

# XPath for Payroll Group dropdown and option
payroll_dropdown_xpath = "//div[@name='payrollGroup']//div[@class='ant-select-selector']"
# Wait for the Payroll Group dropdown to be clickable, then click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, payroll_dropdown_xpath))).click()
payroll_option_xpath = "//div[contains(text(),'Test Salary')]"
# Wait for the specific option to be clickable, then click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, payroll_option_xpath))).click()
print("Payroll Group selected successfully.")

# Input Gross Salary
gs_xpath = "//input[@placeholder='Gross']"
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gs_xpath)))
input_element.clear()  # Clear any existing value
#Input_element.send_keys("50000")  # Input the value
random_value = random.randint(20000, 50000)
input_element.send_keys(str(random_value)) # Input random value
time.sleep(5)
# Retrieve the value entered in the Gross Salary field
salary = input_element.get_attribute("value")
# Print the salary entered
print(f"The entered Gross Salary is: {salary}/=")

# # XPath for the Medical field
# medical_xpath = "(//input[@placeholder='Amount'])[3]"
# # Locate the Medical input field and input the value 5000
# medical = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, medical_xpath)))
# # Clear any existing value and input the new value
# medical.clear()
# WebDriverWait(driver, 2)  # Optionally add a brief wait to allow the field to clear if necessary
# medical.send_keys("5000")
# # Retrieve the value entered in the Medical field
# amount = medical.get_attribute("value")
# # Print the entered amount
# print(f"Successfully entered amount {amount}/= into the Medical field.")

# XPath for the bank dropdown
bank_dropdown_xpath = "//div[@name='bank']//div[@class='ant-select-selector']"
# Wait for the dropdown to be clickable and then click on it
bank_dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, bank_dropdown_xpath)))
bank_dropdown_element.click()
# Wait for the options to be loaded and then find the specific option (e.g., 'AB BANK LTD')
bank_option_xpath = "//div[contains(text(),'AB BANK LTD')]"
# Wait for the option to be clickable and click it
bank_option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, bank_option_xpath)))
bank_option_element.click()
# Alternatively, if you need a slight delay to allow for animations or transitions
time.sleep(2)
# Confirm successful selection
print("Successfully selected the bank.")

# XPath for the branch dropdown
branch_dropdown_xpath = "//div[@name='branch']//div[@class='ant-select-selector']"
# Wait for the dropdown to be clickable and then click on it
branch_dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, branch_dropdown_xpath)))
branch_dropdown_element.click()
# XPath for the specific branch option (e.g., 'Panthapath Branch')
branch_option_xpath = "//div[@title='Nawabpur Road Branch ']"
# Wait for the branch option to be clickable and click it
branch_option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, branch_option_xpath)))
branch_option_element.click()
# Alternatively, if you need a slight delay to allow for animations or transitions
time.sleep(2)
# Confirm successful selection
print("Successfully selected the branch.")

# XPath for the employee name
employee_name_xpath = "//h4[@class='name-about-info']"
# Wait for the employee name to be visible and get the text
employee_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, employee_name_xpath)))
employee_name = employee_name_element.text
# Remove any numbers inside square brackets (e.g., [3890])
employee_name = re.sub(r"\s*\[\d+\]", "", employee_name).strip()
# XPath for the account name input field
account_name_xpath = "//input[@id='PeopleDeskForm_account']"
# Wait for the account name input field to be present and input the employee name
account_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, account_name_xpath)))
account_name_field.clear()  # Clear any existing value
account_name_field.send_keys(employee_name)  # Input the employee name into the account name field
# Confirm successful input
print(f"Successfully input the employee name '{employee_name}' into the account name field.")

# XPath for the account number input field
account_no_xpath = "//input[@id='PeopleDeskForm_accountNo']"
# Generate a random 13-digit number
random_account_number = ''.join([str(random.randint(0, 9)) for _ in range(13)])
# Wait for the account number input field to be present
account_no_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, account_no_xpath)))
# Clear any existing value and input the generated random account number
account_no_field.clear()
account_no_field.send_keys(random_account_number)
# Confirm successful input
print(f"Successfully input the random account number '{random_account_number}' into the account number field.")

#=================Locate save Button====================

# XPath for the Save button
savebutton_xpath = "//span[normalize-space()='Save']"
# Find the Save button element
savebutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, savebutton_xpath)))
# XPath for the container to scroll
scroll_container_xpath = "//div[@class='landing-wrapper dashboard-scroll']"
# Find the scroll container element
scroll_container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, scroll_container_xpath)))
# Scroll the container until the Save button is in view
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)  # Scroll to the bottom (if needed)
time.sleep(2)  # Give it time to scroll
# Now scroll the specific container to the Save button
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", savebutton)
time.sleep(2)  # Give it time to scroll into view
# Click the Save button
savebutton.click()
# Print confirmation
print("Salary input successfully.")
time.sleep(3)

#==========Locate Home Button=====================
# Locate the Home button and click it
homeb_xpath = "//div[@class='company-logo pointer']//img[1]"
homeb_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, homeb_xpath)))
homeb_button.click()
print("Home Button Clicked Successfully.")
time.sleep(2)

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
time.sleep(6)

# Session_End
driver.quit()
