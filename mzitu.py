from bs4 import BeautifulSoup  # 解析网页内容
import re  # 正则式模块.
import os  # 系统路径模块: 创建文件夹用
import requests


def get_headers(referer):
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer": referer
    }
    return headers


def get_page1_urls():  # 定义一个函数
    page1_urls = []  # 定义一个数组,来储存所有主题的URL
    for page in range(1, ):
        # 1-140. 整个妹子图只有140页,注意下面缩进内容都在循环内的!
        url = 'http://www.mzitu.com/page/' + str(page)
        response = requests.get(url, headers=get_headers("https://www.mzitu.com/"))
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
    response = requests.get(page1_url, headers=get_headers(page1_url))
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    try:
        page_num = soup.find('div', {'class': 'pagenavi'}).find_all('a')[-2].find('span').get_text()
    except:
        return None
    return int(page_num)


def get_img_url(url):
    response = requests.get(url, headers=get_headers(url))
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    try:
        img_url = soup.find(
            'div', {'class': 'main-image'}).find('p').find('a').find('img')['src']
    except:
        return None

    # print(img_url)
    return img_url


def get_img_urls(page1_url):
    '''
    返回一个主题下 页面的url
    :param page1_url:
    :return:
    '''
    page_num = get_page_num(page1_url)
    # print(page_num)
    # 这里就用到了 上面的 get_page_num 这个函数了.
    if page_num is None:
        return None
    img_urls = []
    # 定义一个数组 来储存该主题下的 所有照片的 URL
    for page in range(1, page_num + 1):
        url = page1_url + '/' + str(page)
        # 实际照片的链接地址 就是主题的链接 + / + 数量
        img_url = get_img_url(url)
        img_urls.append(img_url)
        print(img_url)
        # 把获取到的 url 添加到 img_urls 这个数组里.
        # 这样循环下来 img_urls 数组里面就有该主题下的所有照片地址了

    return img_urls


def get_img_title(page1_url):
    response = requests.get(page1_url, headers=get_headers(page1_url))
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    # <h2 class="main-title">古典气质型美女施诗 顶级美腿加酥胸圆臀火辣身材性感十足</h2>
    title = soup.find('h2', {'class': 'main-title'}).get_text()
    # 下面两行是异常分析..
    removeSign = re.compile(r'[\/:*?"<>|]')
    # re 就是正则表达式模块
    # re.compile 把正则表达式封装起来. 可以给别的函数用. ()里面的才是真的 表达式.
    # r'[\/:*?"<>|]'
    # [] 表示一个字符集;  \对后面的进行转义 英文/是特殊符号; 其他的是正常符号.
    title = re.sub(removeSign, '', title)
    # re.sub 在字符串中 找到匹配表达式的所有子串. 用另一个进行替换.这里用'' 就是删除的意思.
    # 就是说 删除标题里面的 /:*?"<>| 这些符号.
    # 英文创建文件夹时候 不能有特殊符号的!!!
    return title


def download_imgs(page1_url):
    img_urls = get_img_urls(page1_url)
    print(img_urls)

    if img_urls is None:
        return None
    if not os.path.exists('./妹子图'):
        os.mkdir('./妹子图')
    title = get_img_title(page1_url)

    if title is None:
        return
    local_path = './妹子图/' + title
    if not os.path.exists(local_path):
        try:
            os.mkdir(local_path)
        except:
            pass
    if img_urls is None or len(img_urls) == 0:
        return
    else:
        print('--开始下载--' + title + '--')
        for img_url in img_urls:
            img_name = os.path.basename(img_url)
            print('正在下载 ' + img_name)
            print('from ' + img_url)
            # socket.setdefaulttimeout(10)
            try:
                # urllib.request.urlretrieve(img_url, local_path + '/' + img_name)
                with open(local_path + '/' + img_name, 'wb') as im:
                    im.write(requests.get(img_url, headers=get_headers(page1_url)).content)
            except:
                print('下载' + img_name + '失败')
        print('--' + title + '下载完成--')


def craw_meizitu():
    page1_urls = get_page1_urls()
    # 这里用到了 第一个函数. 也就是获取所有主题的 URL.
    if page1_urls is None or len(page1_urls) == 0:
        return
    else:
        for page1_url in page1_urls:
            # 循环第六步 来下载所有主题的URL
            print(page1_url)
            # download_imgs(page1_url)
        # download_imgs("https://www.mzitu.com/199492")


def main():
    craw_meizitu()


if __name__ == '__main__':
    main()
