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

#===============LogIn Feature============
# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("peopledeskdemo@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("12345")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()
print("Log In successfully.")

#============Go to Leave Policy==================
#Adminstration
Adminstration = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Administration']"))).click()
time.sleep(3)
print("Adminstration Module Click.")

#Leave and Movement
Leave_movement = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Leave and Movement']"))).click()
time.sleep(2)
print("Successfully Clicked on the Leave and Movement.")

#Leave Policy
Leave_policy = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Leave Policy']"))).click()
time.sleep(2)
print("Successfully Clicked on the Leave Policy.")

#Create Leave Policy
Create = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create']"))).click()
time.sleep(2)
print("Successfully Clicked the CREATE button.")

#============General Configuration=============
# Fill in the "Policy Name" field
Policy_name_field = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_strPolicyName']")
Policy_name_field.send_keys('Test Leave-1')
time.sleep(2)
print("Successfully Entered Policy Name.")

# "Leave Type" Select
Leave_type_dropdown = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_leaveType']").click()
time.sleep(2)
Leave_type_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Leave For Test-01')]")
actions = ActionChains(driver)
actions.move_to_element(Leave_type_dropdown).perform()
Leave_type_dropdown.click()
time.sleep(3)
print("Leave Type Successfully Selected.")

# Fill  the "Display Name" field
Display_name_field = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_strDisplayName']")
Display_name_field.send_keys('Test Leave-1')
time.sleep(2)
print("Successfully Entered Display Name.")

# Fill in the "Display Code" field
Display_code_field = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_strDisplayCode']")
Display_code_field.send_keys('TL-1')
time.sleep(2)
print("Successfully Entered Display Code.")

# Select from "Workplace" dropdown
Workplace_dropdown = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_workplace']").click()
time.sleep(2)
Workplace_dropdown = driver.find_element(By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='PeopleDesk Demo']").click()
time.sleep(2)
print("Workplace Successfully Selected.")

# Select from "Designation" dropdown
Designation = driver.find_element(By.XPATH, "//div[@name='designationListDTO']").click()
time.sleep(2)
Designation = driver.find_element(By.XPATH, "(//div[text()='All'])[1]").click()
time.sleep(2)
print("Designation Successfully Selected.")

# Select from "Employment Type" dropdown
Employment_type = driver.find_element(By.XPATH, "//div[@name='intEmploymentTypeList']").click()
time.sleep(2)
#Employment_type = driver.find_element(By.XPATH, "//div[@class='ant-select-item ant-select-item-option ant-select-item-option-active']//div[@class='ant-select-item-option-content'][normalize-space()='All']")
driver.find_element(By.XPATH, "(//div[text()='All'])[2]").click()
# Employment_type.click()
time.sleep(2)
print("Employment Type Successfully Selected.")

# Select from "Gender" dropdown
Gender = driver.find_element(By.XPATH, "//div[@name='intGender']").click()
time.sleep(2)
# Gender = driver.find_element(By.XPATH, "//div[@class='ant-select-item-option-content' and text()='All']")
# Gender.click()
driver.find_element(By.XPATH, "(//div[text()='All'])[3]").click()
time.sleep(2)
print("Gender Selected Successfully.")

# Select from "Religion" dropdown
Religion = driver.find_element(By.XPATH, "//div[@name='religionListDto']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[text()='All'])[4]").click()
time.sleep(2)
print("Religion Selected Successfully.")

# Upload an attachment
Upload_file = driver.find_element(By.XPATH, "//input[@type='file']")
time.sleep(3)
Upload_file.send_keys(r"C:\Users\ibos\Downloads\Image\Blank.jpg")
time.sleep(3)
print("Attachment uploaded successfully.")

#==========Leave Description================
# Write Description
Description = driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']//p")
time.sleep(2)
Description.send_keys("This is a Test Policy.")
time.sleep(3)
print("Description write successfully.")

