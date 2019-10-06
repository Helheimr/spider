# 爬取 "http://www.yhdm.tv/" 下鬼灭之刃全集直链URL

import requests
from lxml import etree
import os
from bs4 import BeautifulSoup


base_url = "http://www.yhdm.tv/v/4426-{}.html"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36",
    'Referer': 'http://www.yhdm.tv'
}


def get_video_url():
    for i in range(1, 27):
        # 遍历26集URL
        url = base_url.format(i)
        # print(url)
        response = requests.get(url, headers=headers)

        # --beautiful soup方法--
        # html = response.decode('utf-8')
        # soup = BeautifulSoup(html, 'lxml')
        # video_url = soup.find('div', {'class': 'bofang'}).find('div')['data-vid'][0:-4]
        # print(video_url)

        # --xpath方法--
        html = etree.HTML(response.content.decode('utf-8'))
        video_url = html.xpath("//div[@class='bofang']/div/@data-vid")[0][0:-4]

        # 将url直链写入文本
        with open('./dowload_url.txt', 'a') as f:
            f.write(video_url + "\n")
        print(video_url + "done.")
        # break


if __name__ == "__main__":
    get_video_url()
