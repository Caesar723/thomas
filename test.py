from urllib import request
from bs4 import BeautifulSoup
from openpyxl import Workbook
arr=[]
def get(a):
    url="http://sh.thomas.pte.sh.cn/info/iList.jsp?cat_id=3048&cur_page="+str(a)
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    req=request.Request(url,headers=header)
    response=request.urlopen(req)
    #print(type(response))
    #print(response.getcode())
    data = response.read()
    data=str( data,encoding="utf-8")
    #print(data)
    with open('in.html',mode="w",encoding="utf-8") as f:
        f.write(data)

def parse(n):
    with open('in.html', mode="r", encoding="utf-8") as f:
        html=f.read()
    be=BeautifulSoup(html,"html.parser")
    #be.find()
    title=be.find_all(class_='newsbiaoti')[n].get_text(strip=True)
    time=be.find_all(class_='newsshij')[n].get_text(strip=True)
    arr.append([title,time])

def excel():
    book=Workbook()
    sheet=book.create_sheet("托马斯旧闻",0)
    sheet.append(["题目","时间"])
    for iii in range(0,len(arr)):
        sheet.append(arr[iii])
    book.save("tms.xlsx")

#get()
#parse()
for i in range(1,11):
    get(i)
    if i==10:
        for iiii in range(3):
            parse(iiii)
    else:
        for ii in range(9):
            parse(ii)
excel()