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

#Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
print("Clicked on Employee Management")
time.sleep(3)

#Loan Request Menu Click
loan_request = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Loan Request']")))
loan_request.click()
time.sleep(2)

#Request loan button click
request_loan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Request Loan']")))
request_loan_button.click()
time.sleep(3)

# #Employee
# Click on the div to activate the dropdown
Employee_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Search (min 3 letter)']/following-sibling::div")))
Employee_name.click()
time.sleep(2)  # Allow dropdown to activate

# Find the actual input field inside the div
input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Search (min 3 letter)']/following-sibling::div//input")))

# Send keys to input field
input_field.send_keys("1601")
time.sleep(2)
input_field.send_keys(Keys.ENTER)
time.sleep(2)

#Loan Type
loan_type = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class=' css-18w4uv4'])[2]")))
loan_type.click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='House Loan']").click()
time.sleep(3)

#Loan Amount
Loan_ammount = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='loanAmount']")))
Loan_ammount.send_keys(10000)
time.sleep(3)

#Interest
Interest = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='interest']")))
Interest.send_keys(2)
time.sleep(3)

#Guarantor Employee
guarantor_emp = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Guarantor Employee']/following-sibling::div")))
guarantor_emp.click()
time.sleep(2)
Input = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Guarantor Employee']/following-sibling::div//input")))
time.sleep(2)
Input.send_keys(3898)
time.sleep(3)
Input.send_keys(Keys.ENTER)
time.sleep(1)
Input.send_keys(3854)
time.sleep(3)
Input.send_keys(Keys.ENTER)
time.sleep(2)

#Installation Number
installation_number = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='installmentNumber']")))
installation_number.send_keys(5)
time.sleep(3)

#Effective Month
effectivemonth = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='effectiveDate']")))
effectivemonth.click()
time.sleep(3)
march_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Mar']")))
march_option.click()
time.sleep(2)

#Description
description = wait.until(EC.element_to_be_clickable((By.XPATH,"//div//textarea[@name='description']")))
description.click()
time.sleep(2)
description.send_keys("Thank You")
time.sleep(2)

#familyGuarantor
familyGuarantor = wait.until(EC.element_to_be_clickable((By.XPATH,"//div//textarea[@name='familyGuarantor']")))
familyGuarantor.click()
time.sleep(2)
familyGuarantor.send_keys("Ishtiaque Ahmed Tanim")
time.sleep(2)

#Upload Attachment
upload_button = driver.find_element(By.XPATH, "//div[text()='Click to upload']")
time.sleep(2)
upload_button.send_keys(r"C:\Users\ishti\OneDrive\Desktop\leave.png")
time.sleep(5)