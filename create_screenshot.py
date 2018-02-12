import re


def _format_link(link):
    link = re.sub('https?://', '', str(link))
    link = re.sub('[:?/=]', '-', str(link))
    # link.replace('http://', '').replace('https://', '').replace('/?#', '-')
    return link


def _format_filename(link, width, height):
    return _format_link(link) + '__' + str(width) + 'x' + str(height) + '.png'


def create_screenshot(driver, data):
    for site in data['siteList']:
        driver.get(site['link'])
        resolution_list = data['resolutionList'] + site['resolutionList']
        for resolution in resolution_list:
            driver.set_window_size(resolution['w'], resolution['h'])
            filename = _format_filename(site['link'], resolution['w'], resolution['h'])
            driver.save_screenshot('screenshots/' + filename)
            print(filename)
