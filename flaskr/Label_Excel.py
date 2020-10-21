import pymongo
import xlwt

client=pymongo.MongoClient(host='39.97.250.70',port=27017)
db=client.Pairr
collection=db.PoemInfo

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet('label')

cursor=collection.find()
row=0
cow=0
for i in cursor:
    print(i['label'])
    # print(len(i['label']))
    for j in i['label']:
        worksheet.write(row,cow,j)
        print(row,cow)
        print("插入成功!")
        cow+=1
        print(j)
    row+=1
    cow=0
workbook.save('.xls')