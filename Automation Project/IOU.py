import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

##........................................................logIn Feature Start
# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("dailystar@ibos.io")
# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("dailystar@ibos")
# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()
##.........................................................Main Landing Page
# Verify dashboard visibility
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Dashboard']")))
assert dashboard_element.is_displayed(), "Login failed or dashboard not found."
print("Login successful, dashboard is visible.")
##.........................................................Login Feature Finish

##.........................................................IOU Process
#Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
time.sleep(2)
print("Clicked on Employee Management")

#.....................IOU Menu Click
ioumenu = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='IOU']")))
ioumenu.click()
time.sleep(2)
print("IOU Menu Click")

#....................IOU Application
iou_application = driver.find_element(By.XPATH,"//a[@href='/profile/iOU/application']")
iou_application.click()
time.sleep(2)
print("IOU Application Menu click")

#...........Request Expense button click
request_expense = driver.find_element(By.XPATH,"//span[text()='Request IOU']")
request_expense.click()
time.sleep(2)

#........................Employee Select
# Read employee IDs from a file
file_name = "employee_ids.txt"
with open(file_name, "r") as file:
    employee_ids = [line.strip() for line in file if line.strip()]
# Select a single random employee
random_employee = random.choice(employee_ids)
# Wait until the employee input field is clickable
wait = WebDriverWait(driver, 10)
selectemp = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_employee']")))
selectemp.click()
time.sleep(1)  # Shorter sleep time for efficiency
# Clear the input field first (ensuring only one ID is entered)
selectemp.clear()
time.sleep(1)
# Enter the selected employee ID
selectemp.send_keys(random_employee)
time.sleep(1)  # Allow time for suggestions to load
# Press ENTER to confirm selection
selectemp.send_keys(Keys.ENTER)
time.sleep(1)
print(f"Selected employee: {random_employee}")

#..................Generate a random IOU Amount
#random_amount = random.randint(500, 2000)
random_amount = random.randint(5, 20) * 100  # Generates numbers like 500, 600, ..., 2000
# Locate and interact with the IOU amount input field
iouamount = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_amount']")
iouamount.click()
time.sleep(2)  # Shorter sleep time for efficiency
iouamount.send_keys(str(random_amount))
time.sleep(2)
print(f"IOU amount: {random_amount}/= added successfully")

#From date
driver.find_element(By.XPATH,"(//input[@id='PeopleDeskForm_fromDate'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[text()='Today'])[1]").click()
time.sleep(2)

# # To Date
# driver.find_element(By.XPATH,"(//input[@id='PeopleDeskForm_toDate'])[2]").click()
# time.sleep(2)
# to_date.send_keys("20/02/2025")
# to_date.send_keys(Keys.ENTER)
# time.sleep(3)

#Description
description = driver.find_element(By.XPATH,"//textarea[@class='ant-input']")
description.click()
time.sleep(2)
description.send_keys("IOU Test.")
time.sleep(2)

#Upload Attachment
upload_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Upload Attachment')])[1]")
time.sleep(2)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(r"C:\Users\ibos\Downloads\Image\E-Mail-Signature-14_iBOS.png")
time.sleep(5)

#Submit Button Click
submitbutton = driver.find_element(By.XPATH,"//span[text()='Submit']")
submitbutton.click()
time.sleep(3)

#Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(3)
print("Navigated to homepage successfully.")

#Approval
Approval = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Approval']")))
Approval.click()
time.sleep(2)
print("Clicked on Approval")

#Expense Application Approval Click
expenseapproval = wait.until(EC.element_to_be_clickable((By.XPATH,"//p[text()='IOU']")))
expenseapproval.click()
time.sleep(3)

#checkbox select
checkbox = driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")
checkbox.click()
time.sleep(2)
print("Checkbox Selected")

#Approve button click
approve = driver.find_element(By.XPATH,"//button//span[text()='Approve']")
approve.click()
print("Approve button click")
time.sleep(2)

#Confirm button click
approve = driver.find_element(By.XPATH,"//span[normalize-space()='Yes']")
approve.click()
time.sleep(2)
print("Confirmation button click")

# Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(3)
print("Navigated to homepage successfully.")

#Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
time.sleep(2)
print("Clicked on Employee Management")

#IOU Menu Click
ioumenu = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='IOU']")))
ioumenu.click()
time.sleep(3)
print("IOU Menu Click")

#IOU Application
iouapplication = driver.find_element(By.XPATH,"//a[@href='/profile/iOU/application']")
iouapplication.click()
time.sleep(5)
print("IOU Application Menu click")

#Approved Status Button Click
approvedbutton = driver.find_element(By.XPATH, "(//span[normalize-space()='Approved'])[1]")
# Scroll left to right before clicking the button
driver.execute_script("arguments[0].scrollIntoView({inline: 'end', behavior: 'smooth'});", approvedbutton)
time.sleep(3)
# Click the approved button
approvedbutton.click()
time.sleep(2)
print("Approved Status Button Clicked Successfully.")

#Click on Edit Button
editbutton = driver.find_element(By.XPATH,"//button[normalize-space()='Edit']")
editbutton.click()
time.sleep(3)
print("Edit Button Clicked Successfully.")

# Define the random amount as adjusted amount
adjusted_amount = random_amount  # Keeping it the same as IOU amount

# # Locate and interact with the Adjusted Amount input field
# adjustamount = driver.find_element(By.XPATH, "//input[@name='adjustedAmount']")
# adjustamount.click()
# time.sleep(2)
# adjustamount.send_keys(str(adjusted_amount))
# time.sleep(2)
# print(f"Adjusted amount: {adjusted_amount}/= added successfully")

# Split adjusted_amount into 60:40 ratio
adjustment_amount_60 = int(adjusted_amount * 0.6)  # 60% of adjusted amount
return_amount_40 = adjusted_amount - adjustment_amount_60  # 40% remainder

# Locate and interact with the Adjusted Amount input field (60%)
adjustamount = driver.find_element(By.XPATH, "//input[@name='adjustedAmount']")
adjustamount.click()
time.sleep(2)
adjustamount.send_keys(str(adjustment_amount_60))  # Inputting 60% of adjusted amount
time.sleep(2)
print(f"Adjusted Amount: {adjustment_amount_60}/= added successfully.")

# Locate and interact with the Pending Amount (Return Amount) input field (40%)
pending_amount = driver.find_element(By.XPATH, "//input[@name='pendingAmount']")
pending_amount.click()
time.sleep(2)
pending_amount.send_keys(str(return_amount_40))  # Inputting 40% of adjusted amount
time.sleep(2)
print(f"Return Amount (Pending Amount): {return_amount_40}/= added successfully.")

#Upload Attachment
upload_button = driver.find_element(By.XPATH, "//span[normalize-space()='Upload files']")
time.sleep(2)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(r"C:\Users\ibos\Downloads\Image\Demo_payslip.jpg")
time.sleep(5)

#Save Button Click
savebutton = driver.find_element(By.XPATH,"//button[normalize-space()='Save']")
savebutton.click()
time.sleep(5)
print("Save Button Clicked Successfully.")

#Back To IOU Landiing Page
backbutton = driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1yxmbwk']")
backbutton.click()
time.sleep(2)
print("Navigate To IOU Landing Page.")

# Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(3)
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
time.sleep(5)

# Close the browser
driver.quit()
print("WebDriver session End.")