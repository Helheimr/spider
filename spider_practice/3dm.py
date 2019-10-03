# 爬取3DM下精选壁纸 
# 暂未采用 多线程
import requests
from lxml import etree
import os

base_url = "https://www.3dmgame.com/bagua_66_1/"
folder = './3dm'
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36",
    'Referer': 'https://www.3dmgame.com/bagua_66_1/'
}


def get_urls(url):
    # 爬取3dm精品壁纸下详情urls
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))
    detail_urls = html.xpath('//ul[@class="list"]//a/@href')
    # print(detail_urls)
    return detail_urls


def spider(url):
    # 爬取3dm该url下图片
    url_pages = [url]
    for i in range(2, 6):
        url_pages.append(url[0:-5] + '_' + str(i) + '.html')
    # print(url_pages)

    imgs = []
    for url_page in url_pages:
        response = requests.get(url_page, headers=headers)
        html = etree.HTML(response.content.decode('utf-8'))
        imgs.extend(html.xpath('//div[@class="news_warp_center"]//p//img/@src'))
    # print(imgs)

    index = etree.HTML(requests.get(url, headers=headers).content.decode('utf-8')).xpath(
        '//div[@class="news_warp_center"]//p[2]//@alt')[0]

    if not os.path.exists(folder + "/" + index):
        os.makedirs(folder + "/" + index)

    j = 0
    for img in imgs:
        with open(folder + "/" + index + '/' + img[-10:-6] + '_%s.jpg' % (str(j)), 'wb') as im:
            print('正在请求-->', img[-10:-6] + '_%s.jpg' % (str(j)))
            im.write(requests.get(img, headers=headers).content)
            print('获取到结果:-->', img[-10:-6] + '_%s.jpg' % (str(j)) + '\n')
            j = j + 1


if __name__ == '__main__':
    # for url in get_urls(base_url):
    for get_url in get_urls(base_url):
        spider(get_url)
