import requests
from bs4 import BeautifulSoup
import bs4
def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('响应失败')
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#过滤掉非tag类型
            tds = tr.find_all('td')#tds为tr标签的列表
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
def displayUivList(ulist,num):
    tqlt = "{0:^10}\t{1:{3}^10}\t{2:^10}"#控制中文对齐
    print(tqlt.format('排名','学校','分数',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tqlt.format(u[0],u[1],u[2],chr(12288)))
    print('Suo'+str(num))
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHtmlText(url)
    fillUnivList(uinfo,html)
    displayUivList(uinfo,20)
main()