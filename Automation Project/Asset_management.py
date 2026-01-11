import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize the WebDriver for Microsoft Edge
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("start-maximized")  # Open browser in maximized mode
driver = webdriver.Edge(options=edge_options)

driver.get("https://devapp.peopledesk.io/")

# Wait for the page title (optional)
wait = WebDriverWait(driver, 20)  # Ensure `wait` is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

##logIn Feature1

# Enter user ID
wait.until( EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("peopledeskdemo@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("12345")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()
time.sleep(5)

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()

# Verify dashboard visibility
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Dashboard']")))
assert dashboard_element.is_displayed(), "Login failed or dashboard not found."
print("Login successful, dashboard is visible.")

# Login Feature Finish

## Business Unit Select Feature2

# Wait for the dropdown to appear and click to open it
# dropdown_xpath = "//div[@class='d-flex']//div[2]//div[1]//div[1]"
# dropdown = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)) )
# WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
# dropdown.click()
# print("Dropdown clicked successfully.")

# # Select the desired option (e.g., "Head Office")
# option_xpath = "//li[normalize-space()='Head Office']"

# # Select the desired option (e.g., "Matador Industrial Park")
# #option_xpath = "//li[normalize-space()='Matador Industrial Park']"
# option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
# option.click()
# print("Option selected successfully.")

# # Optional: Wait and verify the selection
# time.sleep(2)

## Business Unit Select Feature2 Finish

# DashBoard Feature3 Start
#Navigate to Dashboard
dashboard_icon = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Dashboard']")))
dashboard_icon.click()
print("Navigated to Dashboard successfully.")

#Function to select an option from dropdowns
def select_dropdown_option(wait, dropdown_xpath, option_text):
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
    print(f"Dropdown clicked: {dropdown_xpath}")

    option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{option_text}']")))
    option.click()
    print(f"Option selected: {option_text}")

# Select options from dropdowns
select_dropdown_option(wait, "//div[@class=' css-lam97r-control']", "Supervisor")

# Optional: Wait and verify the selection
time.sleep(5)
# DashBoard Feature3 Finish

# Homepage Feature4 Start
#Navigate to Dashboard
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")
# Homepage Feature4 Finish


# Navigate to Asset Management
driver.find_element(By.XPATH, "//img[@alt='Asset Management']").click()
time.sleep(3)

# Click "Item Profile"
driver.find_element(By.XPATH, "//button[text()='Item Profile']").click()
time.sleep(3)

# # Enter item name
itemname = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='itemName']"))
)
itemname.click()
itemname.send_keys("Display")
time.sleep(3)

# Enter description
description = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='description']"))
)
description.click()
description.send_keys("Display for Laptop")
time.sleep(3)

# description
driver.find_element(By.XPATH, "//div[@class=' css-1p1cok9']//div").click()
time.sleep(3)

# description
driver.find_element(By.XPATH, "//div[text()='Piece ']").click()
time.sleep(3)
# finished


# Item Category
driver.find_element(By.XPATH, "(//div[@class=' css-18w4uv4'])[2]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//div[text()='Electronic']").click()
time.sleep(3)
# finished

# Item Sub-Category
driver.find_element(By.XPATH, "(//div[@class=' css-1887a4s']/following-sibling::div)[3]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//div[text()='Device']").click()
time.sleep(3)
# finished

# Manufacturer/Brand Name
manufacturername = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='manufacturerName']"))
)
manufacturername.click()
manufacturername.send_keys("Iphone")
time.sleep(3)
# finished

# Save Clcik
savebutton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Save']"))
)
savebutton.click()
time.sleep(3)
# finished

# RegistrationPage
Registrationpage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Registration']"))
)
Registrationpage.click()
time.sleep(3)
# finished

# RegistrationButton
registrationbutton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Registration']"))
)
registrationbutton.click()
time.sleep(3)
# finished

# Item
driver.find_element(By.XPATH, "//div[@class=' css-1p1cok9']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Keyboard']").click()
time.sleep(3)
# finished

# Identifier By
Identifier = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='identifierBy']"))
)
Identifier.click()
Identifier.send_keys("D-1")
time.sleep(3)
# finished

# Auto Value
autovalue = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"))
)
autovalue.click()
time.sleep(3)
# finished

# startNumber
startNumber = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='startNumber']"))
)
startNumber.click()
time.sleep(3)
startNumber.send_keys("1")
time.sleep(3)
# finished

# Quantity
Qty = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='qty']"))
)
Qty.click()
time.sleep(3)
Qty.send_keys("2")
time.sleep(3)
# finished

# Quantity
Rate = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='rate']"))
)
Rate.click()
time.sleep(3)
Rate.send_keys("800")
time.sleep(3)
# finished

# Add
Add = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Add']"))
)
Add.click()
time.sleep(3)
# finished

