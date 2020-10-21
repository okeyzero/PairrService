#auther:yyb
#time:2020/1/8
import base64
import json
import random

import gensim

from flaskr import mongoDB, loginTest, User, Photo_Search
from flask import Flask,request
from pyhanlp import *
from urllib.parse import quote,unquote
from flaskr import advanced_general
from flaskr.Picture_Recognition import picture_Recognition

app = Flask(__name__)


class Poem():
    def __init__(self,poemname,dynasty,author,content):
        self.poemname=poemname
        self.dynasty=dynasty
        self.author=author
        self.content=content
        self.priority=1

@app.route('/')
def hello():
    return 'Hi,There is A1005！'

@app.route('/photo',methods=['GET','POST'])
def photo():
    if request.method=='GET':
        return '进入GET啦！'
    else:
        print('进入POST方法！')
        data = request.get_data()
        # print('接收信息的类型为：', type(data))
        # print('接收的信息：', data)
        # 转为string 类型
        data1 = data.decode('utf8')
        # print('转换的类型为：', type(data1))
        # url解码
        data2 = unquote(data1, 'utf-8')
        # print(data2)
        # print("data2类型",type(data2))
        # 分割
        for index in range(0,10):
            if(data2[index]=='/'):
                break
        data3 = data2[index:]
        print(data3)
        img=base64.b64decode(data3)    #保存图片
        fh=open("pic.jpg","wb")
        fh.write(img)
        fh.close()

        Recognition_result=picture_Recognition()
        # print(type(Recognition_result))
        # print(Recognition_result)
        getjsondata=list(Recognition_result)     #自己训练的图像识别
        # print(getjsondata)


        # getjsondata=advanced_general.photo(data3)     #百度识别
        print("得到的数据：",getjsondata)
        # print("得到的数据类型：",type(getjsondata))
        # 开始查找
        data_list = []
        for list_data in getjsondata:
            print(list_data)
            poem_cursor = mongoDB.collection.find({'label': list_data})
            # cursor类型
            for poem in poem_cursor:
                print(poem)
                poemname = poem.get("poemname")
                dynasty = poem.get("dynasty")
                author = poem.get("author")
                content = poem.get("content")
                x = Poem(poemname, dynasty, author, content)
                if (len(data_list) == 0):
                    data_list.append(x)
                else:
                    flag = False
                    for i in data_list:
                        # print('进行比对',i.poemname)
                        if (i.poemname == x.poemname):
                            i.priority = i.priority + 1
                            # print(i.priority)
                            # print('有一样的')
                            flag = True
                            break
                    if (flag == False):
                        # print('没有找到一样的')
                        data_list.append(x)
                # data_list = mongoDB.serach(data_list, poem)
            # print(data_list)
        if (len(data_list) == 0):
            print("没有找到相关搜索结果")
            print("END---")
            return "小编没有帮您找到结果"
        else:
            data_list.sort(key=lambda x: x.priority, reverse=True)
            poem_list = []
            for j in data_list:
                list_dict = {}
                list_dict.update({"poemname": j.poemname})
                list_dict.update({"dynasty": j.dynasty})
                list_dict.update({"author": j.author})
                list_dict.update({"content": j.content})
                # print(j.priority)
                poem_list.append(list_dict)
                result = json.dumps(poem_list, ensure_ascii=False)
            # print(result)
            print("END---")
            return result
        # 不排序的查询
        # data_list=[]
        # for list_data in getjsondata:
        #     poem_cursor = mongoDB.collection.find({'label': list_data})
        #     for poem in poem_cursor:
        #         data_list = mongoDB.serach(data_list, poem)
        #
        # s = json.dumps(data_list, ensure_ascii=False)
        # return s

        # 近义词查找的查询
        # data_list1=Photo_Search.First_search(getjsondata)
        # if(data_list1):
        #     s = json.dumps(data_list1, ensure_ascii=False)
        #     print("数据库数据：", s)
        #     return s
        # else:
        #     data_list2 = Photo_Search.Secondary_search(getjsondata)
        #     s = json.dumps(data_list2, ensure_ascii=False)
        #     print("数据库数据：", s)
        #     return s

@app.route('/serach',methods=['GET','POST'])
def serach():
    if request.method=='GET':
        print('俺进入GET方法啦')
        return '俺进入GET啦！'
    else:
        print('进入POST方法！')
        #data为接收到的数据
        data = request.get_data()
        # bytes类型
        # print('接收的信息为：',data)
        string_data=data.decode('utf-8')
        # print('转换后的信息为：',string_data)
        data_results=unquote(string_data,'utf-8')
        data_result=data_results.split('=')[1]
        # 分割
        print('经过处理得到的信息：',data_result)
        #采用HanLP的分词提取关键字
        list = HanLP.extractKeyword(data_result, 20)
        # print('List的类型为:',type(list))
        print('语义分析得到的结果：', list)
        if len(list)==0:
            print("没有分析出关键词")
            print("END---")
            return "您可以尝试改变一下搜索内容"
        # 结果字典
        data_list = []
        for list_data in list:
            print(list_data)
            poem_cursor = mongoDB.collection.find({'label': list_data})
            # cursor类型
            for poem in poem_cursor:
                print(poem)
                poemname = poem.get("poemname")
                dynasty = poem.get("dynasty")
                author = poem.get("author")
                content = poem.get("content")
                x=Poem(poemname,dynasty,author,content)
                if(len(data_list)==0):
                    data_list.append(x)
                else:
                    flag=False
                    for i in data_list:
                        # print('进行比对',i.poemname)
                        if(i.poemname==x.poemname):
                            i.priority=i.priority+1
                            print(i.priority)
                            print('有一样的')
                            flag=True
                            break
                    if(flag==False):
                        print('没有找到一样的')
                        data_list.append(x)
                # data_list = mongoDB.serach(data_list, poem)
            # print(data_list)
        if(len(data_list)==0):
            print("没有找到相关搜索结果")
            print("END---")
            return "小编没有帮您找到结果"
        else:
            data_list.sort(key=lambda x:x.priority,reverse=True)
            poem_list=[]
            for j in data_list:
                list_dict={}
                list_dict.update({"poemname": j.poemname})
                list_dict.update({"dynasty": j.dynasty})
                list_dict.update({"author": j.author})
                list_dict.update({"content": j.content})
                # print(j.priority)
                poem_list.append(list_dict)
                result=json.dumps(poem_list,ensure_ascii=False)
            print(result)
            print("END---")
            return result
        # s = json.dumps(data_list, ensure_ascii=False)
        # print('发送信息的类型为:',type(s))
        # print('发送的消息：',s)
        # return s
