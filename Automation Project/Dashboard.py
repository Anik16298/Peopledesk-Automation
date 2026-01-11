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
username_xpath = "(//input[@class='form-control'])[1]"
# username_xpath = '/html/body/div[1]/div/div[1]/div/form/div[1]/div/div/div[2]/div/div[1]/div/div/div/input'
username_field = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, username_xpath)))
username_field.send_keys("bangjin@ibos.io")  # Replace with the desired username

# Locate the password field and input text
password_xpath = "(//input[@class='form-control'])[2]"
# password_xpath = '/html/body/div[1]/div/div[1]/div/form/div[1]/div/div/div[2]/div/div[2]/div/div/div/input'
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
password_field.send_keys("bangjin@ibos")  # Replace with the desired password

# Locate the Login button and click it
submit_xpath = "//button[@type='submit']"
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
submit_button.click()
time.sleep(5)  # Allow the next page to load
print("Login successfully.")

# Wait for the dropdown to appear and click to open it
dropdown_xpath = "//div[@class='d-flex']//div[2]//div[1]//div[1]"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
time.sleep(3)
print("Dropdown clicked successfully.")

# Select the desired option (e.g., "Borobari")
option_xpath = "//li[normalize-space()='Borobari']"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()
time.sleep(2)
print("Option selected successfully.")

# Wait for the 2nd dropdown to appear and click to open it
dropdown_xpath = "//div[@id='topNav']//div[3]//div[1]//div[1]"
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()
time.sleep(3)
print("Dropdown clicked successfully.")

# Select the desired option (e.g., "B. J. Geo Textile Ltd.")
option_xpath = "//li[normalize-space()='B. J. Geo Textile Ltd.']"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()
time.sleep(2)
print("Option selected successfully.")

# Locate the Dashboard button and click it
dashboard_xpath = "//div[@class='item-card text-center']//div"
dashboard_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dashboard_xpath)))
dashboard_button.click()
time.sleep(3)
print("successfully Access To The Dashboard.")

# # Locate the Notice Board and scroll to it
#     nb_xpath = "(//p[text()='Test'])[2]"
#     target_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, nb_xpath)))
#     driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)
#     print("Scrolled to the Notice Board element.")
#     time.sleep(5)
#
# # Click the Notice Board
#     nb_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, nb_xpath)))
#     nb_button.click()
#     print("Successfully clicked the Notice Board.")
#     time.sleep(8)
#
# # Locate the Cancel Button and click it
#     cb_xpath = "//button[@type='button']"
#     cb_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, cb_xpath)))
#     cb_button.click()
#     print("Successfully clicked the Cancel Button.")
#     time.sleep(2)
#
# # Locate the Company Policy and scroll to it
#     cp_xpath = "//p[text()='Test']/following-sibling::p"
#     target_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, cp_xpath)))
#     driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)
#     print("Scrolled to the Company Policy element.")
#     time.sleep(5)
#
# # Click the Company Policy
#     cp_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, cp_xpath)))
#     cp_button.click()
#     print("Successfully clicked the Company Policy.")
#     time.sleep(5)
#
# # Locate the Cancel Button and click it
#     cb_xpath = "//button[@class='btn btn-cancel']"
#     cb_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, cb_xpath)))
#     cb_button.click()
#     print("Successfully clicked the Cancel Button.")
#     time.sleep(2)

# # Smooth scroll to the top of the page:
#     driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
#     print("Scrolled up to the top of the page.")
#     time.sleep(5)
#
# # To Catch Up-Div
#     upd_xpath = "//div[@class='table-card']//div"
#     upd_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, upd_xpath)))

# # Scroll to Dropdown
#     dropdown_xpath = "//h4[@class='employee-self-dashboard-employee-name']"
#     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", dropdown)
#     time.sleep(15)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Supervisor and click it
sdrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[2]"
sdrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sdrop_xpath)))
sdrop_button.click()
print("successfully Access To The Supervisor Dashboard.")
time.sleep(5)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Management and click it
mdrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[3]"
mdrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mdrop_xpath)))
mdrop_button.click()
print("successfully Access To The Management Dashboard.")
time.sleep(8)

# Locate the User Type dropdown and click it
dropdown_xpath = "//div[@id='userType']/div[1]/div[1]/div[1]/div[2]"
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown_button.click()
time.sleep(2)

# Locate the User Type dropdown, Select Employee Lifecycle and click it
eldrop_xpath = "(//div[@id='react-select-peopleDesk-listbox']//div)[4]"
eldrop_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, eldrop_xpath)))
eldrop_button.click()
print("successfully Access To The Employee Lifecycle Dashboard.")
time.sleep(5)

# Employee Lifecycle open
elc_xpath = "//div[@class='ant-table-body']//table/tbody[1]/tr[2]/td[9]/div[1]"
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

# # Out from the Employee Lifecycle using ESC button
#     action = ActionChains(driver)
#     action.send_keys(Keys.ESCAPE).perform()
#     print("ESC key pressed successfully to close the modal or dropdown.")
#     time.sleep(2)

# Locate the X button and click it
x_xpath = "//button[@class='ant-modal-close']//span"
x_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_xpath)))
x_button.click()
print("'X' Button Clicked Successfully.")
time.sleep(2)

# Locate the Home button and click it
homeb_xpath = "//div[@class='company-logo pointer']//img[1]"
homeb_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, homeb_xpath)))
homeb_button.click()
print("Home Button Clicked Successfully.")
time.sleep(5)

# Locate the Compensation & Benefits and click it
benefits_xpath = "//img[@alt='Compensation & Benefits']"
benefits_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, benefits_xpath)))
benefits_menu.click()
time.sleep(5)

# Locate the  Not Assign button and click it
assign_xpath = "//table[@class='table']/tbody[1]/tr[1]/td[9]/div[1]/div[1]/div[1]"
assign_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, assign_xpath)))
assign_button.click()
time.sleep(5)

# Open the Payroll Group Dropdown
payroll_dropdown_xpath = "//div[@id='payrollElement']/div[1]/div[1]/div[1]/div[1]"
payroll_dropdown_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, payroll_dropdown_xpath)))
payroll_dropdown_button.click()

# Select the First Option from the Dropdown
payroll_option_xpath = "//div[@id='react-select-peopleDesk-listbox']//div[1]"
payroll_option_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, payroll_option_xpath)))
payroll_option_button.click()
print("Payroll Element Selected successfully.")
time.sleep(5)

# Input Gross Salary
gs_xpath = "(//div[contains(@class,'form-group login-input')]//input)[2]"
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, gs_xpath)))
input_element.clear()  # Clear any existing value
#Input_element.send_keys("50000")  # Input the value
random_value = random.randint(15000, 50000)
input_element.send_keys(str(random_value)) # Input random value
time.sleep(5)
#Scroll to "Save" button
savebutton_xpath = driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", savebutton_xpath)
time.sleep(2)
#Click "Save" Button
savebutton_xpath = "(//button[normalize-space()='Save'])[1]"
savebutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, savebutton_xpath)))
savebutton.click()
print("Gross Salary input successfully.")

# Out from the Compensation & Benefits using ESC button
action = ActionChains(driver)
action.send_keys(Keys.ESCAPE).perform()
print("ESC key pressed successfully to close the modal or dropdown.")
time.sleep(2)

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
print("WebDriver session closed.")