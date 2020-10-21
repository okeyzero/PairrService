#auther:yyb
#time:2019/12/25
from flask import Flask
import pymongo


app = Flask(__name__)


user_name='yyb'  #数据库用户密码：yyb yyb@666
user_pwd='yyb@666'
client=pymongo.MongoClient(host='39.97.250.70',port=27017)
db = client.Pairr
db.authenticate(user_name, user_pwd,mechanism='SCRAM-SHA-1')
coll_names = db.list_collection_names(session=None)
collection=db.userInfo

@app.route('/')
def hello():
    return 'Hi,This is Login！'


@app.route('/login')
def login():
    return ;


if __name__ == '__main__':
    app.run()
