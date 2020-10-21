#auther:yyb
#time:2019/12/26
import sys
import json
import base64


# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
# imagePath = r"D://Flask//Pairr_test//image_path//"
# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = 'KCRpdtqKNymFd0EwLN0vknr0'
SECRET_KEY = 'TBgdiKpZ2sSgxQTzdcB4XYFGvzVGiziC'
IMAGE_RECOGNIZE_URL = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
"""
    获取token
"""
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

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        print("打开文件")
        return f.read()
    except:
        print('read image file fail文件打开失败')
        return None
    finally:
        if f:
            f.close()

"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

"""
    调用菜品识别接口并打印结果
"""
def print_result(photobase64data, url):
    # 获取图片
    file_content = photobase64data
    response = request(url, urlencode(
        {
            'image': base64.b64encode(file_content),
            'top_num': 1
        }))
    result_json = json.loads(response)
    print(type(result_json))
    # 打印图片结果
    for data in result_json["result"]:
        print(type(data))
        print(u"  菜品名称: " + data["name"])
def photo(data):
    # 获取access token
    token = fetch_token()
    # 拼接图像识别url
    url = IMAGE_RECOGNIZE_URL + "?access_token=" + token
    # 菜品图1
    print("菜品1")
    print_result(data, url)

