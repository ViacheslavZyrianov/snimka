# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import shutil
# import os
# # from element_has_css_class import element_has_css_class
#
# import urllib.request, json
#
#
# from CreateScreenshot import create_screenshot
#
# if os.path.exists('screenshots'):
#     shutil.rmtree('screenshots')
#
# os.makedirs('screenshots')
#
# driver = webdriver.Chrome()
#
# with urllib.request.urlopen('http://snimka.local/test-data.php') as url:
#     response = json.loads(url.read().decode())
#     create_screenshot(driver, response)
#
# driver.close()
#
# # try:
# #     WebDriverWait(driver, 10).until(
# #         EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loader'))
# #     )
# #     # WebDriverWait(driver, 10).until(
# #     #     EC.presence_of_element_located((By.XPATH, 'nav[class*="nav_item"]:not([style*="disabled"])'))
# #     #     # element_has_css_class((By.CSS_SELECTOR, '.nav_item'), 'disabled')
# #     # )
# #     driver.save_screenshot('screenshots/' + str(size['width']) + 'x' + str(size['height']) + '.png')
# #     driver.close()
# # finally:
# #     print('10 seconds passed!')
# #     driver.close()
