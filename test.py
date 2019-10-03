import requests
from lxml import etree
from urllib.parse import urlencode, quote
from lxml import etree
import urllib.request  # 获取网页内容
from bs4 import BeautifulSoup  # 解析网页内容
import re  # 正则式模块.
import os  # 系统路径模块: 创建文件夹用
import socket  # 下载用到?

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer": "https://www.mzitu.com/199492/1"
}


def get_page1_urls():  # 定义一个函数
    page1_urls = []  # 定义一个数组,来储存所有主题的URL
    for page in range(1, 2):
        # 1-140. 整个妹子图只有140页,注意下面缩进内容都在循环内的!
        url = 'http://www.mzitu.com/page/' + str(page)
        response = requests.get(url, headers=headers)
        html = response.text
        # read 就是读取网页内容并储存到 html变量中.

        soup = BeautifulSoup(html, 'lxml')
        # 把下载的网页.结构化成DOM, 方便下面用 find 取出数据
        lis = soup.find('ul', {'id': 'pins'}).find_all('li')
        # 找到 id 为pins 这个列表下面的 每个列 就找到每个页面下的 24个主题了

        for li in lis:
            # 遍历每页下面的24个主题 (也就是24个li)
            page1_urls.append(li.find('a')['href'])
            # 把每个主题的地址. 添加到page1_urls 这个数组里面.
        # print(page1_urls)
        # 显示网址. 测试用. 循环140次. 这样就获得了所有主题的网址了
    return page1_urls


def get_page_num(page1_url):
    response = requests.get(page1_url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    try:
        page_num = soup.find('div', {'class': 'pagenavi'}).find_all('a')[-2].find('span').get_text()
    except:
        return None
    return int(page_num)






if __name__ == '__main__':
    # urllib.request.urlretrieve("https://i5.meizitu.net/2019/08/18b01.jpg", './妹子图/' +"性感御姐就是阿朱啊旗袍丝袜高清写真 轻熟韵味妩媚优雅" + '/' + "03.jpg")
    with open('./妹子图/' +"性感御姐就是阿朱啊旗袍丝袜高清写真 轻熟韵味妩媚优雅" + '/' + "03.jpg", 'wb') as im:

        im.write(requests.get("https://i5.meizitu.net/2019/08/18b01.jpg", headers=headers).content)
