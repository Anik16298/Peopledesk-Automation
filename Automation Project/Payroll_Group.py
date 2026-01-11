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

#============Go to Payroll Element==================
#Adminstration
Adminstration = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Administration']"))).click()
time.sleep(3)
print("Adminstration Module Click.")

#Payroll Configuration
Payroll_Configuration = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sidebar-dropdown sidebar-second-dropdown'][normalize-space()='Payroll Configuration']")))
Payroll_Configuration.click()
time.sleep(2)
print("Payroll Configuration Click.")

#Payroll Group
Payroll_Group = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Payroll Group']")))
Payroll_Group.click()
time.sleep(2)
print("Payroll Group Click.")

#============Create Payroll Group=================
#Click on Payroll Group Create Button
Create_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create']")))
Create_Button.click()
time.sleep(2)

#Enter Payroll Group Name
Payroll_Group_Name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_breakdownTitle']")))
Payroll_Group_Name.click()
time.sleep(2)
Payroll_Group_Name.send_keys("Test Payroll")
time.sleep(2)
print("Payroll Group Name Entered.")

#Payroll Policy Select
Payroll_Policy_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='payrollPolicy']//div[@class='ant-select-selector']")))
Payroll_Policy_Select.click()
time.sleep(2)
Payroll_Policy_Select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'New policy')]")))
Payroll_Policy_Select.click()
time.sleep(2)
print("Payroll Policy Selected.")

#Workplace Group Select
Workplace_Group_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='payScale']//div[@class='ant-select-selector']")))
Workplace_Group_Select.click()
time.sleep(2)
Workplace_Group_Select = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[text()='PeopleDesk Demo'])[4]")))
Workplace_Group_Select.click()
time.sleep(2)
print("Workplace Group Selected.")

#Workplace Select
Workplace_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selection-overflow']")))
Workplace_Select.click()
time.sleep(2)
Workplace_Select = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[text()='PeopleDesk Demo'])[5]")))
Workplace_Select.click()
time.sleep(2)
print("Workplace Selected.")

#Depends On Select
Depends_On_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='dependsOn']//div[@class='ant-select-selector']")))
Depends_On_Select.click()
time.sleep(2)
Depends_On_Select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Basic')]")))
Depends_On_Select.click()
time.sleep(2)
print("Depends On Selected.")

#Based On Select
Based_On_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='basedOn']//div[@class='ant-select-selector']")))
Based_On_Select.click()
time.sleep(2)
Based_On_Select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Percentage')]")))
Based_On_Select.click()
time.sleep(2)
print("Based On Selected.")

#============Repeated Work==================
#Payroll Element Select
Payroll_Element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='payrollElement']//div[@class='ant-select-selector']")))
Payroll_Element.click()
time.sleep(2)
Payroll_Element_Convence = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Convence')]")))
Payroll_Element_Convence.click()
time.sleep(2)
print("Payroll Element: Convence Selected.")

#Add button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
Add_Button.click()
time.sleep(2)
print("Add Button Clicked.")

#Convence Element
Convence_Element = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@role,'spinbutton')])[1]")))
Convence_Element.send_keys("25")
time.sleep(2)
print("Convence Element Entered.")

#Payroll Element Select
Payroll_Element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='payrollElement']//div[@class='ant-select-selector']")))
Payroll_Element.click()
time.sleep(2)
Payroll_Element_Home = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Home')]")))
Payroll_Element_Home.click()
time.sleep(2)
print("Payroll Element: Home Selected.")

#Add button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
Add_Button.click()
time.sleep(2)
print("Add Button Clicked.")

#Home Element
Home_Element = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@role,'spinbutton')])[2]")))
Home_Element.send_keys("50")
time.sleep(2)
print("Home Element Entered.")

#Payroll Element Select
Payroll_Element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='payrollElement']//div[@class='ant-select-selector']")))
Payroll_Element.click()
time.sleep(2)
Payroll_Element_Medical = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Madical')]")))
Payroll_Element_Medical.click()
time.sleep(2)
print("Payroll Element: Medical Selected.")

#Add button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
Add_Button.click()
time.sleep(2)
print("Add Button Clicked.")

#Madical Element
Madical_Element = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@role,'spinbutton')])[3]")))
Madical_Element.send_keys("25")
time.sleep(2)
print("Madical Element Entered.")

#Save Button Click
Save_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']")))
Save_Button.click()
time.sleep(3)
print("Save Button Clicked.")

#============Payroll Group Created=================

time.sleep(5)

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