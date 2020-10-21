#auther:yyb
#time:2020/7/31
# import efficientnet.keras as efn
# model=efn.EfficientNetB0(weights='imagenet')
# import efficientnet.tfkeras
# from tensorflow.keras.models import load_model
# model=load_model('D:/百度网盘/网盘下载/Pairr图像识别1.0版本/model.h5')
#
# import matplotlib.pyplot as plt  # plt 用于显示图片
# import matplotlib.image as mpimg  # mpimg 用于读取图片
# import numpy as np
#
# lena = mpimg.imread('tupian.jpg')  # 读取和代码处于同一目录下的 lena.png
# # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# lena.shape  # (512, 512, 3)
# plt.imshow(lena) # 显示图片
# plt.axis('off') # 不显示坐标轴
# plt.show()
#!/usr/bin/env python
# coding: utf-8

# xception
# index_to_lable={0: 'snake',
#  1: 'dragonfly',
#  2: 'butterfly',
#  3: 'cicada',
#  4: 'dragon',
#  5: 'caterpillar'}
#
# {0: 'beast',
#  1: 'flower',
#  2: 'human',
#  3: 'scenery',
#  4: 'weather',
#  5: 'bird',
#  6: 'water_animal',
#  7: 'insect',
#  8: 'tree'}
import json
import os
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import efficientnet.tfkeras
from tensorflow.keras.models import load_model
#efficientnet
index_to_lable_insect={0: '蝉',1: '中国龙',2: '蝴蝶',3: '蜻蜓',4: '蛇',5: '毛毛虫'}
index_to_lable_scenery={0: '山川',1: '古屋',2: '大海',3: '草原',4: '夕阳',5: '月景'}
index_to_lable_beast={0: '老鼠',1: '狮子',2: '猴子',3: '狗',4: '兔子',5: '骆驼',6: '狐狸',7: '老虎',8: '鹿',9: '马',10: '猪',11: '猫',
                      12: '熊',13: '狼',14: '象',15: '牛'}
index_to_lable_bird={0: '喜鹊',1: '黄鹂',2: '鹰',3: '鸭子',4: '白鹤',5: '乌鸦',6: '鸡',7: '麻雀',8: '鹅',9: '孔雀',10: '燕子'}
index_to_lable_flower={0: '向日葵',1: '玫瑰花',2: '桃花',3: '荷花',4: '菊花',5: '牡丹花'}
index_to_lable_human={0: '女人', 1: '男人', 2: '老人', 3: '小孩'}
index_to_lable_super={0: '人',1: '花',2: '动物',3: '树',4: '鸟',5: '风景',6: '昆虫',7: '天气',8: '水路两栖类'}
index_to_lable_weather={0: '风沙天气', 1: '雪', 2: '晴天', 3: '阴雨'}
index_to_lable_water={0: '鲨鱼', 1: '龟', 2: '青蛙', 3: '鲸鱼', 4: '锦鲤'}
index_to_lable_tree={0: '银杏树', 1: '柳树', 2: '竹子', 3: '松树'}


def load_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image,channels=3)
    image = tf.image.resize(image,[260,260])
    image = tf.cast(image,tf.float32)
    image = image/125.0-1
    return image
def check(my_image,my_model,index_to_lable):
    my_image = tf.expand_dims(my_image, 0)
    pred = my_model.predict(my_image)
    #print(index_to_lable[np.argmax(pred)],':',pred[0][np.argmax(pred)])
    return index_to_lable[np.argmax(pred)],pred[0][np.argmax(pred)]

