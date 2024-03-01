from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

chrome_driver_path = '/path/to/chromedriver'
download_directory = '/path/to/download/directory'
os.makedirs(download_directory, exist_ok=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://upsc.gov.in/")

forms_downloads_link = driver.find_element(By.LINK_TEXT, "Forms & Downloads")
forms_downloads_link.click()
time.sleep(2)

pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
for pdf_link in pdf_links:
    pdf_link.click()
    time.sleep(5)

for root, dirs, files in os.walk(download_directory):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(os.getcwd(), file)
        os.rename(source_path, destination_path)

driver.quit()
