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

#============Go to Employee Management==================

#Employee management
Employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
Employee_management.click()
time.sleep(2)
print("Successfully clicked on Employee Management")

#Leave
Leave = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Leave']")))
Leave.click()
time.sleep(2)
print("Successfully clicked on Leave")

#Leave Application
Leave_application = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Leave Application']")))
Leave_application.click()
time.sleep(2)
print("Successfully clicked on Leave Application")

#============Apply Leave==================

#Search Employee
Search_employee = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_employee']")))
Search_employee.send_keys("KF007")
time.sleep(2)
Search_employee.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Searched Employee")

# Select Leave Type (dropdown)
Leave_type = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selector'])[3]")))
Leave_type.click()
time.sleep(2)
# Select "Casual Leave" from the dropdown
Casual_leave = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Casual Leave [CL]')]")))
Casual_leave.click()
time.sleep(2)
print("Successfully clicked 'Casual Leave'")

#Leave Consume Type
Leave_consume_type = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selector'])[4]")))
Leave_consume_type.click()
time.sleep(2)
# Select "Full Day" from the dropdown
Full_day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Full Day')]")))
Full_day.click()
time.sleep(2)
print("Successfully clicked 'Full Day'")

# From Date
From_date_div = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-picker-input'])[1]")))
From_date_div.click()
time.sleep(2)
From_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-picker-input'])[1]//input")))
From_date_input.send_keys(Keys.CONTROL, 'a')
time.sleep(1)
From_date_input.send_keys(Keys.BACKSPACE)
time.sleep(1)
# From_date_input.send_keys("21/05/2025")
From_date_input.send_keys(time.strftime("%d/%m/%Y"))
# From_date_input.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully entered 'From Date'")

# To Date
To_date_div = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-picker-input'])[2]")))
From_date_div.click()
time.sleep(2)
To_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-picker-input'])[2]//input")))
To_date_input.send_keys(Keys.CONTROL, 'a')
time.sleep(1)
To_date_input.send_keys(Keys.BACKSPACE)
time.sleep(1)
# To_date_input.send_keys("21/05/2025")
To_date_input.send_keys(time.strftime("%d/%m/%Y"))
# To_date_input.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully entered 'To Date'")

#Leave Reliver
Leave_reliver = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_leaveReliever']")))
Leave_reliver.send_keys("004")
time.sleep(3)
Leave_reliver.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered Searched Employee")

#Location
Location = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_location']")))
Location.send_keys("Test Location.")
time.sleep(2)
Location.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully Entered 'Location'")

#Leave Reason
Leave_reason = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='PeopleDeskForm_reason']")))
Leave_reason.send_keys("Test Reason.")
time.sleep(2)
print("Successfully Entered 'Leave Reason'")

# Upload an attachment
Upload_file = driver.find_element(By.XPATH, "//input[@type='file']")
time.sleep(2)
Upload_file.send_keys(r"C:\Users\ibos\Downloads\Image\Demo_payslip.jpg")
time.sleep(3)
print("Attachment uploaded successfully.")

# Click Apply button
Apply_button = driver.find_element(By.XPATH, "//span[normalize-space()='Apply 1 Day Leave']")
Apply_button.click()
time.sleep(2)
print("Submit successfully.")

#Submit Application
Submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']")))
Submit_button.click()
time.sleep(5)
print("Successfully clicked 'Yes' button")