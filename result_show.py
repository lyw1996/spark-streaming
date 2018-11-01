from wordcloud import WordCloud,ImageColorGenerator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # 动图的核心函数
import seaborn as sns  # 美化图形的一个绘图包
import jieba
import numpy as np
from PIL import Image
import os
import time

#生成词云
def wordcloud(all_comments,i,time):
    # 对句子进行分词，加载停用词
    # 打开和保存文件时记得加encoding='utf-8'编码，不然会报错。
    def seg_sentence(sentence):
        sentence_seged = jieba.cut(sentence.strip(), cut_all=False)  # 精确模式
        stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]  # 这里加载停用词的路径
        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr
    for line in all_comments:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        with open('outputs'+str(i)+'.txt', 'a', encoding='utf-8') as f:
            f.write(line_seg + '\n')

    data = open('outputs'+str(i)+'.txt', 'r', encoding='utf-8').read()
    #data_counts=collections.Counter(data)
    ###自定义图片生成词云
    image = Image.open(r'C:\Users\Administrator\Desktop\taiguo.jpg')
    img = np.array(image)
    my_wordcloud = WordCloud(
        background_color='white',  #设置背景颜色
        max_words=200,  #设置最大实现的字数
        font_path='simhei.ttf',
        mask=img
        # font_path=r'SimHei.ttf',  #设置字体格式，如不设置显示不了中文
    ).generate(data)
    image_colors = ImageColorGenerator(img)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    #文本词频统计函数，本函数自动统计词的个数，以字典形式内部存储，在显示的时候词频大的，字体也大
    plt.ion()
    fig=plt.figure(time)
    #fig=plt.gcf()
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.pause(3)
    plt.show()
    fig.savefig('F:\研一上\云计算\第一次实践作业\wordcloud\\'+str(time)+'.png',dpi=1000,bbox_inches = 'tight')
    plt.close()

f1=open('F:\simulate-hdfs\\noteThailand1540774839.4040117.log','r',encoding='utf-8')
lista=[]
for line in f1:
    each = line.split('\t')[0]
    print(each)
    lista.append(each)
print(type(lista))
now='Thailand'
wordcloud(lista,1,now)
#让时间戳变成时间
#生成柱状图
# def barShow():
#     name_list = ['2013','2014','2015']
#     num_list = [2000, 4000, 3000]
#     plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
#     plt.pause(5)
#     plt.show()

# rootdir = 'D:\homework\\tmp'##评论文件夹
# list = os.listdir(rootdir) #列出该文件夹下所有的目录与文件
# i=0
# for i in range(0,len(list)):
#     path = os.path.join(rootdir,list[i]) #把目录和文件名合成一个路径
#     if os.path.isfile(path):#判断路径是否为文件
#        ##读文件操作
#        f=open(path,'r',encoding='utf-8')
#        lines=f.readlines()
#        comments=[]
#        time=0
#        for line in lines:
#            each=line.split('\t')[0]
#            time=line.split('\t')[1].strip('\n')
#            comments.append(each)
#       # wordcloud(comments,i,time)
#        #time.sleep(3)
# barShow()
##按时间统计文件夹，文件内容为(k,v)时间，评论数形式

'''
from wordcloud import WordCloud
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # 动图的核心函数
import seaborn as sns  # 美化图形的一个绘图包
import jieba
import os
import time

#生成词云
def wordcloud(all_comments,i,time):
    # 对句子进行分词，加载停用词
    # 打开和保存文件时记得加encoding='utf-8'编码，不然会报错。
    def seg_sentence(sentence):
        sentence_seged = jieba.cut(sentence.strip(), cut_all=False)  # 精确模式
        stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]  # 这里加载停用词的路径
        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr
    for line in all_comments:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        with open('outputs'+str(i)+'.txt', 'a', encoding='utf-8') as f:
            f.write(line_seg + '\n')

    data = open('outputs'+str(i)+'.txt', 'r', encoding='utf-8').read()
    #data_counts=collections.Counter(data)
    my_wordcloud = WordCloud(
        background_color='white',  #设置背景颜色
        max_words=200,  #设置最大实现的字数
        font_path=r'SimHei.ttf',  #设置字体格式，如不设置显示不了中文
    ).generate(data)
    #文本词频统计函数，本函数自动统计词的个数，以字典形式内部存储，在显示的时候词频大的，字体也大
    plt.ion()
    fig=plt.figure(time)
    #fig=plt.gcf()
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.pause(3)
    fig.savefig('D:\homework\images\\'+str(time)+'.png',dpi=100,bbox_inches = 'tight')
    plt.close()
#让时间戳变成时间
#生成柱状图
def barShow():
    name_list = ['2013','2014','2015']
    num_list = [2000, 4000, 3000]
    plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
    plt.pause(5)
    plt.show()

rootdir = 'D:\homework\\tmp'##评论文件夹
list = os.listdir(rootdir) #列出该文件夹下所有的目录与文件
i=0
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i]) #把目录和文件名合成一个路径
    if os.path.isfile(path):#判断路径是否为文件
       ##读文件操作
       f=open(path,'r',encoding='utf-8')
       lines=f.readlines()
       comments=[]
       time=0
       for line in lines:
           each=line.split('\t')[0]
           time=line.split('\t')[1].strip('\n')
           comments.append(each)
      # wordcloud(comments,i,time)
       #time.sleep(3)
barShow()
##按时间统计文件夹，文件内容为(k,v)时间，评论数形式



'''
