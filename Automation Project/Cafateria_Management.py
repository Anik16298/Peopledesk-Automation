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

#============Go to Cafateria Management==================
# Cafateria Management
Cafateria_Management = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sidebar-dropdown sidebar-second-dropdown'][normalize-space()='Cafeteria Management']")))
Cafateria_Management.click()
time.sleep(2)
print("Successfully clicked on Cafateria Management")

# Cafateria Pricing Setup
Cafateria_Pricing_Setup = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Cafeteria Pricing Setup']")))
Cafateria_Pricing_Setup.click()
time.sleep(2)
print("Successfully clicked on Cafateria Pricing Setup")

# SETUP PRICING Button Click
Cafateria_Pricing_Setup_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Setup Pricing']")))
Cafateria_Pricing_Setup_Button.click()
time.sleep(2)
print("Successfully clicked on Cafateria Pricing Setup Button")

# Enter Meal Type
Meal_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_mealType']")))
Meal_Type.click()
time.sleep(2)
Per_month_meal = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Per Month')]")))
Per_month_meal.click()
time.sleep(2)
print("Successfully selected Meal Type")

# Select Month
Month = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_date']")))
Month.click()
time.sleep(2)
Month_select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='May']")))
Month_select.click()
time.sleep(2)
print("Successfully selected Month")

# Workplace Group Selection
Workplace_Group = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_workplaceGroup']")))
Workplace_Group.click()
time.sleep(2)
Workplace_group_select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='PeopleDesk Demo']")))
Workplace_group_select.click()
time.sleep(2)
print("Successfully selected Workplace Group")

# Workplace Selection
Workplace = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_workplace']")))
Workplace.click()
time.sleep(2)
Workplace_select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-item ant-select-item-option ant-select-item-option-active']//div[@class='ant-select-item-option-content'][normalize-space()='PeopleDesk Demo']")))
Workplace_select.click()
time.sleep(2)
print("Successfully selected Workplace")

# Pricing Matrix Type
Pricing_Matrix_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_pricingMatrixType']")))
Pricing_Matrix_Type.click()
time.sleep(2)
Pricing_Matrix_Type_select = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Salary Range Wise')]")))
Pricing_Matrix_Type_select.click()
time.sleep(2)
print("Successfully selected Pricing Matrix Type")

# "ADD" Button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
Add_Button.click()
time.sleep(2)
print("Successfully clicked on 'Add' button")

# Salary Range Min
Salary_Range_Min = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[1]")))
Salary_Range_Min.send_keys("1")
time.sleep(2)
print("Successfully entered Salary Range Min")

# Salary Range Max
Salary_Range_Max = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[2]")))
Salary_Range_Max.send_keys("25000")
time.sleep(2)
print("Successfully entered Salary Range Max")

# Own Contribution/Meal
Own_Contribution_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[3]")))
Own_Contribution_Meal.send_keys("750")
time.sleep(2)
print("Successfully entered Own Contribution/Meal")

# Company Contribution/Meal
Company_Contribution_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[4]")))
Company_Contribution_Meal.send_keys("750")
time.sleep(2)
print("Successfully entered Company Contribution/Meal")

# Own Contribution for Guest/Meal
Own_Contribution_Guest_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[5]")))
Own_Contribution_Guest_Meal.send_keys("750")
time.sleep(2)
print("Successfully entered Own Contribution for Guest/Meal")

# Company Contribution for Guest/Meal
Company_Contribution_Guest_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[6]")))
Company_Contribution_Guest_Meal.send_keys("0")
time.sleep(2)
print("Successfully entered Company Contribution for Guest/Meal")

# "ADD" Button Click
Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
Add_Button.click()
time.sleep(2)
print("Successfully clicked on 'Add' button")

# Salary Range Min
Salary_Range_Min = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[7]")))
Salary_Range_Min.send_keys("25001")
time.sleep(2)
print("Successfully entered Salary Range Min")

# Salary Range Max
Salary_Range_Max = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[8]")))
Salary_Range_Max.send_keys("1000000")
time.sleep(2)
print("Successfully entered Salary Range Max")

# Own Contribution/Meal
Own_Contribution_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[9]")))
Own_Contribution_Meal.send_keys("1000")
time.sleep(2)
print("Successfully entered Own Contribution/Meal")

# Company Contribution/Meal
Company_Contribution_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[10]")))
Company_Contribution_Meal.send_keys("1000")
time.sleep(2)
print("Successfully entered Company Contribution/Meal")

