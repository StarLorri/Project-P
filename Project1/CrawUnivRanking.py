#e23.1CrawUnivRanking.py
import json
import requests
import bs4
from bs4 import BeautifulSoup

ulist = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.text)
        return r.text
    except:
        print("连接错误")
        return ""

def printUnivList(ulist, html, num):
    '''提取 html 网页内容中 前 num 名大学信息到 ulist列表中  '''
    data = json.loads(html)  # 对数据进行解码
    # 提取数据 rankings 包含的内容
    content = data['data']['rankings']

    # 把福建学校的相关信息放到ulist里面
    for i in range(num):
        if content[i]['province'] == '福建':
            index = content[i]['rankOverall']
            name = content[i]['univNameCn']
            score = content[i]['score']
            category = content[i]['univCategory']
            ulist.append([index, name, score, category])

    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t{4:^10}"  # {1:{3}^10} 中的 {3} 代表取第三个参数
    print(tplt.format("排名 ", "学校名称", "总分", chr(12288), "类型"))  # chr(12288) 代表中文空格
    # 打印前10名的大学
    for i in range(10):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288), u[3]))  # chr(12288) 代表中文空格

def main():
    #大学总数
    rankover = 581
    url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021'
    html = getHTMLText(url)
    printUnivList(ulist,html,rankover)

if __name__ == '__main__':
    main()
