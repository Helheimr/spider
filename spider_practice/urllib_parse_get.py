# 网页采用utf-8编码
# https://www.baidu.com/s?wd=中
# 编码后，如下
# https://www.baidu.com/s?wd=%E4%B8%AD

from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote  # 加密 解密

keyword = input('>> 请输入搜索关键字')
data = urlencode({
    'wd': keyword
})

base_url = 'http://www.baidu.com/s'
url = '{}?{}'.format(base_url, data)
print(url)

print(unquote(url))  # 解码

# 伪装
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
             "AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/76.0.3809.100 Safari/537.36"

req = Request(url, headers={'User-agent': user_agent})
# request.add_header('User-agent', user_agent)
# 二选一 皆可添加 请求头

with urlopen(req) as res:
    # with open('./{}.html'.format(keyword), "wb+") as f:
    #     f.write(res.read())
    print(res.read())

print('成功')





