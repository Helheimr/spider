from urllib.parse import urlencode
from urllib.request import urlopen, Request

url = "https://movie.douban.com/j/search_subjects"

request = Request(url)
request.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/76.0.3809.100 Safari/537.36"
)

data = urlencode({
    'type': 'movie',
    'tag': '热门',
    'page_limit': 50,
    'page_start': 0
})

# POST方法
res = urlopen(request,data=data.encode())
with res:
    print(res._method)
    print(res.read().decode())

# GET方法
with urlopen('{}?{}'.format(url,data)) as res:
    print(res._method)
    print(res.read().decode())