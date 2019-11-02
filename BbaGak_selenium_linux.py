import datetime
import time
from random import *
#import sys
#from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1280x720')
options.add_argument('disable-gpu')
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
options.add_argument('lang=ko_KR')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')

options.add_argument('--no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")

f = open('/root/bbagak/log.txt', 'a', buffering=1)
driver = webdriver.Chrome('/root/bbagak/chromedriver_77', options=options)
driver.implicitly_wait(3)
#fprint('loading complete')
# sys.stdout.flush()


def fprint(text):
    text = str(text)
    print(text)
    text = text + '\n'
    f.write(text)


def auto_script(bba_id, bba_pass):
    # 로그인
    fprint('user: ' + bba_id)
    driver.get('http://bbasak.com/')
    fprint('  into main page')
    # fprint(driver.page_source)
    driver.find_element_by_css_selector('#login_id').send_keys(bba_id)
    driver.find_element_by_css_selector('#login_pw').send_keys(bba_pass)
    fprint('  login form okay')
    driver.find_element_by_css_selector(
        '#loginbox > p.psr.pl15.pr15.pt10 > input.btn_login').click()

    time.sleep(1)

    # 출첵게시판
    fprint('  browsing through bulletin board')
    driver.get('http://bbasak.com/bbs/board.php?bo_table=com25')
    driver.find_element_by_css_selector(
        '#fboardlist > div.btnwrite > p.fr.pr10 > a > span').click()

    # 글쓰기
    fprint('  writing attendance check')
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#fwrite > table > tbody > tr:nth-child(3) > td > div.notice_img_warning > img')))
    fprint('  attendance check loading complete')
    driver.find_element_by_css_selector(
        '#fwrite > table > tbody > tr:nth-child(1) > td > input').send_keys('출석')
    driver.find_element_by_css_selector(
        '#fwrite > table > tbody > tr:nth-child(3) > td > div.notice_img_warning > img').click()

    time.sleep(4)
    # driver.switch_to.frame(driver.find_element_by_css_selector('#cke_1_contents > iframe'))
    # driver.switch_to.default_content()
    script = 'document.querySelector("#cke_1_contents > iframe").contentDocument.getElementsByTagName("p")[0].innerHTML = "출첵합니다"'
    driver.execute_script(script)
    driver.find_element_by_css_selector('#submit_img').click()
    time.sleep(0.5)

    # 로그아웃
    fprint('  logging out')
    driver.find_element_by_css_selector('#gm > li:nth-child(5) > a').click()


fprint('\n\n====================')
fprint(datetime.datetime.now())
fprint('====================\n')
# sys.stdout.flush()

#auto_script('testid', 'testpassword')
#time.sleep(randint(60, 3600))

driver.quit()
fprint('Complete - ' + datetime.datetime.now().strftime('%H:%M:%S'))
fprint('====================\n')
f.close()
