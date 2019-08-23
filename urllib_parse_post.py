# --------------------------
#          POST请求
# --------------------------
from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote  # 加密 解密
import simplejson

request = Request('http://httpbin.org/post')
request.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/76.0.3809.100 Safari/537.36"
)

data = urlencode(
    {
        'name': '张三,@=/d$%',
        'age': '18'
    }
)
print(data)

# res = urlopen(request, data='name=张三,@=/d$&age=18'.encode()) # 不做url编码有风险
res = urlopen(request, data=data.encode())  # POST方法,Form提交数据
with res:
    print(res.read())

