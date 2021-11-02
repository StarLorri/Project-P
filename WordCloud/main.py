import jieba.posseg as psg
import string
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageSequence
from wordcloud import WordCloud,ImageColorGenerator
def process(text):
    wList = []
    cList = psg.cut(text)
    for x,y in cList:
        if y in['n','nr','nz']:
            wList.append(x)
    return wList

def count(wlist):
    wDict = {}
    for w in wlist:
        if len(w) >1:
            wDict[w] = wDict.get(w,0)+1
    return wDict

def sort(wDict):
    sList = list(wDict.items())
    sList.sort(key = lambda x:x[1],reverse=True)
    return sList

def showCLoud(wDict):
    ima = Image.open("image.jpg")
    graph = np.array(ima)
    wc = WordCloud(max_words=15,mask=graph,background_color='white',font_path="/System/Library/fonts/PingFang.ttc")
    wc.generate_from_frequencies(wDict)
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis('off')
    plt.show()
    wc.to_file('home.png')

with open('text.txt', 'r',encoding='utf-8')as file:
    text=file.read()
    wList = process(text)
    wDict = count(wList)
    result = sort(wDict)
    print('{0:^15}{1:>5}'.format('word','freq'))
    for i in range(15):
        w,f = result[i]
        print('{0:^15}{1:>7}'.format(w, f))
    showCLoud(wDict)

