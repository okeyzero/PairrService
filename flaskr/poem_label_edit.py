#auther:yyb
#time:2020/4/16
import xlrd
from xlutils.copy import copy
import pymongo

user_name='yyb'
user_pwd='20161121bin'
client=pymongo.MongoClient(host='39.96.47.228',port=27017)
print("成功1")
db=client.Pairr
print("成功2")
db.authenticate(user_name,user_pwd,mechanism='SCRAM-SHA-1')
print("成功3")
# 获取所有collections并打印，验证是否登录成功
coll_names = db.list_collection_names(session=None)
collection_poemInfo=db.poemInfo
print("成功4")
# 上传前检查label中的间隔是否为英文逗号
filePath = 'D:\\Flask\\数据上传\\诗词.xls'
file = xlrd.open_workbook(filePath)
# 输出Excel中表的个数
print(file.nsheets)
# 读取某张表
sheet = file.sheet_by_name("Sheet1")
# 获取表的行数
nrows = sheet.nrows
# 获取表的列数
ncols = sheet.ncols
print("nrows: %d, ncols: %d" % (nrows, ncols))
datalist=[]
for i in range(2,nrows):
    # 定义list列表
    poemname=sheet.cell_value(i, 0)  # 获取第2行第5列的数据
    dynasty= sheet.cell_value(i,1)
    author=sheet.cell_value(i, 2)
    content= sheet.cell_value(i, 3)
    label= sheet.cell_value(i, 4)
    labeldata=label.split(",")#利用分割 吧str类型转变为list
    print(type(label))
    print(type(labeldata))
    print(labeldata)
    translate= sheet.cell_value(i, 5)
    notes= sheet.cell_value(i, 6)
    appreciation= sheet.cell_value(i, 7)
    mydict = { "poemname": poemname, "dynasty": dynasty, "author": author,"content":content,"label":labeldata,"translate":translate,"notes":notes,"appreciation":appreciation }
    datalist.append(mydict)
print(len(datalist))
print(type(mydict))
print(datalist)
x = collection_poemInfo.insert_many(datalist)
print(x.inserted_ids)










# 修改数据
# filePath = 'D:\\Flask\\数据上传\\诗词.xls'
#
# data= xlrd.open_workbook(filePath)  #接收excel表格数据
# print("已找到要修改的Excel表格！！！")
# table = data.sheets()[0]  #旧表数据
# newWb = copy(data)               #利用xlutils.copy下的copy函数复制
# ws = newWb.get_sheet(0)   #获取表单0
# i=1   #第二列开始为需要改的数据 0是第一行
# while i<table.nrows:
#     # print(table.cell(i,4))
#     ws.write(i, 4, '["'+table.cell(i,4).value+'"]')             #改变（0,0）的值
#     i=i+1
#     print("已修改了第%d条信息！！！" %i)
# newWb.save(filePath)
# print("修改完成！！！")
