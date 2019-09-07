import requests
from urllib.parse import quote
from lxml import etree
from urllib import request
import os


def get_headers(referer):
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer": "http://wiki.joyme.com/arknights/{}".format(referer)
    }
    return headers


def get_staff_names():
    """
    得到干员名称
    """
    url_staff = "http://wiki.joyme.com/arknights/%E5%B9%B2%E5%91%98%E6%95%B0%E6%8D%AE%E8%A1%A8"
    response = requests.get(url_staff, headers=get_headers(""))
    html = etree.HTML(response.text)
    names = html.xpath('//tr//div[@class="floatnone"]//a/@title')
    # print(names)
    return names


if __name__ == '__main__':
    for name in get_staff_names():
        url = "http://wiki.joyme.com/arknights/" + quote(name)

        response = requests.get(url, headers=get_headers(quote(name)))
        html = etree.HTML(response.text)
        imgs = html.xpath('//div[@class="Contentbox2"][@id="Contentbox3"]//img')
        filename = 'arknights/' + name

        if not os.path.exists(filename):
            os.makedirs(filename)

        for img in imgs:
            img_url = img.get("src")
            alt = img.get("alt")
            # print(img_url)
            print("正在下载>>%s>>%s" % (img_url, filename + "/" + alt))
            request.urlretrieve(img_url, filename + "/" + alt)
        print("下载完成>>%s" % name)
        print("-----------------------------")
