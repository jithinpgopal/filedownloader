
import urllib.request
from urllib.request import Request, urlretrieve
from bs4 import BeautifulSoup
import random
import re


class instagram():
    def vdo_download(self):    
        url=input("Enter Video URL")
        req = Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
        page = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(page,features="html.parser")
    #     soup = BeautifulSoup(page,"lxml")
    #     print(soup.find_all(property="og:video"))
    #     for i in soup.find_all(property="og:video"):
    #         print (i['content'])
        vdo_url=soup.find_all(property="og:video")[0]['content']
        print ("Downloading : "+ vdo_url)
        name = random.randint(0,10000)
        urlretrieve (vdo_url, "C:/a/"+str(name)+".mp4")
    
    def image_download(self):
        url=input("Enter Image URL")    
        req = Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
        page = urllib.request.urlopen(req).read().decode('utf-8')
#         print((page))
        p=re.findall(r'.src.*jpg.*config_height', page)
        q=str(p[0]).split('src')
        r=q[len(q)-1][3:-36]
        print("Downloading : "+ r)
        name = random.randint(0,10000)
        urlretrieve (r, "C:/a/"+str(name)+".jpg")
        
ig1 = instagram()

useri = input ("1:Image   2:video   0:Exit")
while useri!="0":
    if useri == "1":
        ig1.image_download()
    elif useri == "2":
        ig1.vdo_download()
    else :
        print ("Wrong choice")
    useri = input ("1:Image   2:video   0:Exit")
