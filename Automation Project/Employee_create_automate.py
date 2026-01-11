import time
import random
import names
import string
from multiprocessing.pool import worker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

##......................................LogIn Feature

# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("dailystar@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("dailystar@ibos")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()

# Verify dashboard visibility
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Dashboard']")))
assert dashboard_element.is_displayed(), "Login failed or dashboard not found."
print("Login successful, dashboard is visible.")

##...........................Login Feature Finish

# ## Business Unit Select Feature2
# # Wait for the dropdown to appear and click to open it
# dropdown_xpath = "//div[@class='d-flex']//div[2]//div[1]//div[1]"
# dropdown = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)) )
# WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
# dropdown.click()
# print("Dropdown clicked successfully.")
#
# # Select the desired option (e.g., "Head Office")
# option_xpath = "//li[normalize-space()='Head Office']"
#
# # Select the desired option (e.g., "Matador Industrial Park")
# # option_xpath = "//li[normalize-space()='Matador Industrial Park']"
# option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
# option.click()
# print("Option selected successfully.")
# time.sleep(2)

#Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
print("Clicked on Employee Management")

#Employee
employee = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee']")))
employee.click()
time.sleep(3)

#Create button click
create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create New']")))
create_button.click()
time.sleep(3)

##Employee System Onboard 1st step
#Employee id
def generate_random_employee_id():
    return 'EMP-' + ''.join(random.choices(string.digits, k=4))
def generate_random_employee_name():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    full_name = f"{first_name} {last_name}"
    return full_name
def generate_random_reference_id():
    return 'REF-' + ''.join(random.choices(string.digits, k=4))


#Use the functions to generate random values
employee_id = generate_random_employee_id()
employee_name = generate_random_employee_name()
reference_id = generate_random_reference_id()

#Employee ID
driver.find_element(By.XPATH, "//input[@id='empCreate_employeeCode']").send_keys(employee_id)
time.sleep(2)

#Full Name
driver.find_element(By.XPATH, "//input[@id='empCreate_fullName']").send_keys(employee_name)
time.sleep(2)

#Reference ID
driver.find_element(By.XPATH, "//input[@id='empCreate_strReferenceId']").send_keys(reference_id)
time.sleep(2)

#Workplace group
driver.find_element(By.XPATH,"//input[@id='empCreate_workplaceGroup']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[text()='The Daily Star'])[2]").click()
time.sleep(3)
print("Workplace Group entered successfully.")

#Workplace
driver.find_element(By.XPATH,"//input[@id='empCreate_workplace']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[text()='Head Office'])[2]").click()
time.sleep(3)
print("Workplace entered successfully.")

#Employee type
driver.find_element(By.XPATH,"//input[@id='empCreate_employeeType']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='Permanent']//div[1]").click()
time.sleep(3)
print("Employee Type entered successfully.")

#Joining Date
join_date=(driver.find_element(By.XPATH,"//input[@id='empCreate_joiningDate']"))
# join_date.click()
# time.sleep(3)
join_date.send_keys("05/02/2023")
join_date.send_keys(Keys.ENTER)
time.sleep(3)
## join_date.send_keys
# join_date = driver.find_element(By.XPATH,"//a[text()='Today']")
# join_date.click()
# time.sleep(3)
print("Joining date entered successfully.")

# Confirmation Date (Date picker input)
confirmation_date = driver.find_element(By.XPATH, "(//div[@class='ant-picker-input']//input)[2]")
confirmation_date.click()
time.sleep(1)
confirmation_date.clear()
confirmation_date.send_keys('02/07/2023')
confirmation_date.send_keys(Keys.ENTER)
time.sleep(2)
confirmation_date.send_keys(Keys.TAB)
time.sleep(2)

#Department
driver.find_element(By.XPATH,"//input[@id='empCreate_department']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='Business Development']//div[1]").click()
time.sleep(3)
print("Department entered successfully.")

#Section
driver.find_element(By.XPATH,"//input[@id='empCreate_section']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='Digital Sales']//div[1]").click()
time.sleep(3)
print("Section entered successfully.")

#Designation
driver.find_element(By.XPATH,"//input[@id='empCreate_designation']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='Executive, Human Resources']//div[1]").click()
time.sleep(3)
print("Designation entered successfully.")

