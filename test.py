import datetime
import time
from selenium import webdriver

print(datetime.datetime.now())

options = webdriver.ChromeOptions()

# prefs = {'profile.default_content_setting_values': {'cookies' : 2,
# 'images': 2,
# 'plugins' : 2,
# 'popups': 2,
# 'geolocation': 2,
# 'notifications' : 2,
# 'auto_select_certificate': 2,
# 'fullscreen' : 2,
# 'mouselock' : 2,
# 'mixed_script': 2,
# 'media_stream' : 2,
# 'media_stream_mic' : 2,
# 'media_stream_camera': 2,
# 'protocol_handlers' : 2,
# 'ppapi_broker' : 2,
# 'automatic_downloads': 2,
# 'midi_sysex' : 2,
# 'push_messaging' : 2,
# 'ssl_cert_decisions': 2,
# 'metro_switch_to_desktop' : 2,
# 'protected_media_identifier': 2,
# 'app_banner': 2,
# 'site_engagement' : 2,
# 'durable_storage' : 2}}

options.add_argument('headless')
options.add_argument('window-size=1280x720')
options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36')
options.add_argument('lang=ko_KR')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')

options.add_argument('--no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")

# driver = webdriver.Chrome('/root/bbagak/chromedriver_75', options=options)
driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)
print('loading complete')

driver.get('http://bbasak.com/')
print('  into main page')
driver.find_element_by_css_selector('#loginbox > p.psr.pl15.pr15.pt10 > input.btn_login').click()
driver.find_element_by_css_selector('#login_id').send_keys("legatalee")
driver.find_element_by_css_selector('#login_pw').send_keys("newdimigo")
driver.find_element_by_css_selector('#loginbox > p.psr.pl15.pr15.pt10 > input.btn_login').click()
print('  logged in')
driver.implicitly_wait(1)

print('browsing through bulletin board')
driver.get('http://bbasak.com/bbs/board.php?bo_table=com25')

first_writer = driver.find_element_by_css_selector('#fboardlist > table:nth-child(10) > tbody > tr:nth-child(1) > td:nth-child(1) > p').text
print(first_writer)

driver.quit()
print('Complete')
print('\n')