# Save
Save = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Save']"))
)
Save.click()
time.sleep(3)
# finished

# ########################Assign##############

# Navigate to Assign page
Assignpage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Assign']"))
)
Assignpage.click()
time.sleep(3)
# finished

#Assign Button
Assignpage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Asset Assign']"))
)
Assignpage.click()
time.sleep(3)


# Asset Item Name
itemname = driver.find_element(By.XPATH, "(//div[@class='formik-select-wrapper']//div)[8]")
itemname.click()
time.sleep(3)
option1 = driver.find_element(By.XPATH, "//div[text()='Monitor(15)']")
option1.click()

# finished

# Employee Name
driver.find_element(By.XPATH, "(//div[@class='formik-select-wrapper']//div)[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Rifat 3[009]']").click()
time.sleep(3)
# finished

# Assign Date
assigndate = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='startDate']"))
)
assigndate.click()
time.sleep(3)
assigndate.send_keys("20250114")
time.sleep(3)
# finished


# Add
Add = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Add']"))
)
Add.click()
time.sleep(3)
# finished

# Save
Save = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Save']"))
)
Save.click()
time.sleep(3)
# finished

########Maintenance##############
# Navigate to Assign page
Assignpage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Maintenance']"))
)
Assignpage.click()
time.sleep(3)
# finished

#Send Asset to Maintenance
driver.find_element(By.XPATH, "//button[text()='Asset Maintenance']").click()
time.sleep(3)

#Asset
driver.find_element(By.XPATH, "(//div[@class=' css-1887a4s']//div)[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Keyboard(5)']").click()
time.sleep(3)

#Maintenance Type
driver.find_element(By.XPATH, "(//div[@class=' css-1887a4s']//div)[4]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Bios Update']").click()
time.sleep(3)
#finished

#HandOver To
driver.find_element(By.XPATH, "(//div[@class=' css-1887a4s']//div)[6]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Rifat 3[009]']").click()
time.sleep(3)
#finished

#Service Provider Name
driver.find_element(By.XPATH, "(//div[@class=' css-1887a4s']//div)[8]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='Startech']").click()
time.sleep(3)
#finished

#serviceProviderAddress
serviceProviderAddress = driver.find_element(By.XPATH, "//input[@name='serviceProviderAddress']")
serviceProviderAddress.click()
time.sleep(3)
serviceProviderAddress.send_keys("Test")
time.sleep(3)
#finished

#Description
description = driver.find_element(By.XPATH, "//input[@name='description']")
description.click()
time.sleep(3)
description.send_keys("Test")
time.sleep(3)
#finished

#Save Button
Save = driver.find_element(By.XPATH, "//button[text()='Save']")
Save.click()
time.sleep(3)
#finished

#maintenance data
maintenancedata = driver.find_element(By.XPATH, "//tbody//td[2]")
maintenancedata.click()
time.sleep(3)
amount = driver.find_element(By.XPATH, "//input[@name='cost']")
amount.click()
amount.send_keys("500")
time.sleep(3)

# Receive button click
receivebutton = driver.find_element(By.XPATH,"//button[text()='Receive']")
receivebutton.click()
time.sleep(3)
#finished

##################Asset Profile##############
# AssetProfile
assetprofile = driver.find_element(By.XPATH,"//a[text()='Asset Profile']")
assetprofile.click()
time.sleep(3)
#finished


# eye_button = driver.find_element(By.XPATH,"(//div[@class='d-flex justify-content-center'])[1]")
# actions = ActionChains(driver)
# actions.move_to_element(element_to_hover).perform()
# time.sleep(5)
# # View
# view = driver.find_element(By.XPATH,"(//button[@aria-label='Profile View'])[1]")
# view.click
# time.sleep(3)
# #close
# close = driver.find_element(By.XPATH,"//button[@aria-label='Close']")
# close.click
# time.sleep(3)

# #File Upload
# driver.find_element(By.XPATH,"(//button[@aria-label='Attachment Upload'])[1]").click()
# time.sleep(3)
# imageupload= driver.find_element(By.XPATH,"(//span[text()='Upload Asset Image']")
# imageupload.send_keys("C:\Users\ishti\OneDrive\Desktop\leave.png")
# time.sleep(3)


# Navigate to Homepage
home_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']")))
home_icon.click()
time.sleep(5)
print("Navigated to homepage successfully.")


# log out
def log_out(driver, wait):
    try:
        # Click the profile image
        profile_image = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Profile']")))
        profile_image.click()
        print("Clicked on Profile Image")

        # Click the logout button
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Log Out']")))
        logout_button.click()
        print("Clicked on Log Out Button")

        # Verify the login page is visible
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Log In']")))
        print("Logout successful: Login button is visible.")
    except Exception as e:
        print(f"Logout failed: {e}")

# Call the log_out function at the end
log_out(driver, wait)


# Close the driver
driver.quit()