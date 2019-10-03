from urllib.request import urlopen, Request
from http.client import HTTPResponse

url = 'https://www.gamersky.com/ent/wp/'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
             "AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/76.0.3809.100 Safari/537.36"

request = Request(url, headers={
    'User-agent': user_agent
})
response = urlopen(request)
# request.add_header('User-agent', user_agent)
# 二选一 皆可添加 请求头

print(response.closed)
with response:
    print(1, type(response))  # http.client.HTTPResponse 类文件对象
    print(2, response.status, response.reason)
    print(3, response.geturl())
    # print(4, response.info())
    print(5, response.read())


print(request.get_header('User-agent'))
print(response.closed)
