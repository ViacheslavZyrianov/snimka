from selenium import webdriver
import shutil
import os
import urllib.request, json

from CreateScreenshot import create_screenshot

if os.path.exists('screenshots'):
    shutil.rmtree('screenshots')

os.makedirs('screenshots')

driver = webdriver.Chrome()

url_to_open = 'http://snimka.local/test-data.php'

with urllib.request.urlopen(url_to_open) as url:
    response = json.loads(url.read().decode())
    create_screenshot(driver, response)

driver.close()