#HR Position
driver.find_element(By.XPATH,"//input[@id='empCreate_hrPosition']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='bbb']//div[1]").click()
time.sleep(3)
print("HR Position entered successfully.")

#Supervisor
supervisor= driver.find_element(By.XPATH,"//input[@id='empCreate_supervisor']")
supervisor.click()
time.sleep(3)
supervisor.send_keys("1001")
time.sleep(3)
supervisor_option = driver.find_element(By.XPATH, "//div[@title='Mahfuz Anam [1001]']//div[1]")
supervisor_option.click()
time.sleep(5)
print("Supervisor entered successfully.")

#DotedSupervisor
dotedsupervisor = driver.find_element(By.XPATH,"//input[@id='empCreate_dottedSupervisor']")
dotedsupervisor.click()
time.sleep(3)
dotedsupervisor.send_keys("3501")
time.sleep(3)
dotedsupervisor_option= driver.find_element(By.XPATH,"//div[@title='Mizanur Rahman FCA [3501]']//div[1]")
dotedsupervisor_option.click()
time.sleep(5)
print("Doted Supervisor entered successfully.")

#Line Manager
line_manager = driver.find_element(By.XPATH,"//input[@id='empCreate_lineManager']")
line_manager.click()
time.sleep(3)
line_manager.send_keys("61218")
time.sleep(3)
linemanager_option= driver.find_element(By.XPATH,"//div[@title='Parban Chakma [61218]']//div[1]")
linemanager_option.click()
time.sleep(5)
print("Line Manager entered successfully.")

#Salary Type
salarytype = driver.find_element(By.XPATH,"//input[@id='empCreate_salaryType']")
salarytype.send_keys("Hourly")
salarytype.send_keys(Keys.ENTER)
time.sleep(5)

#OverTime Type
overtime_type= driver.find_element(By.XPATH,"//input[@id='empCreate_otType']")
overtime_type.send_keys("Not Applicable")
overtime_type.send_keys(Keys.ENTER)
time.sleep(3)
print("OverTime Type entered successfully.")

#Overtime Based on
overtime_based_on= driver.find_element(By.XPATH,"//input[@id='empCreate_strOTbasedon']")
overtime_based_on.send_keys("Calendar")
overtime_based_on.send_keys(Keys.ENTER)
time.sleep(3)
print("Overtime Based on entered successfully.")

#PayScale Grade
driver.find_element(By.XPATH,"//input[@id='empCreate_payScaleGrade']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='Grade-3']//div[1]").click()
time.sleep(3)
print("PayScale Grade entered successfully.")

# #Employee Signature
# employee_signature= driver.find_element(By.XPATH,"//span[text()='Employee Signature']")
# employee_signature.send_keys("C:\Users\ibos\Downloads\Image\signature-2.png")
# time.sleep(3)
# print("Employee Signature entered successfully.")

#Employee Signature
# Locate the actual file input field (update XPath if necessary)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
# Send the file path to upload
file_input.send_keys(r"C:\Users\ibos\Downloads\Image\signature-2.png")
time.sleep(3)
print("Employee Signature uploaded successfully.")

##........Employee System Onboard 1st step

##Voluntary Disclosures
# #Religion
# driver.find_element(By.XPATH,"//input[@id='empCreate_religion']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//div[text()='Islam']").click()
# time.sleep(3)
# print("Religion entered successfully.")

#Religion
driver.find_element(By.XPATH,"//input[@id='empCreate_religion']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='Others']").click()
time.sleep(3)
print("Religion entered successfully.")


# #Gender
# driver.find_element(By.XPATH,"//input[@id='empCreate_gender']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//div[text()='Male']").click()
# time.sleep(3)
# print("Gender entered successfully.")

#Gender
driver.find_element(By.XPATH,"//input[@id='empCreate_gender']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@title='Others']//div)[2]").click()
time.sleep(3)
print("Gender entered successfully.")

#Birthday date
birthday_date= driver.find_element(By.XPATH,"//input[@id='empCreate_dateofBirth']")
birthday_date.send_keys("07/05/1996")
birthday_date.send_keys(Keys.ENTER)
time.sleep(3)
print("Birthday date entered successfully.")

#Blood Group
blood_group = driver.find_element(By.XPATH,"//input[@id='empCreate_bloodGroup']")
blood_group.click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@title='O positive']//div[1]").click()
time.sleep(3)
print("Blood Group successfully.")

