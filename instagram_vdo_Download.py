
import urllib.request
from urllib.request import Request, urlretrieve
from bs4 import BeautifulSoup
import random

url = input("Enter URL")
print("Video will be saved to C:/a")
def ig_vdo_download():
    req = Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    page = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page)
#     soup = BeautifulSoup(page,"lxml")
#     print (soup.head.meta)
#     print(soup.find_all('meta'))
#     print(soup.find_all(property="og:video"))
#     for i in soup.find_all(property="og:video"):
#         print (i['content'])
    vdo_url=soup.find_all(property="og:video")[0]['content']
    print (vdo_url)
    name = random.randint(0,10000)
    urlretrieve (vdo_url, "C:/a/"+str(name)+".mp4")

ig_vdo_download()
