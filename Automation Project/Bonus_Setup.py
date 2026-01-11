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

#=============Go TO Bonus Setup=================
#Adminstration
Adminstration = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Administration']"))).click()
time.sleep(3)
print("Adminstration Module Click.")

#Payroll Configaration
Payroll_Configuration = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sidebar-dropdown sidebar-second-dropdown'][normalize-space()='Payroll Configuration']")))
Payroll_Configuration.click()
time.sleep(2)
print("Payroll Configuration Click.")

#Bonus Setup
Bonus_Setup = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Bonus Setup']")))
Bonus_Setup.click()
time.sleep(2)
print("Bonus Setup Click.")

#============Create Bonus Policy=================
#Click on Bonus Create Button
Create_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create']")))
Create_Button.click()
time.sleep(2)
print("Create Button Clicked.")

# Add Bonus Name
Add_Bonus = wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'])[21]")))
Add_Bonus.click()
time.sleep(2)
# Enter Bonus Name
Bonus_Name = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='PeopleDeskForm_bonusName'])[2]")))
Bonus_Name.send_keys("Special Religious Bonus")
time.sleep(2)
Submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Submit']")))
print("Bonus Name Entered.")

# Select Bonus Name
Bonus_Name_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='bonusName']//span[@class='ant-select-selection-item']")))
Bonus_Name_Select.click()
time.sleep(2)
Bonus_Name_Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Special Religious Bonus')]")))
Bonus_Name_Select.click()
time.sleep(2)
print("Bonus Name Selected.")

#Select Workplace
Workplace = wait.until(EC.element_to_be_clickable((By.XPATH, "///div[@name='workplace']//span[@class='ant-select-selection-item']")))
Workplace.click()
time.sleep(2)
Workplace_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ant-select-item-option-content')][normalize-space()='PeopleDesk Demo']")))
Workplace_Option.click()
time.sleep(2)
print("Workplace Selected.")

#Bonus Depend On
Bonus_Depend_On = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@name,'bounsDependOn')]//span[contains(@class,'ant-select-selection-item')]")))
Bonus_Depend_On.click()
time.sleep(2)
Bonus_Depend_On_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Gross')]")))
Bonus_Depend_On_Option.click()
time.sleep(2)
print("Bonus Depend On Selected.")

#Bonus Percentage
Bonus_Percentage = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_bonusPercentage']")))
Bonus_Percentage.send_keys("25")
time.sleep(2)
print("Bonus Percentage Entered.")

#Service Length Type
Service_Length_Type = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='serviceLengthType']//div[@class='ant-select-selector']")))
Service_Length_Type.click()
time.sleep(2)
Service_Length_Type_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Month')]")))
Service_Length_Type_Option.click()
time.sleep(2)
print("Service Length Type Selected.")

#Minimum Service Length
Minimum_Service_Length = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_minServiceLengthMonth']")))
Minimum_Service_Length.send_keys("0")
time.sleep(2)
print("Minimum Service Length Entered.")

#Maximum Service Length
Maximum_Service_Length = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_maxServiceLengthMonth']")))
Maximum_Service_Length.send_keys("9999")
time.sleep(2)
print("Maximum Service Length Entered.")

#HR Position
HR_Position = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selection-overflow'])[1]")))
HR_Position.click()
time.sleep(2)
HR_Position_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Executive')]")))
HR_Position_Option.click()
time.sleep(2)
print("HR Position Selected.")

#Employment Type
Employment_Type = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selection-overflow'])[2]")))
Employment_Type.click()
time.sleep(2)
Employment_Type_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Permanent')]")))
Employment_Type_Option.click()
time.sleep(2)
print("Employment Type Selected.")

#Religion
Religion = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ant-select-selection-overflow'])[3]")))
Religion.click()
time.sleep(2)
Religion_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Islam')]")))
Religion_Option.click()
time.sleep(2)
print("Religion Selected.")

#Add Button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
Add_Button.click()
time.sleep(3)
print("Add Button Clicked.")

#Save Button Click
Save_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']")))
Save_Button.click()
time.sleep(2)
print("Bonus Policy Created Successfully.")

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




























