import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")  # Open browser in maximized mode
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://devapp.peopledesk.io/")

# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

##logIn Feature

# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("peopledeskdemo@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("12345")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()

#Conpensation & Benefits
compen = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Compensation & Benefits']")))
compen.click()
time.sleep(2)
print("Conpensation & Benefits Menu Clicked Successfully")

#CLick on Payroll
Payroll = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Payroll']")))
Payroll.click()
time.sleep(2)
print("Payroll Clicked Successfully")

# CLick on Salary Generate
Salary_Generate = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Salary Generate']")))
Salary_Generate.click()
time.sleep(2)
print("Salary Generate Clicked Successfully")

#Click on salary Code
salary_code = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//p[text()='SAL-20251204']")))
salary_code.click()
time.sleep(2)
print("Click on the salary code")

#Click on details
details = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Details']")))
details.click()
time.sleep(10)
print("Click on details")

# Scroll the "Signature" element into view
signature_element = driver.find_element(By.XPATH, "//div[text()='Signature']")
driver.execute_script("arguments[0].scrollIntoView(true);", signature_element)
time.sleep(8)
print("Scrolled horizontally to the Right.")

#Click on Salary_PaySlip
Salary_PaySlip = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Salary PaySlip']")))
Salary_PaySlip.click()
time.sleep(5)
print("Click on the Salary_PaySlip")

#Click on PaySlip
PaySlip = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='PaySlip']")))
PaySlip.click()
time.sleep(5)
print("Click on the PaySlip")

#month
month = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='month']")))
month.click()
month.send_keys("January")
time.sleep(2)
month.send_keys(Keys.TAB)
time.sleep(2)
month.send_keys("2025")
time.sleep(2)
print("Payroll Month Selected")

#Employee
Employee = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-2-input']")))
Employee.click()
time.sleep(3)
Employee.send_keys("Anika")
time.sleep(2)
Employee.send_keys(Keys.ENTER)
time.sleep(2)
print("Employee Selected")

#Salary Code
salary_code = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='react-select-peopleDesk-input']")))
salary_code.click()
time.sleep(2)
salary_code.send_keys("SAL-20251204")
time.sleep(2)
salary_code.send_keys(Keys.ENTER)
print("Salary Code Entered Selected")

#View Button Click
view_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='View']")))
view_button.click()
time.sleep(3)
print("View button is clicked")

# #Click on download button
# pyautogui.moveTo(545, 271)  # Coordinates for the Print button; adjust them as per your screen
# pyautogui.click()
# time.sleep(3)
# print("PDF printed successfully")
#
# pyautogui.moveTo(591, 555)  # Coordinates for the Save button; adjust them as per your screen
# pyautogui.click()
# print("Save button clicked")

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