#=========Paid Leave Configuration============
# Scroll to better view
Leave = driver.find_element(By.XPATH, "//div//span[text()='Leave Consume Type']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Leave)
time.sleep(2)

# Fill in the "Paid Type" dropdown
Paid_type_dropdown = driver.find_element(By.XPATH, "//span[@title='Paid Leave']").click()
time.sleep(2)
Paid_type_dropdown = driver.find_element(By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='Paid Leave']").click()
time.sleep(2)
print("'Paid Type' Selected successfully.")

# Fill in the "Pay Depend On" dropdown
Pay_depend_on_dropdown = driver.find_element(By.XPATH, "//span[@title='Gross Salary']").click()
time.sleep(2)
Pay_depend_on_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Gross Salary')]").click()
time.sleep(2)
print("'Pay Depend On' Selected successfully.")

# Fill in the "Pay Depend On Value"
Pay_depend_on_value_field = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_payValue']")
# Pay_depend_on_value_field.clear()
Pay_depend_on_value_field.send_keys('100')
time.sleep(2)
print("'Pay Depend On Value' Selected successfully.")

#======Leave Consume Type==========
# Fill in the "Leave Consume Type" dropdown
Leave_consume_type_dropdown = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_leaveConsumeType']").click()
time.sleep(2)
Leave_consume_type_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Full Day')]").click()
Add_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Add')])[1]").click()
time.sleep(2)
print("'Leave Consume Type' Selected successfully.")

#==============Leave Lapse============
# Fill in "Leave Lapse After"
Leave_lapse_after = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_leavelapse']").click()
time.sleep(2)
Leave_lapse_after = driver.find_element(By.XPATH, "//div[contains(text(),'Calender Year')]").click()
time.sleep(2)
print("'Leave Lapse After' Selected successfully.")

# Scroll
Leave_balance = driver.find_element(By.XPATH, "//div//span[text()='Leave Balance']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Leave_balance)
time.sleep(2)

#================Pro Rata==========
# Fill in the "Pro Rata" dropdown
Pro_rata = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[16]").click()
time.sleep(2)
Pro_rata = driver.find_element(By.XPATH, "//div[contains(text(),'No')]").click()
time.sleep(2)
print("'ProRata' Selected successfully.")

#=============Leave Balance==================
# Select "Service Length Depend On" from the dropdown
Service_Depend_selection = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[17]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[text()='Date of Joining'])[2]").click()
time.sleep(2)
print("'Service Length Depend On' Selected successfully.")

# Locate and fill in the "From Service Length (Month)" field
From_service_length = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_serviceStartLengthBalance']")
From_service_length.send_keys("0")  # Example service length in months
time.sleep(2)
print("'From Service Length' input successfully.")

# Locate and fill in the "To Service Length (Month)" field
To_service_length = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_serviceEndLengthBalance']")
To_service_length.send_keys("999")
time.sleep(2)
print("'TO Service Length' input successfully.")

# Select "Leave Balance Depend On" dropdown and choose an option
Leave_balance_depend_on = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[20]").click()
time.sleep(2)
Leave_balance_depend_on = driver.find_element(By.XPATH, "//div[contains(text(),'Fixed Days')]").click()
time.sleep(2)
print("'Leave Balance Depend On' Selected successfully.")

# Locate and fill in the "Leave Days" field
Leave_days = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_leaveDaysFor']")
Leave_days.send_keys("5")
time.sleep(2)
print("'Leave Days' input successfully.")

# Click the "ADD" button to add the data
Add_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Add')])[2]").click()
time.sleep(4)
print("Add button clicked successfully.")

# Click the "NEXT" button
Next_button = driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
time.sleep(3)
print("NEXT button clicked successfully.")

#=============Leave Carry Forward==================
# Click the "Leave carry Forward" field and select option
Leave_cf = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[2]")
Leave_cf.click()
time.sleep(2)
Leave_cf = driver.find_element(By.XPATH, "//div[contains(text(),'No')]").click()
time.sleep(2)
print("'Leave carry Forward' option selected successfully.")

# Click the "NEXT" button
Next_button = driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
time.sleep(2)
print("NEXT button clicked successfully.")

#=============Leave Encadshment==================
# Click the "Leave carry Forward" field and select option
Leave_ect = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[2]")
Leave_ect.click()
time.sleep(2)
Leave_ect = driver.find_element(By.XPATH, "//div[contains(text(),'No')]")
Leave_ect.click()
print("'Leave Encashment' option selected successfully.")

# Click the "NEXT" button
Next_button = driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
time.sleep(3)
print("NEXT button clicked successfully.")

#=============Additional Configuration==================
# Show Balance From Self Service
Balance_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[2]")
Balance_dropdown.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[contains(text(),'Yes')])[1]").click()
print("'Show Balance From Self Service' set to 'Yes'.")

