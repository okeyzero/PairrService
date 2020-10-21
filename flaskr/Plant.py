#auther:yyb
#time:2019/12/26
import json
import sys
from urllib.parse import urlencode

import requests
import base64
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

API_KEY = 'KCRpdtqKNymFd0EwLN0vknr0'

SECRET_KEY = 'TBgdiKpZ2sSgxQTzdcB4XYFGvzVGiziC'


IMAGE_RECOGNIZE_URL = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

# 二进制方式打开图片文件
f = open('./image/animal1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token =fetch_token() #'[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)

if response:
    print (response.json())

#
#     result_json = json.loads(response)
#
# # 打印图片结果
# for data in result_json["result"]:
#     print(u"  植物名称: " + data["name"])