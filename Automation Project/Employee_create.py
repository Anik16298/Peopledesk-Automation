import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import names
import random
import string

# Function to initialize WebDriver based on browser type
def get_web_driver(browser="chrome"):
    if browser.lower() == "chrome":
        driver_path = ChromeService(r'chromedriver.exe')
        driver = webdriver.Chrome(service=driver_path)
    elif browser.lower() == "edge":
        driver_path = EdgeService(r'msedgedriver.exe')
        driver = webdriver.Edge(service=driver_path)
    else:
        raise ValueError("Unsupported browser type. Use 'chrome' or 'edge'.")
    return driver

def test_create_employee_all_fields():
    # Initialize the WebDriver
    browser = "chrome"  # Change to 'chrome' or 'edge' if required
    driver = get_web_driver(browser)

# Maximize webdriver
driver.maximize_window()

# Open the target URL
url = "https://devapp.peopledesk.io/"
driver.get(url)
time.sleep(5)  # Allow the page to load

# Locate the username/loginid field and input text
WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "//div[contains(@class,'form-group login-input')]//input"))).send_keys("matador@ibos.io")

# Locate the password field and input text
WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "(//div[contains(@class,'form-group login-input')]//input)[2]"))).send_keys("matador@ibos")  # Replace with the desired password

# Locate the submit button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='auth-log-submit']//button[1]"))).click()

# Wait for the dropdown to appear and click to open it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='d-flex']//div[2]//div[1]//div[1]"))).click()

# Select the desired option (e.g., "Head Office")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Head Office']"))).click()

# Wait until the "Employee Management" button is clickable and then click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='MuiCardContent-root css-1h3am5o']//img)[2]"))).click()
time.sleep(2)

# Wait until the "Employee Create" button is clickable and then click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='ant-btn ant-btn-primary  ']//span)[3]"))).click()
time.sleep(2)

def generate_random_employee_id():
    return 'EMP' + ''.join(random.choices(string.digits, k=5))

def generate_random_employee_name():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    full_name = f"{first_name} {last_name}"
    return full_name

def generate_random_reference_id():
    return 'REF' + ''.join(random.choices(string.digits, k=5))

# Use the functions to generate random values
employee_id = generate_random_employee_id()
employee_name = generate_random_employee_name()
reference_id = generate_random_reference_id()

# Employee ID
driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content']//input)[2]").send_keys( employee_id)
time.sleep(2)

# Full Name
driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content']//input)[3]").send_keys(employee_name)
time.sleep(2)

# Reference ID
driver.find_element(By.XPATH, "//label[text()='Reference ID']/following::input").send_keys(reference_id)
time.sleep(2)

# Workplace Group (Searchable dropdown)
workplace_group = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search']//input)[2]")
workplace_group.click()
time.sleep(1)
workplace_group.send_keys('Head Office')  # Replace with actual option
workplace_group.send_keys(Keys.ENTER)
time.sleep(2)

driver.execute_script("arguments[0].scrollIntoView(true);", workplace_group)
time.sleep(1)

# Workplace/Concern (Searchable dropdown)
workplace = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search']//input)[3]")
workplace.click()
time.sleep(1)
workplace.send_keys('Matador Writing Instruments Ltd')  # Replace with actual option
workplace.send_keys(Keys.ENTER)
time.sleep(2)

driver.execute_script("arguments[0].scrollIntoView(true);", workplace)
time.sleep(1)

# Employment Type (Searchable dropdown)
employment_type = driver.find_element(By.XPATH, "//label[text()='Employment Type']/following::input")
employment_type.click()
time.sleep(1)
employment_type.send_keys('Parmanent')  # Replace with actual option
employment_type.send_keys(Keys.ENTER)
time.sleep(2)

# Joining Date (Date picker input)
joining_date = driver.find_element(By.XPATH, "//div[@class='ant-picker-input']//input")
joining_date.click()
time.sleep(1)
joining_date.clear()
joining_date.send_keys('01/01/2020')
joining_date.send_keys(Keys.ENTER)
time.sleep(2)

