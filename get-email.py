#coding=utf-8
from bs4 import BeautifulSoup
import requests


URLSO = 'https://www.foomajapan.jp/2015/english/exhibitor_info/'
URL = URLSO+'index.html'
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
detailslink = soup.find_all("a",href=True)



for link in detailslink:
    url = URLSO+link.get('href')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    # 找到Email那行
    email = soup.find(abbr="E-mail")
    # txt从末尾加入文字
    f = open("list.txt", "a", encoding="utf-8")
    if email is not None:
        # 获取Email后面一行的地址
        mail = email.find_next_sibling()
        maillist = mail.get_text()
        # 写入邮箱地址
        f.writelines(['\n',maillist])
        print(maillist)
    else:
        print('None')
        
f.close()
print('Done')
        

