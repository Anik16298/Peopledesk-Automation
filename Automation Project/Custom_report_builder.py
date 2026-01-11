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

#============Go to Employee Management==================
# Employee Management
Employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
Employee_management.click()
time.sleep(2)
print("Successfully clicked on Employee Management")

#============Go to Custom Report Builder==================
#Reports Builder
Reports_Builder = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sidebar-dropdown sidebar-second-dropdown'][normalize-space()='Reports Builder']")))
Reports_Builder.click()
time.sleep(2)
print("Successfully clicked on Reports Builder")

#Custom Report Builder
Custom_Report_Builder = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Custom Report Builder']")))
Custom_Report_Builder.click()
time.sleep(2)
print("Successfully clicked on Custom Report Builder")

#Select Column
Business_Unit = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Business Unit']")))
Business_Unit.click()
time.sleep(2)
Workplace_Group = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Workplace Group']")))
Workplace_Group.click()
time.sleep(2)
Workplace = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Workplace']")))
Workplace.click()
time.sleep(2)
Employee_Code = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Employee Code']")))
Employee_Code.click()
time.sleep(2)
Employee_Name = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Employee Name']")))
Employee_Name.click()
time.sleep(2)
Department = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Department']")))
Department.click()
time.sleep(2)
Designation = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Designation']")))
Designation.click()
time.sleep(2)
Employment_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Employment Type']")))
Employment_type.click()
time.sleep(2)
HR_Position = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='HR Postion']")))
HR_Position.click()
time.sleep(2)
Gender = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Gender']")))
Gender.click()
time.sleep(2)
Religion = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Religion']")))
Religion.click()
time.sleep(2)
Blood_Group = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Blood Group']")))
Blood_Group.click()
time.sleep(2)
Birthday = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Birthday']")))
Birthday.click()
time.sleep(2)
Employee_Address = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Employee Address']")))
Employee_Address.click()
time.sleep(2)
Office_Mail = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Office Mail']")))
Office_Mail.click()
time.sleep(2)
Office_Mobile = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Office Mobile']")))
Office_Mobile.click()
time.sleep(2)
print("Successfully selected columns.")

# # Click on the "View" button
# View_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View']")))
# View_Button.click()
# time.sleep(3)
# print("Successfully clicked on View button.")

#Download Excel
Excel_Download = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Export CSV']//*[name()='svg']")))
Excel_Download.click()
time.sleep(5)
x, y = 636, 448
pyautogui.click(x, y)
time.sleep(5)
print("Excel file downloaded successfully.")

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