# Confirmation Date (Date picker input)
confirmation_date = driver.find_element(By.XPATH, "(//div[@class='ant-picker-input']//input)[2]")
confirmation_date.click()
time.sleep(1)
confirmation_date.clear()
confirmation_date.send_keys('01/04/2020')
confirmation_date.send_keys(Keys.ENTER)
time.sleep(2)

confirmation_date.send_keys(Keys.TAB)
time.sleep(2)

# Department (Searchable dropdown)
department = driver.find_element(By.XPATH, "//input[@id='empCreate_department']")
department.click()
time.sleep(1)
department.send_keys('Admin')  # Replace with actual option
department.send_keys(Keys.ENTER)
time.sleep(2)

# Section (Searchable dropdown)
section = driver.find_element(By.XPATH, "//input[@id='empCreate_section']")
section.click()
time.sleep(1)
section.send_keys('Test 01')  # Replace with actual option
section.send_keys(Keys.ENTER)
time.sleep(2)

# Designation (Searchable dropdown)
designation = driver.find_element(By.XPATH, "//input[@id='empCreate_designation']")
designation.click()
time.sleep(1)
designation.send_keys('Cleaner')  # Replace with actual option
designation.send_keys(Keys.ENTER)
time.sleep(2)

# HR Position (Searchable dropdown)
hr_position = driver.find_element(By.XPATH, "//input[@id='empCreate_hrPosition']")
hr_position.click()
time.sleep(1)
hr_position.send_keys('Executive')  # Replace with actual option
hr_position.send_keys(Keys.ENTER)
time.sleep(2)

# Supervisor (Searchable dropdown)
supervisor = driver.find_element(By.XPATH, "//input[@id='empCreate_supervisor']")
supervisor.click()
time.sleep(1)
supervisor.send_keys('Abdur Rashid')  # Replace with actual option
time.sleep(3)
supervisor.send_keys(Keys.ENTER)
time.sleep(1)

# Dotted Supervisor (Searchable dropdown)
dotted_supervisor = driver.find_element(By.XPATH, "//input[@id='empCreate_dottedSupervisor']")
dotted_supervisor.click()
time.sleep(1)
dotted_supervisor.send_keys('Abdur Rashid')  # Replace with actual option
time.sleep(2)
dotted_supervisor.send_keys(Keys.ENTER)
time.sleep(1)

# Line Manager (Searchable dropdown)
line_manager = driver.find_element(By.XPATH, "//input[@id='empCreate_lineManager']")
line_manager.click()
time.sleep(1)
line_manager.send_keys('Abdur Rashid')  # Replace with actual option
time.sleep(2)
line_manager.send_keys(Keys.ENTER)
time.sleep(1)

# Salary Type
salary_type = driver.find_element(By.XPATH, "//input[@id='empCreate_salaryType']")
salary_type.send_keys('Hourly')  # Replace with an actual option
time.sleep(2)
salary_type.send_keys(Keys.ENTER)
time.sleep(1)

# Overtime Type
overtime_type = driver.find_element(By.XPATH, "//input[@id='empCreate_otType']")
overtime_type.send_keys('Not Applicable')  # Replace with an actual option
time.sleep(2)
overtime_type.send_keys(Keys.ENTER)
time.sleep(1)

# Overtime Based On
overtime_based_on = driver.find_element(By.XPATH, "//input[@id='empCreate_strOTbasedon']")
overtime_based_on.send_keys('Calendar')  # Replace with an actual option
time.sleep(2)
overtime_based_on.send_keys(Keys.ENTER)
time.sleep(1)

# Voluntary Disclosures - Religion
religion = driver.find_element(By.XPATH, "//input[@id='empCreate_religion']")
religion.send_keys('Christian')  # Replace with an actual option
time.sleep(2)
religion.send_keys(Keys.ENTER)
time.sleep(1)

