#auther:yyb
#time:2019/12/25
import json
from flaskr import mongoDB,loginTest
from flask import Flask,request
from pyhanlp import *
import re

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi,There is A1005！'

@app.route('/serach',methods=['GET','POST'])
def serach():
    if request.method=='GET':
        print('俺进入GET方法啦')
        return '俺进入GET啦！'
    else:
        print('进入POST方法！')
        data = request.get_data()
        print('接收信息的类型为：',type(data))
        print('接收的信息：', data.decode("utf-8"))
        list = HanLP.extractKeyword(data, 20)
        print('List的类型为:',type(list))
        print('语义分析：', list)
        data_list = []
        for list_data in list:
            poem_cursor = mongoDB.collection.find({'label': list_data})
            for poem in poem_cursor:
                data_list = mongoDB.serach(data_list, poem)
        s = json.dumps(data_list, ensure_ascii=False)
        print('发送信息的类型为:',type(s))
        print('发送的消息：',s)
        return s

@app.route(('/login'),methods=['POST'])
def login():
    print('已进入登录验证界面！')
    data=request.get_data()
    userinfo=data.decode("utf-8")
    print('接收到的信息为：',userinfo)
    # 数据分割
    list=userinfo.split("&")
    print(list[1])
    print(list[0])
    password = re.sub("password=", '',list[0])
    phoneNumber = re.sub("phoneNumber=", '', list[1])

    print("开始搜索！")
    user = loginTest.collection.find_one({'phoneNumber': phoneNumber})
    print(user)
    if(user==None):
        return "用户不存在"
    user_password=user['password']
    if password==user_password:
        print("正确！")
        return "OK"
    else:
        print("错误！")
        return "NO"
@app.route(('/qqlogin'),methods=['POST'])
def login():
    print('已进入qq登录验证界面！')
    data=request.get_data()
    userinfo=data.decode("utf-8")
    print('接收到的信息为：',userinfo)
    result_qqOpenid=userinfo
    print(result_qqOpenid)
    print("开始搜索！")
    user=loginTest.collection.find_one({'qqOpenid':result_qqOpenid})
    print(user)
    if(user==None):
        loginTest.collection.insert({'qqOpenid':result_qqOpenid})
        print("插入成功啦！")
        return 'true'
    else:
        print("该用户已经存在了呢")
        return 'false'


if __name__ == '__main__':
    app.run()