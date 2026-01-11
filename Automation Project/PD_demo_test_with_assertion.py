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

# Open the website
driver.get("https://devapp.peopledesk.io/")

# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

# Locate the username field and input text
username_xpath = "(//input[@class='form-control'])[1]"
username_field = WebDriverWait(driver, 10).until(
 EC.presence_of_element_located((By.XPATH, username_xpath)))
assert username_field.is_displayed(), "Username field is not displayed"
username_field.send_keys("bangjin@ibos.io")  # Replace with the desired username

# Locate the password field and input text
password_xpath = "(//input[@class='form-control'])[2]"
password_field = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, password_xpath)))
assert password_field.is_displayed(), "Password field is not displayed"
password_field.send_keys("bangjin@ibos")  # Replace with the desired password

# Locate the Login button and click it
submit_xpath = "//button[@type='submit']"
submit_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, submit_xpath)))
assert submit_button.is_enabled(), "Submit button is not enabled"
submit_button.click()
print("Login successfully.")
time.sleep(5)  # Allow the next page to load

# Wait for the dropdown to appear and click to open it
dropdown_xpath = "//div[@class='d-flex']//div[2]//div[1]//div[1]"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
assert dropdown.is_displayed(), "Dropdown is not displayed"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
print("Dropdown clicked successfully.")

# Select the desired option (e.g., "Borobari")
option_xpath = "(//ul[contains(@class,'MuiList-root MuiList-padding')]//li)[3]"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
assert option.is_displayed(), "Option is not displayed"
option.click()
print("Option selected successfully.")
time.sleep(5)

# Wait for the 2nd dropdown to appear and click to open it
dropdown_xpath = "//div[@id='topNav']//div[3]//div[1]//div[1]"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
assert dropdown.is_displayed(), "Second dropdown is not displayed"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
print("Second dropdown clicked successfully.")

# Select the desired option (e.g., "B. J. Geo Textile Ltd.")
option_xpath = "//li[normalize-space()='B. J. Geo Textile Ltd.']"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
assert option.is_displayed(), "Second option is not displayed"
option.click()
print("Second option selected successfully.")
time.sleep(5)

# Locate the Dashboard button and click it
dashboard_xpath = "//div[@class='item-card text-center']//div"
dashboard_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dashboard_xpath)))
assert dashboard_button.is_enabled(), "Dashboard button is not enabled"
dashboard_button.click()
print("successfully Access To The Dashboard.")
time.sleep(5)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
assert dropdown_button.is_enabled(), "Dropdown button is not enabled"
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Supervisor and click it
sdrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[2]"
sdrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sdrop_xpath)))
assert sdrop_button.is_enabled(), "Supervisor dropdown option is not enabled"
sdrop_button.click()
print("successfully Access To The Supervisor Dashboard.")
time.sleep(5)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
assert dropdown_button.is_enabled(), "Dropdown button is not enabled"
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Management and click it
mdrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[3]"
mdrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mdrop_xpath)))
assert mdrop_button.is_enabled(), "Management dropdown option is not enabled"
mdrop_button.click()
print("successfully Access To The Management Dashboard.")
time.sleep(8)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
assert dropdown_button.is_enabled(), "Dropdown button is not enabled"
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Employee Lifecycle and click it
eldrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[4]"
eldrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, eldrop_xpath)))
assert eldrop_button.is_enabled(), "Employee Lifecycle dropdown option is not enabled"
eldrop_button.click()
print("successfully Access To The Employee Lifecycle Dashboard.")
time.sleep(5)

# Employee Lifecycle open
elc_xpath = "//div[@class='ant-table-body']//table/tbody[1]/tr[2]/td[9]/div[1]"
elc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, elc_xpath)))
assert elc_button.is_enabled(), "Employee Lifecycle button is not enabled"
elc_button.click()
print("successfully Access To The Employee Lifecycle.")
time.sleep(5)

# Click on Next Page Button 13 times......output show once.
np_xpath = "//span[text()='Next Page']"

