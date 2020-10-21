#auther:yyb
#time:2020/7/13
import json

from flaskr import Data_dictionary_generation, Word2vec


def First_search(list1):
    model_l=len(list1)
    data_list = []
    for i in range(0, model_l):
        try:
            Data_dictionary_generation.find_dictionary(list1[i])
        except Exception:
            i += 1
        else:
            dictionary_data_ID = Data_dictionary_generation.find_dictionary_id(list1[i])
            if (dictionary_data_ID == None):
                print("没找到")
                return data_list
                # break
            else:
                dictionary_data_ID = dictionary_data_ID["ID"]
                print(dictionary_data_ID)
                print(len(dictionary_data_ID))
                print(type(dictionary_data_ID))
                for n in range(0, len(dictionary_data_ID)):
                    print(dictionary_data_ID[n])
                    data_list = Data_dictionary_generation.find_poem(data_list, dictionary_data_ID[n])
                # s = json.dumps(data_list, ensure_ascii=False)
                # print("数据库数据：", s)
                return data_list
def Secondary_search(list1):
    model_l = len(list1)
    data_list = []
    print("一级查找有点差劲,进入二级查找")
    data_similar_list = []
    for i in range(0, model_l):
        data_similar_list += Word2vec.data_similar(list1[i])  # 得到list元素
    data_similar_list_len = len(data_similar_list)
    for j in range(0, data_similar_list_len):
        try:
            Data_dictionary_generation.find_dictionary(data_similar_list[j])
        except Exception:
            j += 1
        else:
            dictionary_data_ID = Data_dictionary_generation.find_dictionary_id(data_similar_list[j])
            if (dictionary_data_ID == None):
                print("没找到")
                return data_list
            else:
                dictionary_data_ID = dictionary_data_ID["ID"]
                print(dictionary_data_ID)
                print(len(dictionary_data_ID))
                print(type(dictionary_data_ID))

                for n in range(0, len(dictionary_data_ID)):
                    print(dictionary_data_ID[n])
                    data_list = Data_dictionary_generation.find_poem(data_list, dictionary_data_ID[n])
                # s = json.dumps(data_list, ensure_ascii=False)
                # print("数据库数据：", s)
                return data_list