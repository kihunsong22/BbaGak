import re
import requests
from bs4 import BeautifulSoup
import time
import copy
from random import *

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def show_cookies(session, title=""):
    cookie_dict = session.cookies.get_dict()
    print("%s cookies: {" % title)
    for cookie in cookie_dict:
        print("    %s: %s" % (cookie, cookie_dict[cookie]))
    print("}\n")


header = {
    'Referer': 'http://bbasak.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

sleep_time = randint(100, 21600)
time.sleep(sleep_time)

sess = requests.Session()
res_1 = sess.get('http://bbasak.com/', headers=header)

show_cookies(sess, "Main Page")


# login
login_data = {
    'url': '',
    'mb_id': 'testid',
    'mb_password': 'testpassword'
}
res_2_login = sess.post('https://bbasak.com/bbs/login_check.php', data=login_data, headers=header)
show_cookies(sess, "Login")


# check login
res_3_main = sess.get('http://bbasak.com/', headers=header)
# print(res_3_main.text)


# # 출첵 value 받아오기
# res_4_postData = sess.get('http://bbasak.com/bbs/write.php?bo_table=com25', headers=header)
# soup = BeautifulSoup(res_4_postData.text, 'html.parser')
#
# value = [13]
# hidValues = soup.select('#fwrite > input[type=hidden]')
#
# post_data = {}
# for i in range(13):
#     num = "0"+str(i) if i < 10 else i
#     print("hidv[%s]: %s" % (num, hidValues[i]))
#
#     regex_name = '(?<=name=")(.+)(?=" type)'
#     regex = re.compile(regex_name)
#     name = regex.search(str(hidValues[i])).group()
#     regex_value = '(?<=value=")(.+)(?=")'
#     regex = re.compile(regex_value)
#     value = regex.search(str(hidValues[i]))
#     value = "" if value is None else value.group()
#
#     print("RexEx: name: %s,   value: %s" % (name, value))
#     post_data[name] = [value]
#
# print()
# post_data['wr_subject'] = '출석'
# post_data['wr_link1'] = ''
# post_data['nx_seller_nick'] = ''
# post_data['nx_seller_id'] = ''
# post_data['wr_content'] = '<p>출첵합니다</p>'
# post_data['x'] = '41'
# post_data['y'] = '6'
# post_data['wr_beforeunload'] = '1'
# # post_data['bf_file[]'] = ['']
# print("Post Data: " + str(post_data))
#
# header_write = copy.deepcopy(header)
# header_write['Host'] = 'bbasak.com'
# header_write['Referer'] = 'http://bbasak.com/bbs/write.php?bo_table=com25'
# # header_write['Origin'] = 'http://bbasak.com'
# # header_write['board_wr_id'] = ',5681790,5681832,5681837,5687459,5688666'
# # header_write['bo_tables'] = ',com25,com25,com25,com25,com25,com25,com25,com25,com25,com25'
# print("Write Header: " + str(header_write))
#
# time.sleep(0.1)
#
# res_5_WriteData = sess.get('http://bbasak.com/bbs/write_update.php', headers=header_write, data=post_data, proxies=proxies)
#
# print("\n\n")
# print(res_5_WriteData.text)

pass
