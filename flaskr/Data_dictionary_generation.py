#auther:yyb
#time:2020/6/21
import pymongo
from flask import Flask
from flaskr import mongoDB
from pyhanlp import *
app = Flask(__name__)

user_name='yyb'
user_pwd='yyb@666'
client=pymongo.MongoClient(host='39.97.250.70',port=27017)
db=client.Pairr
db.authenticate(user_name,user_pwd,mechanism='SCRAM-SHA-1')
# 获取所有collections并打印，验证是否登录成功
coll_names = db.list_collection_names(session=None)
print("数据库："+coll_names[1])
collection_poemInfo=db.poemInfo
collection_Basic_dictionary=db.Basic_dictionary
print("成功")


l=collection_poemInfo.find().count()
print(l)

# poem_cursor = collection_poemInfo.find()
# for x in poem_cursor:
#    print(x)
#    id=x['_id']
#    print("ID:", id)

   # # 标题添加基础词典
   # poemname = x['poemname']
   # list_poemname = HanLP.extractKeyword(poemname, 50)
   # print("标题分词：",list_poemname)
   # # print("标题分词数量：",len(list_poemname))
   # for i in range(0,len(list_poemname)):
   #     basic_data=collection_Basic_dictionary.find_one({'Words': list_poemname[i]})
   #     if(basic_data==None):
   #         collection_Basic_dictionary.insert_one({"Words": list_poemname[i], "ID": [id]})
   #         print("没有该数据,已添加")
   #     else:
   #         if (list_poemname[i] == basic_data["Words"]):
   #           collection_Basic_dictionary.update_one({'Words':list_poemname[i]},{'$addToSet':{"ID":id}})
   #         print("更新数据")

   #         内容添加基础词典
   # content = x['content']
   # list_content = HanLP.extractKeyword(content, 50)
   # print("内容分词：",list_content)
   # # print("内容分词数量：",len(list_content))
   # for i in range(0,len(list_content)):
   #     basic_data=collection_Basic_dictionary.find_one({'Words': list_content[i]})
   #     if(basic_data==None):
   #         collection_Basic_dictionary.insert_one({"Words": list_content[i], "ID": [id]})
   #         print("没有该数据,已添加")
   #     else:
   #         if (list_content[i] == basic_data["Words"]):
   #           collection_Basic_dictionary.update_one({'Words':list_content[i]},{'$addToSet':{"ID":id}})
   #         print("更新数据内容")

           # 翻译添加基础词典
   # translate = x['translate']
   # list_translate = HanLP.extractKeyword(translate, 80)
   # print("翻译分词：",list_translate)
   # # print("翻译分词数量：",len(list_translate))
   # for i in range(0,len(list_translate)):
   #     basic_data=collection_Basic_dictionary.find_one({'Words': list_translate[i]})
   #     if(basic_data==None):
   #         collection_Basic_dictionary.insert_one({"Words": list_translate[i], "ID": [id]})
   #         print("没有该数据,已添加")
   #     else:
   #         if (list_translate[i] == basic_data["Words"]):
   #           collection_Basic_dictionary.update_one({'Words':list_translate[i]},{'$addToSet':{"ID":id}})
   #         print("更新数据翻译")

def find_dictionary(word):
    word_data=collection_Basic_dictionary.find_one({'Words': word})
    return word_data

def find_dictionary_id(word):
    ID=collection_Basic_dictionary.find_one({'Words': word})
    return ID
def find_poem(data_list,id):
    poem=collection_poemInfo.find_one({"_id": id})
    poemname = poem.get("poemname")
    dynasty = poem.get("dynasty")
    author = poem.get("author")
    content = poem.get("content")
    # translate=poem.get("translate")
    # nots=poem.get("nots")
    # appreciation=poem.get("appreciation")
    data_dict = {}
    data_dict.update({"poemname": poemname})
    data_dict.update({"dynasty": dynasty})
    data_dict.update({"author": author})
    data_dict.update({"content": content})
    # data_dict.update({"translate": translate})
    # data_dict.update({"nots": nots})
    # data_dict.update({"appreciation": appreciation})
    data_list.append(data_dict)
    return data_list