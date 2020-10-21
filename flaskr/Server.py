# # # coding:utf-8
# # import socket
# # from flaskr import mongoDB
# # import json
# # import logging
# # from pyhanlp import *
# #
# # BUFSIZE = 4096  #设置缓冲区大小
# # tcpServerSocket = socket.socket()  # 1.创建
# # hostip = '10.133.129.55'     #120.24.216.203  手机192.168.123.9    电脑192.168.108.1
# # port = 5000
# # tcpServerSocket.bind((hostip, port))  # 2.bind
# # tcpServerSocket.listen(10)  # 监听，设置等待队列最大数目
# # while True:
# #     logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# #     print("等待连接...")
# #     clientSocket, addr = tcpServerSocket.accept()  # 3.接收连接请求，并获得ip和端口号
# #     # while True:
# #     data = clientSocket.recv(BUFSIZE).decode()  # 4.接收数据
# #     print('接收值:',data)
# #     # 关键词提取
# #     list=HanLP.extractKeyword(data, 20)
# #     print("分词结果：",list)
# #     data_list = []
# #     for list_data in list:
# #         poem_cursor = mongoDB.collection.find({'label': list_data})
# #         for poem in poem_cursor:
# #             data_list = mongoDB.serach(data_list, poem)
# #     if not data:
# #         break
# #     s = json.dumps(data_list,ensure_ascii=False)
# #     print('返回值：',s)
# #     clientSocket.send(s.encode())  # 5.发送数据
# #     print('重新建立连接....')
# #
# #     clientSocket.close()
#
# import json
# import socket
#
# import pyhanlp
# import pymongo
#
# BUFSIZE = 4096  # 设置缓冲区大小
# tcpServerSocket = socket.socket()  # 1.创建
# hostip = '192.168.43.195'  # 120.24.216.203  手机192.168.123.9    电脑192.168.108.1、、39.97.250.70
# port = 5000
# tcpServerSocket.bind((hostip, port))  # 2.bind
# tcpServerSocket.listen(10)  # 监听，设置等待队列最大数目
#
# client = pymongo.MongoClient(host='39.97.250.70', port=27017)
# db = client.Pairr
# collection = db.PoemInfo
# count = 0
#
#
# def serach(data_list, poem):
#     poemname = poem.get("poemname")
#     dynasty = poem.get("dynasty")
#     author = poem.get("author")
#     content = poem.get("content")
#     data_dict = {}
#     data_dict.update({"poemname": poemname})
#     data_dict.update({"dynasty": dynasty})
#     data_dict.update({"author": author})
#     data_dict.update({"content": content})
#     data_list.append(data_dict)
#     return data_list
#
#
# while True:
#     # logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
#     print("等待连接...")
#     clientSocket, addr = tcpServerSocket.accept()  # 3.接收连接请求，并获得ip和端口号
#     data = clientSocket.recv(BUFSIZE).decode()  # 4.接收数据
#     print('接收值:', data)
#     data_content = data.split("&")
#     print(type(data_content[0]))
#     print(data_content[1])
#     # 关键词提取
#     list= pyhanlp.HanLP.extractKeyword(data_content[0], 20)
#     print("分词结果：",list)
#     data_list = []
#     for list_data in list:
#          poem_cursor = collection.find({'label': list_data}).limit(5)
#          print("list-data:",list_data)
#          # print("poem-cursor:",poem_cursor)
#          for poem in poem_cursor:
#              print("poem:",poem)
#              data_list =serach(data_list, poem)
#     if not data:
#       break
#     count = int(data_content[1]) + 5
#     print(count)
#
#
#     # data_list = []
#     # poem_cursor = collection.find({'label': data}).limit(5)
#     # for poem in poem_cursor:
#     #     data_list = serach(data_list, poem)
#     s = json.dumps(data_list, ensure_ascii=False)
#
#
#     print('返回值：', s)
#     clientSocket.send(s.encode())  # 5.发送数据
#
#     print('重新建立连接....')
#
#     clientSocket.close()

# 标签依据逗号分开用于提取数据词典用来匹配诗词
# import re
# import xlrd
# # 打开文夹
# from xlwt import Workbook
# data = xlrd.open_workbook('D:/Flask/数据上传/标签.xlsx')
# # 查看工作表
# data.sheet_names()
# print("sheets：" + str(data.sheet_names()))
# # 通过文件名获得工作表,获取工作表1
# table = data.sheet_by_name('Sheet1')
# # 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
# # table = data.sheet_by_index(0)
# # 获取行数和列数
# # 行数：table.nrows
# # 列数：table.ncols
# print("总行数：" + str(table.nrows))
# print("总列数：" + str(table.ncols))
# work_book = Workbook()
# ws = work_book.add_sheet('datas')
# n=1
# nw = 0
# while(int(n)<table.nrows):
#     cel_Bn = table.cell(n,0).value
#     # print(type(cel_B3))
#     # print("第"+n+"行第0列的值：" + cel_Bn)
#     cel_Bn_split=re.split('，',cel_Bn)
#     print(cel_Bn_split)
#     nl = 0
#     for i in cel_Bn_split:
#         ws.write(nw, nl,i)
#         nl+=1
#         print(i)
#     nw+=1
#     work_book.save('D:\Flask\数据上传\标签分开1.xls')
#     n+=1

# import json
# import random
#
# with open('../json/data_dictionary.json','r',encoding='utf8')as fp:
#     json_data = json.load(fp)
#     # print(len(json_data['dependencies']))
#     for i in range(0,len(json_data['dependencies'])):
#         data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
#         if("风景"==data):
#             print(data)


    # data=json_data['dependencies'][0]['data']  #产生随机数并获取数据
    # n=random.sample(list(data),3)
    # for i in n:
    #     print(data[i])
    # print(n)
    # print('这是文件中的json数据：',json_data)
    # print('这是读取到文件数据的数据类型：', type(json_data))
#格式化json文件
# import re
# import xlrd
# # 打开文夹
# from xlwt import Workbook
# data = xlrd.open_workbook('C:/Users/杨亚斌/Desktop/标签分类.xlsx')
# # 查看工作表
# data.sheet_names()
# print("sheets：" + str(data.sheet_names()))
# # 通过文件名获得工作表,获取工作表1
# table = data.sheet_by_name('Sheet1')
# # 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
# # table = data.sheet_by_index(0)
# # 获取行数和列数
# # 行数：table.nrows
# # 列数：table.ncols
# print("总行数：" + str(table.nrows))
# print("总列数：" + str(table.ncols))
# # cel_Bn = table.cell(1,1).value  # print("第"+n+"行第0列的值：" + cel_Bn)
# for j in range(0,table.nrows):  #行
#     n = 0
#     for i in range(1,table.ncols):  #列
#       cel_Bn = table.cell(j, i).value
#       print("\""+str(n)+"\""+":"+"\""+cel_Bn+"\""+",")
#       n+=1

