#auther:yyb
#time:2019/12/28
import pyhanlp
data="今夕何夕兮，搴舟中流。今日何日兮，得与王子同舟。蒙羞被好兮，不訾诟耻。心几烦而不绝兮，得知王子。山有木兮木有枝，心悦君兮君不知。"
list= pyhanlp.HanLP.extractKeyword(data, 20)
print(list)