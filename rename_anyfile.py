"""
Search for the file name in google and add it to the file name.
ex)
input OnePiece.pdf
output [尾田 栄一郎] OnePiece.pdf
"""
#pip install lxml
from urllib.parse import parse_qsl
from urllib.parse import urlparse
#pip install beautifulsoup4
from bs4 import BeautifulSoup
#pip install requests
from requests import get as GET
import re
import os
import sys
import webbrowser

#The folder with the files you want to search. Multiple files are possible.
folder_name="C:/Users/USER/Downloads/book" 
#Keywords related to the file (to improve search hits) 
keyword="manga"


def idou(file,ext):
    html = GET("https://www.google.co.jp/search?q={0} {1}".format(file,keyword)).text
    bs = BeautifulSoup(html, 'lxml')
    print("\n"+"-"*15+file+"-"*15)
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[0].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[1].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[2].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[3].getText().strip())

    for el in bs.select("h3.r a"):
        title = el.get_text()
        print(title)
    add_name = input()
    if add_name == "a":
        pass
        webbrowser.open("https://www.google.co.jp/search?q={0}+{1}".format(file,keyword))
        add_name=""
        add_name = input()
        os.rename("{0}/{1}{2}".format(folder_name,file,ext),
                  "{0}/[{1}] {2}{3}".format(folder_name,add_name, file,ext))
    else:
        os.rename("{0}/{1}{2}".format(folder_name,file,ext),
            "{0}/[{1}] {2}{3}".format(folder_name,add_name, file,ext))

if __name__ == '__main__':
    files = os.listdir(folder_name)
    for _name in files:
        root_ext = os.path.splitext(_name)[1]
        cnt_ext=int(len(root_ext))
        if cnt_ext>0:
            _name = _name[:-1*cnt_ext]
        idou(_name,root_ext)