def picture_Recognition():

    picture_path=os.path.abspath('..')+'/PairrService/pic.jpg'  #获取父目录路径
    picture_path=picture_path.replace('\\','/')
    print(picture_path)
    # path='D:/JAVA/Android Studio/android github/Pairr/PairrService/pic.jpg'
    my_image = load_preprocess_image(picture_path)
    plt.imshow(my_image)

    model_path=os.path.abspath('..')+'/PairrService/model_self'  #获取父目录路径
    model_super_path=model_path+'/9superb2.h5'
    model_super_path=model_super_path.replace('\\','/')
    print(model_super_path)
    model_super = load_model(model_super_path)
    option,rate = check(my_image,model_super,index_to_lable_super)
    print(option,rate)

    if option=='动物':
        print('111')
        model_beast_path = model_path + '/beastb2.h5'
        model_beast_path = model_beast_path.replace('\\', '/')
        model_beast=load_model(model_beast_path)
        Recognition_result=check(my_image,model_beast,index_to_lable_beast)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='鸟':
        model_bird_path = model_path + '/birdb2.h5'
        model_bird_path = model_bird_path.replace('\\', '/')
        model_bird=load_model(model_bird_path)
        Recognition_result=check(my_image,model_bird,index_to_lable_bird)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='花':
        model_flower_path = model_path + '/flowerb2.h5'
        model_flower_path = model_flower_path.replace('\\', '/')
        model_flower=load_model(model_flower_path)
        Recognition_result=check(my_image,model_flower,index_to_lable_flower)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='人':
        model_human_path = model_path + '/humanb2.h5'
        model_human_path = model_human_path.replace('\\', '/')
        model_human=load_model(model_human_path)
        Recognition_result=check(my_image,model_human,index_to_lable_human)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='昆虫':
        model_insect_path = model_path + '/insectb2.h5'
        model_insect_path = model_insect_path.replace('\\', '/')
        model_insect=load_model(model_insect_path)
        Recognition_result=check(my_image,model_insect,index_to_lable_insect)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='风景':
        model_scenery_path = model_path + '/sceneryb2.h5'
        model_scenery_path = model_scenery_path.replace('\\', '/')
        model_scenery=load_model(model_scenery_path)
        Recognition_result=check(my_image,model_scenery,index_to_lable_scenery)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label=[]
            for i in range(0, len(json_data['dependencies'])):
                 data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                 if(Recognition_result[0]==data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n=random.sample(list(data),3)
                    for j in n:
                      list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='树':
        model_tree_path = model_path + '/treeb2.h5'
        model_tree_path = model_tree_path.replace('\\', '/')
        model_tree=load_model(model_tree_path)
        Recognition_result=check(my_image,model_tree,index_to_lable_tree)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='水路两栖类':
        model_water_path = model_path + '/water_animal.h5'
        model_water_path = model_water_path.replace('\\', '/')
        model_water=load_model(model_water_path)
        Recognition_result=check(my_image,model_water,index_to_lable_water)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label
    elif option=='天气':
        model_weather_path = model_path + '/weather.h5'
        model_weather_path = model_weather_path.replace('\\', '/')
        model_weather=load_model(model_weather_path)
        Recognition_result=check(my_image,model_weather,index_to_lable_weather)
        with open('D:/JAVA/Android Studio/android github/Pairr/PairrService/flaskr/data_dictionary.json', 'r',
                  encoding='utf8')as fp:
            json_data = json.load(fp)
            list_label = []
            for i in range(0, len(json_data['dependencies'])):
                data = json_data['dependencies'][i]['data_name']  # 遍历数据数据
                if (Recognition_result[0] == data):
                    print(data)
                    data = json_data['dependencies'][0]['data']  # 产生随机数并获取数据
                    n = random.sample(list(data), 3)
                    for j in n:
                        list_label.append(data[j])
        print("Recognition_result数据：")
        list_label.append(Recognition_result[0])
        print(list_label)
        return list_label


# model_beast=load_model('F:/model/beastb2.h5')

# model_bird=load_model('F:/model/birdb2.h5')

# model_flower=load_model('F:/model/flowerb2.h5')

# model_human=load_model('F:/model/humanb2.h5')

# model_insect=load_model('F:/model/insectb2.h5')

# model_scenery=load_model('F:/model/flowerb2.h5')

# model_tree=load_model('F:/model/flowerb2.h5')

# model_water=load_model('F:/model/flowerb2.h5')

# model_weather=load_model('F:/model/flowerb2.h5')

# def get_swish(**kwargs):
#     backend, layers, models, keras_utils = get_submodules_from_kwargs(kwargs)
#
#     def swish(x):
#         """Swish activation function: x * sigmoid(x).
#         Reference: [Searching for Activation Functions](https://arxiv.org/abs/1710.05941)
#         """
#
#         if backend.backend() == 'tensorflow':
#             try:
#                 # The native TF implementation has a more
#                 # memory-efficient gradient implementation
#                 return backend.tf.nn.swish(x)
#             except AttributeError:
#                 pass
#
#         return x * backend.sigmoid(x)
#
#     return swish
#
#
# def get_dropout(**kwargs):
#     """Wrapper over custom dropout. Fix problem of ``None`` shape for tf.keras.
#     It is not possible to define FixedDropout class as global object,
#     because we do not have modules for inheritance at first time.
#     Issue:
#         https://github.com/tensorflow/tensorflow/issues/30946
#     """
#     backend, layers, models, keras_utils = get_submodules_from_kwargs(kwargs)
#
#     class FixedDropout(layers.Dropout):
#         def _get_noise_shape(self, inputs):
#             if self.noise_shape is None:
#                 return self.noise_shape
#
#             symbolic_shape = backend.shape(inputs)
#             noise_shape = [symbolic_shape[axis] if shape is None else shape
#                            for axis, shape in enumerate(self.noise_shape)]
#             return tuple(noise_shape)
#
#     return FixedDropout
