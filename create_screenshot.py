from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _format_link(link):
    return link.replace('http://', '').replace('https://', '').replace('www.', '').replace('/', '-')


def _format_filename(link, width, height):
    return _format_link(link) + '__' + str(width) + 'x' + str(height) + '.png'


def _emulate_mobile():
    print('mobile')


def _loader(driver):
    is_loader_exists = driver.execute_script('return !!document.querySelector(".loader")')
    if is_loader_exists:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loader'))
        )


def create_screenshot(data):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=options)

    for site in data['siteList']:
        driver.get(site['link'])
        resolution_list = data['resolutionList'] + site['resolutionList']
        for resolution in resolution_list:
            if resolution['h'] == 1:
                resolution['h'] = driver.execute_script('return document.querySelector("body").scrollHeight;')
            driver.set_window_size(resolution['w'], resolution['h'])
            if resolution['w'] <= 960:
                _emulate_mobile()
            filename = _format_filename(site['link'], resolution['w'], resolution['h'])
            _loader(driver)
            driver.save_screenshot('screenshots/' + filename)
            print(filename)
