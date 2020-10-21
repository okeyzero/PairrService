#auther:yyb
#time:2020/6/23

# # 训练模型
# import gensim
#
# print("1")
# from gensim.models import word2vec
# print("开始训练")
# sentences=word2vec.Text8Corpus("D:\\Flask\\数据上传\\All.txt")  #text8为语料库文件名
# print("读取文件")
# #sentences是训练所需预料，可通过该方式加载，此处训练集为英文文本或分好词的中文文本
# model=gensim.models.Word2Vec(sentences,sg=1,size=100,window=5,min_count=2,negative=3,sample=0.001,hs=1,workers=4)
# model.save("model")	#模型会保存到该 .py文件同级目录下，该模型打开为乱码
# #model.wv.save_word2vec_format("翻译训练3",binary = "Ture/False")  #通过该方式保存的模型，能通过文本格式打开，也能通过设置binary是否保存为二进制文件。但该模型在保存时丢弃了树的保存形式（详情参加word2vec构建过程，以类似哈夫曼树的形式保存词），所以在后续不能对模型进行追加训练
# print("保存完成")
# print("训练完成")



# # 生成语料库
# import pymongo
# from pyhanlp import HanLP
# user_name='yyb'
# user_pwd='yyb@666'
# client=pymongo.MongoClient(host='39.97.250.70',port=27017)
# db=client.Pairr
# db.authenticate(user_name,user_pwd,mechanism='SCRAM-SHA-1')
# # 获取所有collections并打印，验证是否登录成功
# coll_names = db.list_collection_names(session=None)
# print("数据库："+coll_names[1])
# collection_poemInfo=db.poemInfo
# print("成功")
#
# l=collection_poemInfo.find().count()
# print(l)
# poem_cursor = collection_poemInfo.find()
# with open ('D:\\Flask\\数据上传\\content.txt', 'wb') as f:
#     for x in poem_cursor:
#        # print(x)
#        translate = x['content']
#        list_translate = HanLP.extractKeyword(translate, 80)
#        n=len(list_translate)
#        print(n)
#        for word in list_translate:
#            # print(word+" ")
#            word_data=word+" "
#            print(word_data)
#            word_data=word_data.encode()
#            f.write(word_data)
# f.close()



# 加载模型
import gensim

print("1")
# model=gensim.models.Word2Vec.load("model")
#model = model.wv.load_word2vec_format('翻译训练')
# Y2=model.most_similar("大雁",topn=10)
# print(Y2)
# print(model["李白"])
# list_data=model.most_similar("荷花")
# print(list_data)
# print(type(list_data))
# print(len(list_data))
# print(list_data[0])
# print(type(list_data[0]))
# list1=[]
# list2=['杨亚斌']
# for i in range(0,len(list_data)):
#     list1.append(list_data[i][0])
#     print(list_data[i][0])
# print(list1)
# print(list1+list2)
# print(model.most_similar("收割"))
# print(model.most_similar("短袖衫"))
# print(model.similarity("天空","上天"))
print("输出完成")

def data_similar(str):
    model = gensim.models.Word2Vec.load("model")
    list = []
    try:
      list_model=model.most_similar(str)
    except Exception:
        print("基础词典没有",str)
        return list
    print(list_model)
    print(type(list_model))   #list类型[('凋敝', 0.9135234355926514), ('万籁俱寂', 0.9116435647010803), ('逾', 0.9105814099311829), ('世人', 0.907585859298706), ('满城', 0.9066942930221558), ('药', 0.9046663641929626), ('痾', 0.9030646681785583), ('老翁', 0.901869535446167), ('漳浦', 0.9001981019973755), ('词意', 0.8995852470397949)]
    print(list_model[0])      #list第一个元素 ('凋敝', 0.9135234355926514)是元组类型
    print(type(list_model[0])) #<class 'tuple'>
    for i in range(0, len(list_model)):  #遍历list个数
        list.append(list_model[i][0])    #将元组中第一个数据添加到新的list中
    print(list)
    return list   #返回list元素

def data_similarity(data1,data2):
    model = gensim.models.Word2Vec.load("model")
    Similarity=model.similarity(data1,data2)
    return Similarity