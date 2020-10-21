# auther:yyb
# time:2019/12/31
import xlwt
from pyhanlp import HanLP
import json
import os

filePath = 'D:\\Flask\\20多万诗词\\诗词json\\'     #诗词存放路径目录
j=0
while(j<len(os.listdir(filePath))):
    # print(os.listdir(filePath)[j])
    with open(filePath+os.listdir(filePath)[j], 'r',encoding='utf8') as f:   #打开文件
        data = f.read()
        data_json=json.loads(data)
        i=0
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('poet')
        while(i<len(data_json)):
            # 标题
            # print(HanLP.convertToSimplifiedChinese(data_json[i]['title']))
            print(data_json[i]['title'])
            sheet.write(i, 0, HanLP.convertToSimplifiedChinese(data_json[i]['title']))
            # 作者
            # print(HanLP.convertToSimplifiedChinese(data_json[i]['author']))
            sheet.write(i, 1,HanLP.convertToSimplifiedChinese(data_json[i]['author']))
            # 内容
            length=len(data_json[i]['paragraphs'])
            # print(type(length))
            l=0     #int型 print(type(l))
            str_content=""
            while(l<length):
              # print(HanLP.convertToSimplifiedChinese(data_json[i]['paragraphs'][l]))
              str_content=str_content+HanLP.convertToSimplifiedChinese(data_json[i]['paragraphs'][l])
              # print(type(str_content))
              l+=1
            # print(i)
            print(str_content)
            sheet.write(i, 2, HanLP.convertToSimplifiedChinese(str_content))
            i+=1
        work_book.save('诗词'+str(j)+'.xls')
    j+=1





