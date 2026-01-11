import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Initialize Edge WebDriver with options
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("start-maximized")  # Open Edge browser in maximized mode.
# Launch Edge browser with specified options
driver = webdriver.Edge(options=edge_options)

## Initialize Chrome WebDriver with options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("start-maximized")  # Open Chrome browser in maximized mode.
# # Launch Chrome browser with specified options
# driver = webdriver.Chrome(options=chrome_options)

## Open the website
driver.get("https://devapp.peopledesk.io/")

# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}.")

##..............................LogIn Feature
# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("dailystar@ibos.io")
# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("dailystar@ibos")
# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()
# Verify dashboard visibility
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Dashboard']")))
assert dashboard_element.is_displayed(), "Login failed or dashboard not found."
print("Login successful, dashboard is visible.")
## ............................Login Feature Finish

##...............................Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
time.sleep(2)
print("Clicked on Employee Management.")

##..............................Expense Menu Click
expensemenu = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Expense']")))
expensemenu.click()
time.sleep(2)
print("Expense Menu Clicked.")

## Expense Application Menu
expenseapplication = driver.find_element(By.XPATH,"//a[text()='Expense Application']")
expenseapplication.click()
time.sleep(2)
print("Expense Application Menu clicked.")

## Request Expense button click
requestexpense = driver.find_element(By.XPATH,"//span[text()='Request Expense']")
requestexpense.click()
time.sleep(2)
print("'Request Expense' Button clicked successfully.")

## Create Expense Type
# createexpensebutton =driver.find_element(By.XPATH,"//span[@aria-label='plus-circle']//*[name()='svg']")
# createexpensebutton.click()
# time.sleep(2)
#
# createexpensetype = driver.find_element(By.XPATH,"//input[@id='PeopleDeskForm_expenseType']")
# createexpensetype.click()
# createexpensetype.send_keys("Allowance")
# time.sleep(2)
#
# addbutton = driver.find_element(By.XPATH,"//button//span[text()='Add']")
# addbutton.click()
# time.sleep(2)

## Expense Type
expensetype = driver.find_element(By.XPATH,"//input[@id='PeopleDeskForm_expenseTypeDDL']")
expensetype.click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[contains(text(),'Demo Test')]").click()  
time.sleep(2)
print("Expense Type selected successfully.")

## List of employees
# employee_ids = ["EMP96743", "EMP54272", "EMP34614", "EMP60193", "EMP22884", "E-123456789", "1601", "3898", "3896", "61228", "61197", "61196", "61195", "61182", "61181", "61226", "61225", "61224", "61223", "61222", "61221", "61220", "61219", "61218", "61217", "61216", "3501", "1001", "1819", "1818", "1817", "1816", "1814", "1813", "1811", "1805", "1804", "1803", "1554", "1548", "1600", "1599", "1598", "1587", "1583", "1579", "1577", "1576", "1575", "1537", "1514", "1506", "1368", "2604", "2601", "1810", "1809", "1723", "1722", "1721", "1720", "1719", "1717", "1716", "1714", "1710", "1709", "1707", "1702", "1511", "1340", "1115", "2802", "2303", "2203", "1573", "1572", "1568", "1564", "1563", "1562", "1561", "1560", "1555", "1552", "1542", "1540", "1538", "1031", "2010", "2008", "1801", "1380", "1379", "1377", "1376", "1375", "1374", "1373", "1372", "1370", "1366", "1365", "1364", "1363", "1362", "1361", "1357", "1356", "1346", "1344", "1342", "1337", "1335", "1327", "1323", "1319", "1318", "1317", "1315", "1314", "1313", "1311", "1310", "1307", "1305", "3131", "3128", "3127", "3125", "3124", "3122", "3120", "3119", "3118", "3116", "3114", "3104", "3102", "3008", "3007", "3006", "3004", "3003", "3002", "3854", "2509", "2313", "2003", "1597", "1596", "1592", "1586", "1580", "1571", "1545", "1507", "1505", "1504", "1320", "1164", "1163", "1161", "1159", "1158", "1157", "1155", "1153", "1152", "1151", "1148", "1132", "1126", "1120", "1119", "1117", "1112", "1109", "1107", "1106", "1103", "1102", "1003", "2115", "2707", "2705", "3011", "2916", "2915", "2914", "2912", "2911", "2907", "2906", "2904", "1528", "1526", "3708", "3707", "3655", "3654", "3653", "3651", "3648", "3647", "3646", "3645", "3644", "3643", "3642", "3616", "3608", "1914", "1912", "1911", "1910", "1908", "1907", "1905", "1904", "1903", "1902", "1901", "1549", "3530", "3529", "3528", "3527", "3525", "3520", "3514", "3507", "3506", "3505", "3504", "2810", "2809", "2808", "2515", "2513", "2512", "2506", "2415", "2414", "2413", "2409", "2207", "2202", "2114", "2110", "2108", "2105", "2102", "2009", "1034", "1033", "1032", "1030", "1028", "1026", "1018", "1005", "1595", "1594", "1593", "1584", "1544", "1543", "1021", "3518", "3404", "3403", "3401", "3894", "3893", "3892", "3891", "3890", "3888", "3887", "3885", "3884", "3883", "3879", "3876", "3875", "3872", "3871", "3866", "3863", "3861", "3856", "3855", "3846", "3844", "3831", "3825", "3823", "3822", "3816", "3814", "3813", "3807", "3804", "3517", "1006", "2320", "2319", "2318", "2315", "2314", "2305", "2208", "3704", "10591"]
# random_employee = random.choice(employee_ids)  # Pick a random employee

