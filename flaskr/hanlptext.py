#auther:yyb
#time:2020/5/15
from pyhanlp import *


content = "风景，人物，山水";
phraseList = HanLP.extractPhrase(content, 10)
print(phraseList)
