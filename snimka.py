from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os
# from element_has_css_class import element_has_css_class
from CreateScreenshot import create_screenshot

jsonFromSomewhere = {
    'resolutionList': [
        {
            'w': 1920,
            'h': 1080,
        },
        {
            'w': 1440,
            'h': 900,
        },
        {
            'w': 1366,
            'h': 768,
        },
        {
            'w': 1280,
            'h': 1024,
        },
        {
            'w': 1280,
            'h': 800,
        },
        {
            'w': 1024,
            'h': 768,
        },
    ],
    'siteList': [
        {
            'link': 'https://habrahabr.ru/post/348634/#comment_10659356',
            'resolutionList': [
                {
                    'w': 900,
                    'h': 765,
                },
                {
                    'w': 1488,
                    'h': 228,
                },
            ],
        },
        {
            'link': 'http://selenium-python.readthedocs.io/',
            'resolutionList': [],
        },
        {
            'link': 'http://moringa.labgrape.com',
            'resolutionList': [],
        },
    ]
}

if os.path.exists('screenshots'):
    shutil.rmtree('screenshots')

os.makedirs('screenshots')

driver = webdriver.Chrome()

create_screenshot(driver, jsonFromSomewhere)

driver.close()

# try:
#     WebDriverWait(driver, 10).until(
#         EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loader'))
#     )
#     # WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, 'nav[class*="nav_item"]:not([style*="disabled"])'))
#     #     # element_has_css_class((By.CSS_SELECTOR, '.nav_item'), 'disabled')
#     # )
#     driver.save_screenshot('screenshots/' + str(size['width']) + 'x' + str(size['height']) + '.png')
#     driver.close()
# finally:
#     print('10 seconds passed!')
#     driver.close()