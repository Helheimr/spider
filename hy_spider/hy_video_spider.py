# todo:
# - json
# -

import requests
from lxml import etree
import you_get
import re
import random
import sys
from urllib.parse import unquote

# 这是爬取好的url
# video_urls = ['http://vqzone.gtimg.com/1006_9f98ec51aa4545689af86b7d7d2bdbbb.f0.mp4?vkey=E805DE3E904AB243B193379482D9864F112768BA572A8391BFACF2EFC2EDFC878050A73BB63C74E9183403E14025BCC4632F8D16032761DF', 'http://vqzone.gtimg.com/1006_6a832c6118804e3aa1ac92fd6ffddbbb.f0.mp4?vkey=86DAD618B9EA341AE1649457EA29DF6F8EECE9ADCC71552F9DB10D4C361561781323EBC5A83F6CF5E2D4338F95E07F5DF2C5AAA747D9910D', 'http://vqzone.gtimg.com/1006_2ccfaa3edc3b4358985f1598d287dbbb.f0.mp4?vkey=6C284B16644A495781C7F4DF58C15B459BA4896ED8C22205DBED0D6B22D363265A6FF7450090BE8CB5B874D5B100F11F0B95657909EA5E47', 'http://vqzone.gtimg.com/1006_79e4fb2625d34bc199d49391da4cdbbb.f0.mp4?vkey=8E3229CEE71A7FFCB6751F96004AD8D004070F6A25DCAC0528A8F795E61C8901CEE6C041BEBE508093488282D5B44D4D1B1FCDF00A357D3A', 'http://vqzone.gtimg.com/1006_5637e2f787de45d3b214b58751a4dbbb.f0.mp4?vkey=2763C9475D83F658CC93D52FAAB9C16A2E7BF1E07A39B976D8720CDC954E109ECAE25B929D84FA072CF7A2C53647C3DD5604F6B22B289060', 'http://vqzone.gtimg.com/1006_ab59302e91294209a15cfb11c91edbbb.f0.mp4?vkey=BEA7605EE2EFEAB398CE1DE4B1A7CADC8509E4CD58B89C9717D945C9FE103F7A372065EF3988765BCCA65C01B2FC1D013FEDAF6B4E243C8B',
            #   'http://vqzone.gtimg.com/1006_85734b76016a4dcda8df8552bd13dbbb.f0.mp4?vkey=45390F9BDC4976110937E6BAC6AA78D908A5B9B76FDE34CAA62962E6698D67AE7FC1865EA67CF56147EEE31BCCEB50A43C93FC0601B75EE4', 'http://vqzone.gtimg.com/1006_c4caf593291e46649b5e6f22efaddbbb.f0.mp4?vkey=67E85E34E9072B1195CC5446A049E9384BD69C2EF8E5234B5C2EB62070F2A95671A9606DEFBD46AC1775B927C6F732FFFB272036BE925512', 'http://vqzone.gtimg.com/1006_02edb3902e134f18a5340f8526e0dbbb.f0.mp4?vkey=DE549EAAD939CD44DFF74661DA4EE75C47B7C294BE1AD137251643A4401010BEE32A42266514A704C63266B72F67F220B64B136F60412AE3', 'http://vqzone.gtimg.com/1006_c147f20fa1e84bb0b55305138944dbbb.f0.mp4?vkey=6179724077324095215A609583C8A593AE74CB98665A7B7258AEAA4B10312E7A279362F8915754E1F9582EDEA117FD4B234339CD652DC776', 'http://vqzone.gtimg.com/1006_9d8a61e3e1b544f9b46d74adbd3ddbbb.f0.mp4?vkey=1A2EAAFD59646EC514184FF0A314274FC0E7ED8CA20569E913F34D475B09A7184A0EABB4C6530E134B76CEB68055B9003565DA16FBABA445', 'http://vqzone.gtimg.com/1006_611236a197d9424cbf84f6026831dbbb.f0.mp4?vkey=6179724077324095215A609583C8A593B97C8EAD6C1AE792A3A55F35327EA489705AB06EAEAB4CCCBB390A380D59F0DC339B12CF1461DE0A']
video_urls = []
xhr_url = "https://www.agefans.tv/_getplay?animeid=20190042&routeidx=2&episodeidx={id}&time=1&pc_play_vid=v&playcfgname=fc7f4531&pc_play_vid_sign={vid_sign}&num={num}"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36",
    'Referer': 'https://www.agefans.tv/'
}


def get_vid():
    '''
    获取关键请求参数vid_sign
    '''
    url = "https://www.agefans.tv/play/20190042"
    response = requests.get(url, headers=headers)
    # --xpath方法--
    html = etree.HTML(response.content.decode('utf-8'))
    vid = html.xpath(
        "//p[@class='x_x_a9']//a[@routeidx='2']/@pc_play_vid_sign")

    return vid


def get_video_url():
    id = 1
    num = random.random()
    for vid in get_vid():
        url = xhr_url.format(id=id, vid_sign=vid, num=num)
        id += 1
        response = requests.get(url, headers=headers)
        content = response.content.decode('utf-8')
        video_url = unquote(content)
        # with open('./dowload_url.txt', 'a+') as f:
        #     f.write(video_url + "\n")
        #     f.close
        video_urls.append(video_url)
        print(video_url + " done.")


def dowload_url(i):
    name = "Kaguya-sama wa Kokurasetai Tensai-tachi no Ren ai Zunousen [720P_10Bit_HEVC_FLAC][{}]".format(
        i)
    url = video_urls[i-1]
    print(name)
    print(url)
    sys.argv = ['you-get', '-o', r'./かぐや様は告らせたい～天才たちの恋愛頭脳戦～', '-O', name, url]
    you_get.main()


if __name__ == "__main__":
    get_video_url()

    # for i in range(1, 13):
        # dowload_url(i)