#Office Email
office_email = driver.find_element(By.XPATH,"//input[@placeholder='Office Email']")
office_email.send_keys("test@gmail.com")
time.sleep(2)
print("Personal/Office Email Entered successfully.")

#Personal/Office Contact No.
contact_num = driver.find_element(By.XPATH,"//input[@id='empCreate_officePhone']")
contact_num.send_keys("01557272482")
time.sleep(2)
print("Personal/Office Contact No. Entered successfully.")

#NID
nid = driver.find_element(By.XPATH,"//input[@id='empCreate_nid']")
nid.send_keys("7876441658")
time.sleep(2)
print("NID Entered successfully.")

#TIN
tin = driver.find_element(By.XPATH,"//input[@id='empCreate_tinNo']")
tin.send_keys("847586082365")
time.sleep(2)

#Permanent Address
tin = driver.find_element(By.XPATH,"//input[@id='empCreate_permanentAddress']")
tin.send_keys("Test Location-X")
time.sleep(2)

#Present Address
tin = driver.find_element(By.XPATH,"//input[@id='empCreate_presentAddress']")
tin.send_keys("Test Location-Y")
time.sleep(2)
##....................Voluntary Disclosures

#Employment Shift Info
#Calendar Type
driver.find_element(By.XPATH,"//input[@id='empCreate_calenderType']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@title='Calendar']//div)[2]").click()
time.sleep(2)

# dropdown = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='empCreate_calenderType']"))
# )
# dropdown.click()

# Wait until the desired option appears and then click it
# option = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "(//div[@title='Calendar']//div)[2]"))
# )
# option.click()

#Calendar Name
calendarname = driver.find_element(By.XPATH,"//input[@id='empCreate_calender']")
calendarname.click()
time.sleep(2)
calendar_option= driver.find_element(By.XPATH,"//div[@title='General (Head Office)']//div[1]")
calendar_option.click()
time.sleep(3)

# Calender Generate Date
calender_generate_date = driver.find_element(By.XPATH, "//input[@id='empCreate_generateDate']")
calender_generate_date.click()
time.sleep(1)
calender_generate_date.clear()
calender_generate_date.send_keys('02/01/2025')
calender_generate_date.send_keys(Keys.ENTER)
time.sleep(2)
calender_generate_date.send_keys(Keys.TAB)
time.sleep(2)

#Offday
Offday= driver.find_element(By.XPATH,"//input[@id='empCreate_offday']")
Offday.click()
time.sleep(3)
offday_option = driver.find_element(By.XPATH,"//div[@title='Friday']//div[1]")
offday_option.click()
time.sleep(3)

#Holiday
holiday= driver.find_element(By.XPATH,"//input[@id='empCreate_holiday']")
holiday.click()
time.sleep(3)
holiday_option = driver.find_element(By.XPATH,"//div[@title='Government Holiday for Head Office 2025']//div[1]")
holiday_option.click()
time.sleep(3)
print("Holiday entered successfully.")
#................Employment Shift Info

#Employee System Access
#ESS Portal
ess_portal= driver.find_element(By.XPATH,"//input[@type='checkbox']")
ess_portal.click()
time.sleep(3)

#Office Email
office_email = driver.find_element(By.XPATH,"(//input[@placeholder='Office Email'])[2]")
office_email.send_keys("test@gmail.com")
time.sleep(2)
print("Office Email Entered successfully.")

#Contact No.
contact_num = driver.find_element(By.XPATH,"//input[@placeholder='Contact No.']")
contact_num.send_keys("01557272482")
time.sleep(2)
print("Contact No. Entered successfully.")
#...............Employee System Access

# Scroll to Save Button
save_button = driver.find_element(By.XPATH, "(//button[@type='button']//span)[3]")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", save_button)
time.sleep(2)

# Click Save
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button']//span)[3]"))).click()
time.sleep(10)
print("Employee Created Successfully")

# Navigate to employee profile
employee_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[2]/td[4]")))
employee_profile.click()
time.sleep(8)
print("Navigated to employee profile successfully.")

# Return to employee management dashbboard
back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'d-flex align-items-center')]//button)[1]")))
back_button.click()
time.sleep(5)
print("Return to employee management dashbboard.")

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
time.sleep(6)

# Session_End
driver.quit()
print("WebDriver session closed.")