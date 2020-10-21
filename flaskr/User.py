import pymongo

user_name='yyb'
ser_name='yyb'
user_pwd='yyb@666'
client=pymongo.MongoClient(host='39.97.250.70',port=27017)
db = client.Pairr
db.authenticate(user_name, user_pwd,mechanism='SCRAM-SHA-1')
coll_names = db.list_collection_names(session=None)
collection=db.userInfo

class User():
    def __init__(self,phoneNumber):
        print('用户构造函数')
        self.username='广部'
        self.phoneNumber=phoneNumber
        self.password='6039'
        self.sex='男'
        self.age='20'
        self.signature='咚咚'
        self.position='濮阳市'
        self.dialog=[]
        self.qqOpenid =''
    def readfromDB(self):
        print('ReadFromDB Function')
        user_data=collection.find_one({'phoneNumber':self.phoneNumber})
        print(user_data)
        self.username=user_data['username']
        self.password = user_data['password']
        self.sex = user_data['sex']
        self.age = user_data['age']
        self.signature = user_data['signature']
        self.position = user_data['position']
        self.dialog=user_data['dialog']
        self.qqOpenid = user_data['qqOpenid']

def middleclass(phoneNumber):
    print('MiddleClass')
    user=User(phoneNumber)
    user.readfromDB()
    return user