# Own Contribution for Guest/Meal
Own_Contribution_Guest_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[11]")))
Own_Contribution_Guest_Meal.send_keys("1000")
time.sleep(2)
print("Successfully entered Own Contribution for Guest/Meal")

# Company Contribution for Guest/Meal
Company_Contribution_Guest_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Amount'])[12]")))
Company_Contribution_Guest_Meal.send_keys("0")
time.sleep(2)
print("Successfully entered Company Contribution for Guest/Meal")

#Save Button Click
Save_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']")))
Save_Button.click()
time.sleep(2)
print("Successfully clicked on 'Save' button")

#=============Food Corner==================
#Food Corner
Food_Corner = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Food Corner']")))
Food_Corner.click()
time.sleep(2)
print("Successfully clicked on Food Corner")

#=============Meal Requisition==================
# Employee Name
Employee_Name = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class=' css-18w4uv4'])[1]")))
Employee_Name.click()
time.sleep(2)
input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='react-select-2-input']")))
input_box.send_keys("KF007")
time.sleep(3)
input_box.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully entered Employee Name")

# Number of Meal
Number_of_Meal = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='meal'])[1]")))
Number_of_Meal.click()
Number_of_Meal.send_keys(Keys.CONTROL, 'a')
Number_of_Meal.send_keys(Keys.BACKSPACE)
Number_of_Meal.send_keys("1")
time.sleep(2)
print("Successfully entered Number of Meal")

#Meal Status
Meal_Status = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='own']")))
Meal_Status.click()
time.sleep(2)
print("Successfully selected Meal Status as 'Own'")

# Date
Date = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='date'])[1]")))
Date.click()
time.sleep(2)
# Select today's date
today = time.strftime("%d")
month = time.strftime("%m")
year = time.strftime("%Y")
Date.send_keys(today + month + year)
time.sleep(2)
print("Successfully selected Date")

# Remarks
Remarks = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='remarks']")))
Remarks.click()
Remarks.send_keys("Test Meal Requisition.")
time.sleep(2)
print("Successfully entered Remarks")

# Save Button click
Save_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
Save_Button.click()
time.sleep(2)
print("Successfully clicked on Save Button")

#=============Details Report(Daily)==================
# Details Report
Details_Report = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Details Report']")))
Details_Report.click()
time.sleep(2)
print("Successfully clicked on Details Report")

#Report type
Report_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='reportType']//div[@class='ant-select-selector']")))
Report_Type.click()
time.sleep(2)
Report_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Daily')]")))
Report_Type.click()
time.sleep(2)
print("Successfully selected Report Type as 'Daily'")

# Date
Date = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='PeopleDeskForm_fromDate']")))
Date.click()
Date.send_keys(Keys.CONTROL, 'a')
Date.send_keys(Keys.BACKSPACE)
time.sleep(2)
# Select today's date
today = time.strftime("%d")
Date.send_keys(today)
Date.send_keys(Keys.ENTER)
time.sleep(2)
print("Successfully selected Date for Report")

# View button Click
View_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='View']")))
View_Button.click()
time.sleep(5)
print("Successfully clicked on View Button")

# #=============Details Report(Monthly)==================
# #Report type
# Report_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='reportType']//div[@class='ant-select-selector']")))
# Report_Type.click()
# time.sleep(2)
# Report_Type = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Monthly')]")))
# Report_Type.click()
# time.sleep(2)
# print("Successfully selected Report Type as 'Daily'")
#
# # From Date
# From_Date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_fromDate']")))
# From_Date.send_keys(Keys.CONTROL, 'a')
# From_Date.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# From_Date.send_keys("01/05/25")
# time.sleep(2)
# From_Date.send_keys(Keys.ENTER)
# time.sleep(2)
# print("Successfully selected From Date for Report")
#
# # To Date
# To_Date = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='PeopleDeskForm_toDate']")))
# time.sleep(1)
# To_Date.send_keys("30/05/25")
# time.sleep(2)
# To_Date.send_keys(Keys.ENTER)
# time.sleep(2)
# print("Successfully selected To Date for Report")
#
# # View button Click
# View_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='View']")))
# View_Button.click()
# time.sleep(4)
# print("Successfully clicked on View Button")

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
Logout_button = driver.find_element(By.XPATH, "(//ul[@class='profile-popup-list']//li)[3]")  # Update XPath if needed
Logout_button.click()
time.sleep(3)
print("Logout successfully.")

# Close the browser
driver.quit()
print("WebDriver session End.")
























