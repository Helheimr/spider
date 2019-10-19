# Author：lyuan
# 爬取站点：https://www.luoxia.com/piaomiaolu/
# Time：2019.10.18

import requests
import os
import re
from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing import Pool
import time

base_url = "https://www.luoxia.com/piaomiaolu/pml-{}"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36",
    'Referer': 'https://www.luoxia.com/piaomiaolu/'
}

booknames = ['九州·缥缈录I：莽荒', '九州·缥缈录II：苍云古齿',
             '九州·缥缈录III：天下名将', '九州·缥缈录IV：辰月之征', '九州·缥缈录V：一生之盟', '九州·缥缈录VI：豹魂 ']


def get_book(i):
    url = base_url.format(str(i))
    # 获取每本书下id 起 末
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))

    id_sta = html.xpath(
        "//div[@class='book-list clearfix']//a/@href")[0][-9:-4]
    id_end = html.xpath(
        "//div[@class='book-list clearfix']//a/@href")[-1][-9:-4]
    # bookname = str(html.xpath('//div[@class="book-describe"]//h1/text()')[0])
    bookname = booknames[i-1]
    print(bookname)

    # 写入本书开始语
    with open(r'./' + booknames[i-1] + '.txt', 'a+', encoding='utf-8') as f:
        f.write('《' + booknames[i-1] + '》' + '\r\n')
        f.close

    # 遍历一本书下所有章节
    for id in range(int(id_sta), int(id_end) + 1):
        section_url = "https://www.luoxia.com/piaomiaolu/{}.htm".format(id)

        print("正在下载 --->" + bookname + "下：--->" + section_url)
        
        try:
            get_section(section_url, bookname)
        except Exception:
            continue

        print("下载完成 " + bookname + "下：" + section_url)

    # 写入本书结束语 
    with open(r'./' + booknames[i-1] + '.txt', 'a+', encoding='utf-8') as f:
        f.write('\r' + '《' + booknames[i-1] + '》完' + '\r\n')
        f.close

def get_section(url, bookname):
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    # 获取章节文本
    section_text = str(soup.select('#nr1')[0])
    section_text = re.sub(r'<.*?>', '', section_text).strip()
    # 去除水印
    section_text = re.sub(r'落.*[m,M,说]', '', section_text, re.S)
    # 获取章节名称
    section_name = str(soup.select('#nr_title')[0])
    section_name = re.sub(r'<.*?>', '', section_name).strip()
    # section_name = soup.find_all('h1',{'id':'nr_title'})[0].get_text()

    # print(section_text)
    # print(section_name)

    with open(r'./' + bookname + '.txt', 'a+', encoding='utf-8') as f:
        f.write('\r' + section_name + '\r\n')

        f.write(section_text + "\n")
        f.close


if __name__ == "__main__":

    e1 = time.time()
    # 创建进程池
    pool = Pool(6)
    pool.map(get_book, range(1, 7))
    pool.close()
    pool.join()
    e2 = time.time()
    print(e2-e1)

    # 60.14s pool 5
    # 59.33s pool 6