# Voluntary Disclosures - Gender
gender = driver.find_element(By.XPATH, "//input[@id='empCreate_gender']")
gender.send_keys('Male')  # Replace with an actual option
time.sleep(2)
gender.send_keys(Keys.ENTER)
time.sleep(1)

# Voluntary Disclosures - Date of Birth (Date picker input)
dob = driver.find_element(By.XPATH, "//input[@id='empCreate_dateofBirth']")
dob.click()
time.sleep(1)
dob.clear()
dob.send_keys('06/05/1995')  # Send the date in the required format
dob.send_keys(Keys.ENTER)
time.sleep(2)

# Voluntary Disclosures - Blood Group
blood_group = driver.find_element(By.XPATH, "//input[@id='empCreate_bloodGroup']")
blood_group.send_keys('B Posative')  # Replace with an actual option
time.sleep(2)
blood_group.send_keys(Keys.ENTER)
time.sleep(1)

# Voluntary Disclosures - Personal/Office Email
email = driver.find_element(By.XPATH, "//input[@id='empCreate_officeEmail']")
email.send_keys('demo@ibos.io')
time.sleep(2)

# Voluntary Disclosures - Personal/Office Contact No
contact_no = driver.find_element(By.XPATH, "//input[@id='empCreate_officePhone']")
contact_no.send_keys('01329731858')
time.sleep(2)

# Voluntary Disclosures - NID
nid = driver.find_element(By.XPATH, "//input[@id='empCreate_nid']")
nid.send_keys('987654321')
time.sleep(2)

# Voluntary Disclosures - TIN No
tin = driver.find_element(By.XPATH, "//input[@id='empCreate_tinNo']")
tin.send_keys('TIN123456')
time.sleep(2)

# Voluntary Disclosures - Permanent Address
permanent_address = driver.find_element(By.XPATH, "//input[@id='empCreate_permanentAddress']")
permanent_address.send_keys('78/2, Borobag, Mirpur-2, Dhaka, Bangladesh')
time.sleep(2)

# Voluntary Disclosures - Present Address
present_address = driver.find_element(By.XPATH, "//input[@id='empCreate_presentAddress']")
present_address.send_keys('78/2, Borobag, Mirpur-2, Dhaka, Bangladesh')
time.sleep(2)

# Employment Shift Info - Calendar Type
calendar_type = driver.find_element(By.XPATH, "//input[@id='empCreate_calenderType']")
calendar_type.send_keys('Calendar')  # Replace with an actual option
time.sleep(2)
calendar_type.send_keys(Keys.ENTER)
time.sleep(1)

# Employment Shift Info - Calendar Name
calendar_type = driver.find_element(By.XPATH, "//input[@id='empCreate_calender']")
calendar_type.send_keys('HO-Driver')  # Replace with an actual option
time.sleep(2)
calendar_type.send_keys(Keys.ENTER)
time.sleep(1)

# Select Off Day
off_day = driver.find_element(By.XPATH, "//div[@class='ant-select-selection-overflow']")
off_day.click()
time.sleep(1)
off_day_option = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and text()='Friday']")
off_day_option.click()
time.sleep(1)

# Click the Holiday field to shift focus
holiday = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//div[@name='holiday']//div[@class='ant-select-selector']")))
holiday.click()
time.sleep(2)

# Select 'Holiday List HO MWIL 2024'
holiday_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and text()='Holiday List HO MWIL 2024']")))
holiday_option.click()
time.sleep(2)

# Smooth scroll to the top of the page using a loop for better effect
for i in range(0, 100, 10):
 driver.execute_script(f"window.scrollTo(0, {i});")  # Scroll incrementally
time.sleep(4)  # Small delay for smooth effect
driver.execute_script("window.scrollTo(0, 0);")  # Ensure final scroll to top
print("Scrolled up to the top of the page.")
time.sleep(5)

# Click on 'Save' button to submit the form
save_button = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
save_button.click()
time.sleep(5)

# Teardown
driver.quit()


# Run the test case
test_create_employee_all_fields()