# Apply From Self Service
Apply_self_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[3]")
Apply_self_dropdown.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[contains(text(),'Yes')])[2]").click()
print("'Apply From Self Service' set to 'Yes'.")

# Leave Rounding Type
Round_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[4]")
Round_dropdown.click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(),'No Round')]").click()
time.sleep(2)
print("'Leave Rounding Type' set to 'No Round'.")

# Leave Application Time
Apply_time = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[5]")
Apply_time.click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(),'Apply Anytime')]").click()
time.sleep(2)
print("'Leave Application Time' set to 'Apply Anytime'.")

# Attachment Mandatory
Attachment_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-form-item-control-input-content'])[6]")
Attachment_dropdown.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[contains(text(),'Yes')])[3]").click()
time.sleep(2)
print("'Attachment Mandatory' set to 'Yes'.")

# Attachment Mandatory After consuming (Min Days)
Min_days_input = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_attachmentMandatoryAfter']")
Min_days_input.click()
Min_days_input.send_keys(Keys.CONTROL, 'a')
Min_days_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
Min_days_input.send_keys("3")
time.sleep(2)
print("'Attachment Mandatory After consuming (Min Days)' set to 3.")

# Max. Leave Application in Lapse
Lapse_input = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_maxLeaveApplyInLapse']")
Lapse_input.click()
Lapse_input.send_keys(Keys.CONTROL, 'a')
Lapse_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
Lapse_input.send_keys("5")
time.sleep(2)
print("'Max. Leave Application in Lapse' set to 5.")

# Max. Leave Apply Days (Monthly)
Monthly_input = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_maxLeaveApplyMonthly']")
Monthly_input.click()
Monthly_input.send_keys(Keys.CONTROL, 'a')
Monthly_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
Monthly_input.send_keys("3")
time.sleep(2)
print("'Max. Leave Apply Days (Monthly)' set to 3.")

# Max. Leave Apply Days (At a Time)
Max_at_time_input = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_minLeaveApplyDays']")
Max_at_time_input.click()
Max_at_time_input.send_keys(Keys.CONTROL, 'a')
Max_at_time_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
Max_at_time_input.send_keys("3")
time.sleep(2)
print("'Max. Leave Apply Days (At a Time)' set to 3.")

# Min. Leave Apply Days (At a Time)
Min_at_time_input = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_minLeaveInApplication']")
Min_at_time_input.click()
Min_at_time_input.send_keys(Keys.CONTROL, 'a')
Min_at_time_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
Min_at_time_input.send_keys("1")
time.sleep(2)
print("'Min. Leave Apply Days (At a Time)' set to 1.")

# # Save Button Click
# Save_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
# Save_btn.click()
# time.sleep(4)
# print("Configuration saved successfully.")

#================Navigate to Logout===============
# Navigate to Homepage
Home_icon = driver.find_element(By.XPATH, "//div[@class='logo-img']")
Home_icon.click()
time.sleep(4)
print("Navigated to homepage successfully.")

# Locate the Profile button and click it
Profile_icon = driver.find_element(By.XPATH, "//span[@class='profile-menu-img']//img[1]")
Profile_icon.click()
time.sleep(3)
print("Clicked on Profile Successfully.")

# Logout from the application
Logout_button = driver.find_element(By.XPATH, "(//ul[@class='profile-popup-list']//li)[3]")
Logout_button.click()
time.sleep(3)
print("Logout successfully.")

# Close the browser
driver.quit()
print("WebDriver session End.")