for _ in range(13):
    np_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, np_xpath)))
    assert np_button.is_enabled(), "Next Page button is not enabled"
    np_button.click()
    time.sleep(2)  # Ensure the page loads before the next click

# Print only once after all 13 clicks......output show once.
print("Next Page Button successfully clicked 13 times.")

# Click on Previous Page Button 13 times......output show once.
pp_xpath = "//span[text()='Prev Page']"

for _ in range(13):
    pp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pp_xpath)))
    assert pp_button.is_enabled(), "Previous Page button is not enabled"
    pp_button.click()
    time.sleep(5)  # Ensure the page loads before the next click

# Print only once after all 13 clicks
print("Previous Page Button successfully clicked 13 times.")

# Locate the X button and click it
x_xpath = "//button[@class='ant-modal-close']//span"
x_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_xpath)))
assert x_button.is_enabled(), "X button is not enabled"
x_button.click()
print("'X' Button Clicked Successfully.")
time.sleep(2)

# Locate the Home button and click it
homeb_xpath = "//div[@class='company-logo pointer']//img[1]"
homeb_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, homeb_xpath)))
assert homeb_button.is_enabled(), "Home button is not enabled"
homeb_button.click()
print("Home Button Clicked Successfully.")
time.sleep(5)

# Locate the Compensation & Benefits and click it
benefits_xpath = "//img[@alt='Compensation & Benefits']"
benefits_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, benefits_xpath)))
assert benefits_button.is_enabled(), "Benefits button is not enabled"
benefits_button.click()
time.sleep(5)

# Locate the Not Assign button and click it
assign_xpath = "//table[@class='table']/tbody[1]/tr[1]/td[9]/div[1]/div[1]/div[1]"
assign_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, assign_xpath)))
assert assign_button.is_enabled(), "Assign button is not enabled"
assign_button.click()
time.sleep(5)

# Open the Payroll Group Dropdown
payroll_dropdown_xpath = "//div[@id='payrollElement']/div[1]/div[1]/div[1]/div[1]"
payroll_dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, payroll_dropdown_xpath)))
assert payroll_dropdown_button.is_enabled(), "Payroll dropdown button is not enabled"
payroll_dropdown_button.click()

# Select the First Option from the Dropdown
payroll_option_xpath = "//div[@id='react-select-peopleDesk-listbox']//div[1]"
payroll_option_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, payroll_option_xpath)))
assert payroll_option_button.is_enabled(), "Payroll option button is not enabled"
payroll_option_button.click()
print("Payroll Element Selected successfully.")
time.sleep(5)

# Input Gross Salary
gs_xpath = "(//div[contains(@class,'form-group login-input')]//input)[2]"
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gs_xpath)))
input_element.clear()  # Clear any existing value
random_value = random.randint(15000, 50000)
input_element.send_keys(str(random_value))  # Input random value
time.sleep(10)
print("Gross Salary input successfully.")

# Out from the Compensation & Benefits using ESC button
action = ActionChains(driver)
action.send_keys(Keys.ESCAPE).perform()
print("ESC key pressed successfully to close the modal or dropdown.")
time.sleep(2)

# Locate the Home button and click it
homeb_xpath = "//div[@class='company-logo pointer']//img[1]"
homeb_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, homeb_xpath)))
assert homeb_button.is_enabled(), "Home button is not enabled"
homeb_button.click()
print("Home Button Clicked Successfully.")
time.sleep(2)

# Locate the Profile button and click it
profile_xpath = "//span[@class='profile-menu-img']//img[1]"
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
assert profile_button.is_enabled(), "Profile button is not enabled"
profile_button.click()
print("Clicked on Profile Successfully.")
time.sleep(2)

# Logout from the application
logout_xpath = "(//ul[@class='profile-popup-list']//li)[3]"  # Update with the correct XPath
logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logout_xpath)))
assert logout_button.is_enabled(), "Logout button is not enabled"
logout_button.click()
print("Logout successfully.")
time.sleep(6)

# Session_End
driver.quit()
print("WebDriver session closed.")