@app.route('/login',methods=['POST'])
def login():
    print('已进入登录验证界面！')
    data=request.get_data()
    userinfo=data.decode("utf-8")
    print('接收到的信息为：',userinfo)
    # 数据分割
    list=userinfo.split("&")
    result_phoneNumber = list[0].split('=')[1]
    result_password = list[1].split('=')[1]
    print(result_phoneNumber, result_password)

    # password = re.sub("password=", '',list[0])
    # phoneNumber = re.sub("phoneNumber=", '', list[1])
    print("开始搜索！")
    user = loginTest.collection.find_one({'phoneNumber': result_phoneNumber})
    print(user)
    if (user == None):
        return 'false'
        # return "您是不是还没注册呢"
    user_password = user['password']
    if result_password == user_password:
        print("正确！")
        return 'true'
    else:
        print("错误！")
        return 'false'

@app.route('/qqLogin',methods=['POST'])
def qqLogin():
    print('已进入qq登录验证界面！')
    data=request.get_data()
    userinfo=data.decode("utf-8")
    print('接收到的信息为：',userinfo)
    print(userinfo.rfind("=") + 1)
    result_qqOpenid=userinfo[userinfo.rfind("=") + 1:]
    print("开始搜索！"+result_qqOpenid)
    user = loginTest.collection.find_one({'qqOpenid': result_qqOpenid})
    print(user)
    if (user == None):
        loginTest.collection.insert({'qqOpenid':result_qqOpenid})
        print("插入成功啦！")
        return 'true'
        # return "您是不是还没注册呢"
    else:
        print("正确！")
        return 'true'

#注册功能，将正确的信息插入到用户数据库中
@app.route('/register',methods=['POST'])
def register():
    print('开始注册验证喽！')
    user_data=request.get_data().decode("utf-8");
    print('俺收到：',user_data)
    list = user_data.split("&")
    print(list)
    result_phoneNumber = list[0].split('=')[1]
    result_password = list[1].split('=')[1]
    print(result_phoneNumber, result_password)
    user=loginTest.collection.find_one({'phoneNumber':result_phoneNumber})
    print(user)
    if(user==None):
        loginTest.collection.insert({'phoneNumber':result_phoneNumber,'password':result_password})
        print("插入成功啦！")
        return 'true'
    else:
        print("用户已经存在了呢")
        return 'false'

#qq注册功能，将正确的信息插入到用户数据库中
# def qqregister(result_qqOpenid):
#     print('开始qq注册验证喽！'+result_qqOpenid)
#     # user_data=request.get_data().decode("utf-8");
#     # print('俺收到：',user_data)
#     # list = user_data.split("&")
#     # print(list)
#     # result_phoneNumber = list[0].split('=')[1]
#     # result_password = list[1].split('=')[1]
#     #result_qqOpenid=user_data
#     print(result_qqOpenid)
#     user=loginTest.collection.find_one({'qqOpenid':result_qqOpenid})
#     print(user)
#     if(user==None):
#         loginTest.collection.insert({'qqOpenid':result_qqOpenid})
#         print("插入成功啦！")
#         return 'true'
#     else:
#         print("该用户已经存在了呢")
#         return 'false'

#获取用户的所有信息 phoneNumber=XXX
@app.route('/inituser',methods=['POST'])
def initUser():
    print('返回用户信息')
    data = request.get_data()
    userinfo = data.decode("utf-8")
    print('接收到的信息为：', userinfo)
    phoneNumber = userinfo.split('=')[1]
    # str
    print(phoneNumber)
    flag=True
    user=User(phoneNumber)
    flag=user.readfromDB()
    if(flag==False):
        return '无此用户'
    user_dict=user.printf()
    return user_dict

#用户数据的修改
@app.route('/update',methods=['POST'])
def update():
    print("这里是update：")
    data=request.get_data().decode("utf-8")
    print(data)
    user=json.loads(data)
    # 分别提取属性进行更新
    # print(user['name'])
    query={"phoneNumber":user['phoneNumber']}
    newValues={"$set":user}
    loginTest.collection.update_one(query,newValues)
    update_result=loginTest.collection.find_one({"phoneNumber":user['phoneNumber']})
    print("修改后的数据：",update_result)
    return "修改成功！"
#获取注册界面的验证码
@app.route('/verification',methods=['POST'])
def verification():
    print('开始获取注册界面的验证码')
    seeds = "1234567890"
    random_num =[]
    for i in range(4):
        random_num.append(random.choice(seeds))
    id ="".join(random_num)
    print(random_num)
    print(id)
    return id
if __name__ == '__main__':
    app.run()