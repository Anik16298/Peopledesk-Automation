from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import pyautogui
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ────────────────────────────────────────────────
# APM Screenshot Automation (This script automates the process of taking screenshots of APM transactions and errors for each service listed on the APM page)
# ────────────────────────────────────────────────
# Step 1: VPN Connection On
# pyautogui.click(x=1750, y=1050)  # Adjust coordinates to focus on the browser
# time.sleep(2)
# pyautogui.click(x=1800, y=585)  # Adjust coordinates to focus on the browser
# time.sleep(5)

# Setup Firefox options
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 30)

# Create output folder
output_dir = "apm_screenshots"
os.makedirs(output_dir, exist_ok=True)

# Open APM dashboard
driver.get("http://10.209.99.128:5601/")

# Click APM Project List
apm_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//span[@class='euiToolTipAnchor euiListGroupItem__tooltip'])[11]")))
apm_btn.click()

# Select 'Production' from environment filter
env_input = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='euiSelect euiSelect--inGroup']")))
env_input.click()
time.sleep(1)
prod_option = wait.until(EC.presence_of_element_located((By.XPATH, "//option[text()='Production']")))
prod_option.click()
time.sleep(1)

# Click Refresh
refresh_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='euiButton__text euiSuperUpdateButton__text']")))
refresh_btn.click()

# Get total number of projects initially by collecting their hrefs
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".euiTableCellContent a")))
project_elements = driver.find_elements(By.CSS_SELECTOR, ".euiTableCellContent a")
project_links = [(elem.text.replace("/", "-"), elem.get_attribute("href")) for elem in project_elements]

print(f"Total projects found: {len(project_links)}")

# List of services to skip
services_to_skip = {"Apon-API", "PeopleDesk-V2-Scheduler", "Peopledesk-ARL-API", "RmgFinance-API", "Rmg-API",
                    "RmgProduction-API", "TAX-Identity-API", "Tax-Domain-API",
                    "SmeCPanelAPI"}  # Add the names of services to skip

# Loop through each project by link
for project_name, project_url in project_links:
    if project_name in services_to_skip:
        print(f"Skipping: {project_name}")
        continue

    print(f"Processing: {project_name}")

    # Navigate directly to the project link
    driver.get(project_url)

    # Wait until Transaction page loads
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'euiTitle')]")))
    time.sleep(5)

    avg_button = driver.find_element(By.XPATH, "//span[text()='Avg. duration']")
    for _ in range(2):
        avg_button.click()

    # Save Transaction screenshot
    driver.get_full_page_screenshot_as_file(f"{output_dir}/{project_name}_transaction.png")
    print(f"Saved: {project_name}_transaction.png")

    # Click on the Errors tab
    try:
        error_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Errors']")))
        error_tab.click()
        time.sleep(5)

        # Save Errors screenshot
        driver.get_full_page_screenshot_as_file(f"{output_dir}/{project_name}_error.png")
        print(f"Saved: {project_name}_error.png")
    except Exception as e:
        print(f"Error tab not found for {project_name}: {e}")

    # Optional short wait before going to the next project
    time.sleep(2)

# Go back to the APM Services page
recall = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class = 'euiLink euiLink--subdued euiBreadcrumb']"))).click()
time.sleep(5)

print("All screenshots captured.")

driver.quit()

# ────────────────────────────────────────────────
# Email the screenshots
# ────────────────────────────────────────────────
print("Mailing screenshots In Progress...")
sender_email = 'anik.chakraborty@ibos.io'
password = 'qvsh hfri cowb ylvk'  # Use an App Password if 2FA is enabled
receiver_address = 'ishtiaque@ibos.io'
body = "Kibana APM Screenshots-Test"

# Create message container
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_address
message["Subject"] = "Kibana APM All Project Screenshots"

# Add body to emailAsset-API_transaction.png
message.attach(MIMEText(body, "plain"))

# Folder containing images
image_folder = r"C:\Users\ibos\PycharmProjects\Peopledesk_demo_automate\.venv\apm_screenshots"  # Replace with your folder path

# Supported image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Attach all images from the folder
for filename in os.listdir(image_folder):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        filepath = os.path.join(image_folder, filename)
        with open(filepath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

            # Add headers to attachment
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)

# Send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_address, message.as_string())

print(f"Email Sent with {len(message._payload) - 1} image attachments")  # Subtract 1 for the text body

# # Close the browser
# driver.quit()
# print("WebDriver session End.")