##........................Employee Select
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

## Generate a random Expense Amount
random_amount = random.randint(500, 2000)
# Locate and interact with the IOU amount input field
expenseamount = driver.find_element(By.XPATH, "//input[@id='PeopleDeskForm_amount']")
expenseamount.click()
time.sleep(2)  # Shorter sleep time for efficiency
expenseamount.send_keys(str(random_amount))
time.sleep(2)
print(f"Expense amount: {random_amount}/= added successfully.")

## From date
driver.find_element(By.XPATH,"(//input[@id='PeopleDeskForm_fromDate'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[text()='Today'])[1]").click()
time.sleep(2)

## To Date
# driver.find_element(By.XPATH,"(//input[@id='PeopleDeskForm_toDate'])[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[text()='Today'])[1]").click()
# time.sleep(2)

## Description
description = driver.find_element(By.XPATH,"//textarea[@class='ant-input']")
description.click()
time.sleep(2)
description.send_keys("Test Allowance.")
time.sleep(2)

## Upload Button
upload_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Upload Attachment')])[1]")
time.sleep(2)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(r"C:\Users\ibos\Downloads\Image\Demo_payslip.jpg")
time.sleep(5)

## Submit Button Click
submitbutton = driver.find_element(By.XPATH,"//span[text()='Submit']")
submitbutton.click()
time.sleep(2)

## Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")

## Approval
approval = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Approval']")))
approval.click()
time.sleep(2)
print("Clicked on Approval.")

## Expense Application Approval Click
expense_approval = wait.until(EC.element_to_be_clickable((By.XPATH,"//p[text()='Expense Application']")))
expense_approval.click()
time.sleep(3)

#Selected Random Employee Search In Approval
search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search...']")))
search.send_keys(random_employee)
search.send_keys(Keys.ENTER)
time.sleep(2)
print("The Specific Employee Was Found.")

## Checkbox select
check_box = driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")
check_box.click()
time.sleep(3)
print("Checkbox Selected successfully.")

## Approve button click
approve = driver.find_element(By.XPATH,"//button//span[text()='Approve']")
approve.click()
time.sleep(2)
print("Approve button clicked.")

## Confirm button click
approve = driver.find_element(By.XPATH,"//span[normalize-space()='Yes']")
approve.click()
time.sleep(2)
print("Confirmation button clicked.")

## Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")

## Employee management
employee_management = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Employee Management']")))
employee_management.click()
time.sleep(2)
print("Clicked on Employee Management.")

## Expense Menu Click
expensemenu = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Expense']")))
expensemenu.click()
time.sleep(2)
print("Expense Menu Clicked.")

## Expense Application Menu
expenseapplication = driver.find_element(By.XPATH,"//a[text()='Expense Application']")
expenseapplication.click()
time.sleep(2)
print("Expense Application Menu clicked.")

## Approved Expense Application Check
approved_application = driver.find_element(By.XPATH,"(//div[@class='d-flex align-items-center'])[2]")
approved_application.click()
time.sleep(5)
print("Approved Application checked.")

## Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")

## Locate the Profile button and click it
profile_xpath = "//span[@class='profile-menu-img']//img[1]"
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, profile_xpath)))
profile_button.click()
print("Clicked on Profile Successfully.")
time.sleep(2)

## Logout from the application
logout_xpath = "(//ul[@class='profile-popup-list']//li)[3]"  # Update with the correct XPath
logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logout_xpath)))
logout_button.click()
print("Logout successfully.")
time.sleep(6)

## Close the browser
driver.quit()
print("WebDriver session End.")