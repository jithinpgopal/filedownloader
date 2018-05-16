import urllib.request
from urllib.request import Request, urlopen

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
urllib.request.install_opener(opener)


def convert_string(value):
    new_value = str(value)
    return new_value
#sequence identifier
def down_seq():
    download_path = input("Enter your input path(example : c:/my_folder ):")
    print("Url format : http://www.example.com/imageseq_no.jpg for downloading www.example.com/image1.jpg ... www.example.com/image100.jpg " )
    url = input("enter your file path with \"seq_no\" in place of the numbers" )
    nstart= int(input("Enter the starting number"))
    nend= int(input("Enter the ending number"))
    starting_file = url.replace("seq_no", str(nstart))
    ending_file = url.replace("seq_no", str(nend))
    print ("Starting file :"+starting_file)
    print("Ending File : "+ending_file)
    for i in range(nstart,nend+1):
        nurl=url.replace("seq_no", str(i))
#         print(nurl)
        down_file(nurl,download_path)

#File downloader
def down_file(fqurl,download_path):
    filename=fqurl.split('/')[-1] 
    print(filename)
    try:
        print("Downloading " + fqurl)
        urllib.request.urlretrieve(str(fqurl),download_path+"/"+filename)
        print ("Downloaded ")
#     except urllib.error.HTTPError:
#         print("Error: Forbidden")
    except Exception as de:
        print("Error: " + str(de))   

down_seq()
