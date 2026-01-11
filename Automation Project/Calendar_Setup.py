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
wait = WebDriverWait(driver, 20)  # Ensure wait is initialized here
wait.until(EC.title_contains("PeopleDesk"))
print(f"Page title: {driver.title}")

##.............LogIn Feature................##

# Enter user ID
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your id']"))).send_keys("dailystar@ibos.io")

# Enter password
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("dailystar@ibos")

# Click the "Log In" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))).click()

# Wait for the dashboard logo and click it
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logo-img']"))).click()

#Adminstration
Adminstration = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Administration']")))
Adminstration.click()
time.sleep(5)
print("Adminstration Module Click")

#Time Management
Time_Management = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Time Management']")))
Time_Management.click()
time.sleep(3)
print("Clicked Successfully on the Time_Management")

#Calendar Setup
Calendar_Setup = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Calendar Setup']")))
Calendar_Setup.click()
time.sleep(3)
print("Clicked Successfully on the Calendar Setup")

#Calendar Setup Button Click
Calendar_Setup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li//button[text()='calendar Setup']")))
Calendar_Setup_button.click()
time.sleep(3)
print("Successfully Clicked on the Calendar Setup Button")

# Generate a random two-digit number
random_number = random.randint(1, 999)

#Calendar Name
Calendar_Name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='calendarName']")))
Calendar_Name.click()
time.sleep(3)
Calendar_Name.send_keys(f"General Calendar HO - {random_number}")
time.sleep(5)
print("Successfully Entered the Calendar Name")

#Minimum Working Hour
Minimum_Working_Hour = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='minWork']")))
Minimum_Working_Hour.click()
time.sleep(3)
Minimum_Working_Hour.send_keys("8")
time.sleep(5)
print("Entered Successfully Minimum Working Hour")

#Office Opening Time
Office_Opening_Time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='officeStartTime']")))
Office_Opening_Time.click()
time.sleep(3)
Office_Opening_Time.send_keys("08")
time.sleep(3)
Office_Opening_Time.send_keys("00")
time.sleep(3)
Office_Opening_Time.send_keys("AM")
time.sleep(3)
print("Entered Successfully Office Opening Time")

#Office Closing Time
Office_Closing_Time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='officeCloseTime']")))
Office_Closing_Time.click()
time.sleep(3)
Office_Closing_Time.send_keys("08")
time.sleep(3)
Office_Closing_Time.send_keys("00")
time.sleep(3)
Office_Closing_Time.send_keys("PM")
time.sleep(3)
print("Entered Successfully Office Closing Time")

#Start Time
Start_Time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='startTime']")))
Start_Time.click()
time.sleep(3)
Start_Time.send_keys("09")
time.sleep(3)
Start_Time.send_keys("00")
time.sleep(3)
Start_Time.send_keys("AM")
time.sleep(3)
print("Entered Successfully Start Time")

#End Time
End_Time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='endTime']")))
End_Time.click()
time.sleep(3)
End_Time.send_keys("06")
time.sleep(3)
End_Time.send_keys("00")
time.sleep(3)
End_Time.send_keys("PM")
time.sleep(3)
print("Entered Successfully End Time")

#Extended Start Time
Extended_Start_Time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='allowedStartTime']")))
Extended_Start_Time.click()
time.sleep(5)
Extended_Start_Time.send_keys("09")
time.sleep(5)
Extended_Start_Time.send_keys("15")
time.sleep(5)
Extended_Start_Time.send_keys("AM")
time.sleep(5)
print("Entered Successfully Extended Start Time")

#Last Start Time
Last_Start_Time  = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='lastStartTime']")))
Last_Start_Time.click()
time.sleep(5)
Last_Start_Time.send_keys("12")
time.sleep(5)
Last_Start_Time.send_keys("00")
time.sleep(5)
Last_Start_Time.send_keys("PM")
time.sleep(5)
print("Entered Successfully Last Start Time")

#Lunch Start Time
Lunch_Start_Time  = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='breakStartTime']")))
Lunch_Start_Time.click()
time.sleep(5)
Lunch_Start_Time.send_keys("01")
time.sleep(5)
Lunch_Start_Time.send_keys("30")
time.sleep(5)
Lunch_Start_Time.send_keys("PM")
time.sleep(5)
print("Entered Successfully Lunch Start Time")

#Lunch End Time
Lunch_End_Time  = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='breakEndTime']")))
Lunch_End_Time.click()
time.sleep(5)
Lunch_End_Time.send_keys("02")
time.sleep(5)
Lunch_End_Time.send_keys("30")
time.sleep(5)
Lunch_End_Time.send_keys("PM")
time.sleep(5)
print("Entered Successfully Lunch End Time")

#Workplace
Workplace = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='input-field-main']//div)[1]")))
time.sleep(3)
Workplace.click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[4]").click()
time.sleep(3)

pyautogui.moveTo(1214, 713)  # Coordinates for the Save button; adjust them as per your screen
pyautogui.click()
time.sleep(5)
print("Clicked on the Save button.")

#Save Button Click
Save_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Save']")))
Save_button.click()
time.sleep(5)
print("Save Button Click")


# log out
def log_out(driver):
    switch_to_main_window(driver)
    # Click the profile image
    driver.find_element(By.XPATH, "//img[@alt='Profile']").click()
    print("Clicked on Profile Image")

    # Click the logout button
    driver.find_element(By.XPATH, "//h3[normalize-space()='Log Out']").click()
    print("Clicked on Log Out Button")

    # Verify the login page is visible
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log In']")
    if login_button.is_displayed():
        print("Logout successful.")
    else:
        print("Logout failed: Login button not visible.")

# Close the browser
driver.quit()