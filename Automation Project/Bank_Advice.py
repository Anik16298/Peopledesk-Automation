import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

# Initialize Edge WebDriver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")  # Open browser in maximized mode
# Launch Chrome browser with specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://devapp.peopledesk.io/")
# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

# Locate the username field and input text
username_xpath = "//input[@placeholder='Enter your id']"
username_field = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, username_xpath)))
username_field.send_keys("01401155155")  # Replace with the desired username

# Locate the password field and input text
password_xpath = "//input[@placeholder='Enter your password']"
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
password_field.send_keys("01401155155")  # Replace with the desired password

# Locate the Login button and click it
submit_xpath = "//button[@type='submit']"
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
submit_button.click()
time.sleep(2)  # Allow the next page to load
print("Login successfully.")

# Click on the Compensation & Benefits module
compensation_benefits_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Compensation & Benefits']")))
compensation_benefits_button.click()
time.sleep(2)  # Ensure the next step is executed after the page loads
print("Compensation & Benefits module open.")

# Click on the Bank Advice sub-feature
bank_advice_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Bank Advice']")))
bank_advice_button.click()
time.sleep(2)  # Wait for the Bank Advice page to load
print("Bank Advice Feature open.")

# Payroll month field
payroll_month_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='month']")))
payroll_month_field.send_keys('April')
payroll_month_field.send_keys(Keys.TAB)
payroll_month_field.send_keys('2025')
time.sleep(2)
print("Input Month & Year Successfully.")

# Workplace Group Select
Workplace_Group = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[1]")))
Workplace_Group.click()
time.sleep(3)
Workplace_Group.send_keys("Halda Valley Food & Beverage")
time.sleep(2)
Workplace_Group.send_keys(Keys.ENTER)
time.sleep(2)
print("Workpplace Group Select Sucessfully.")

#Bank Advice For
Bank_Advice = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[2]")))
Bank_Advice.click()
Bank_Advice.send_keys("Salary")
time.sleep(2)
Bank_Advice.send_keys(Keys.ENTER)
time.sleep(2)
print("Bank Advice Selected.")

#Salary Code
Salary_Code = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[3]")))
Salary_Code.click()
time.sleep(2)
Salary_Code.send_keys("SAL-20254396")
time.sleep(2)
Salary_Code.send_keys(Keys.ENTER)
time.sleep(2)
print("Salary_Code Selected.")

#Workplace
Workplace = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[4]")))
Workplace.click()
time.sleep(2)
Workplace.send_keys("Halda Valley Food & Beverage")
time.sleep(2)
Workplace.send_keys(Keys.ENTER)
time.sleep(2)
print("Workplace Selected.")

#Bank Name
Bank_Name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[5]")))
Bank_Name.click()
time.sleep(2)
Bank_Name.send_keys("PRIME BANK LTD")
time.sleep(2)
Bank_Name.send_keys(Keys.ENTER)
time.sleep(2)
print("Bank_Name Selected.")

#Advice Type
Advice_Type = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[6]")))
Advice_Type.click()
time.sleep(2)
Advice_Type.send_keys("PRIME")
time.sleep(2)
Advice_Type.send_keys(Keys.ENTER)
time.sleep(2)
print("Advice_Type Selected.")

#Account
Account = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='react-select-peopleDesk-input'])[7]")))
Account.click()
time.sleep(2)
Account.send_keys("Halda Valley")
time.sleep(2)
Account.send_keys(Keys.ENTER)
time.sleep(2)
print("Account Selected.")

#View Button Click
view_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='View']")))
view_button.click()
time.sleep(5)
print("View button is clicked.")

# Scroll down using JavaScript
scroll_downto_bottom = driver.find_element(By.XPATH, "//span[text()='Halda Valley Food & Beverage']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_downto_bottom)
time.sleep(2)
print("Scroll down to bottom")

# Scroll Up to Download Button
scroll_upto_bottom = driver.find_element(By.XPATH, "//button[text()='Download']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_upto_bottom)
time.sleep(2)
print("Scroll upto download bottom")

#Click on download button
download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Download']")))
download_button.click()
time.sleep(3)
Top_Sheet_as_PDF = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='Top Sheet as PDF']")))
Top_Sheet_as_PDF.click()
time.sleep(3)

#For Printing
pyautogui.moveTo(1206, 758)  # Coordinates for the Save button; adjust them as per your screen
pyautogui.click()
time.sleep(5)
print("Clicked the Save button in the print dialog.")


# # Locate the Home button and click it
# home_xpath = "//div[@class='company-logo pointer']//img[1]"
# home_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, home_xpath)))
# home_button.click()
# print("Home Button Clicked Successfully.")
# time.sleep(5)
#
# # Locate the Profile button and click it
# profile_xpath = "//img[@alt='Profile']"
# profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
# profile_button.click()
# print("Clicked on Profile Successfully.")
# time.sleep(3)
#
# # Logout from the application
# logout_xpath = "//div[@id='simple-popover']//li[3]"  # Update with the correct XPath
# logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logout_xpath)))
# logout_button.click()
# print("Logout successfully.")
# time.sleep(5)
#
# # Session_End
# driver.quit()
# print("WebDriver session closed.")