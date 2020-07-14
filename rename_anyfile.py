from urllib.parse import parse_qsl
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import get as GET
import re
import os
import sys
import webbrowser

repository_mame = "C:/Users/USER/Downloads/H/pdf/[5/新しいフォルダー"

def idou(file):
    html = GET("https://www.google.co.jp/search?q={} 同人".format(file)).text
    bs = BeautifulSoup(html, 'lxml')
    print("\n"+"-"*15+file+"-"*15)
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[0].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[1].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[2].getText().strip())
    print(bs.find_all(class_="BNeawe vvjwJb AP7Wnd")[3].getText().strip())

    for el in bs.select("h3.r a"):
        #print(el)
        title = el.get_text()
        #url = dict(parse_qsl(urlparse(el.get("href")).query))["q"]
        print(title)
        #print(re.search(r"[", title))
        #print(title)
        #print("  ", url)
    z = input()
    if z == "a":
        pass
        webbrowser.open("https://www.google.co.jp/search?q={}+同人".format(file))
        z=""
        z = input()
        os.rename("{0}/{1}.pdf".format(repository_mame, file),
                  "C:/Users/USER/Downloads/H/pdf/[5/ido/[{0}] {1}.pdf".format(z, file))
    else:
        #os.rename("C:/Users/USER/Downloads/cg/5/{}.pdf".format(file),"C:/Users/USER/Downloads/cg/5/[{0}] {1}.pdf".format(z, file))
        os.rename("{0}/{1}.pdf".format(repository_mame, file),
                  "C:/Users/USER/Downloads/H/pdf/[5/ido/[{0}] {1}.pdf".format( z, file))


files = os.listdir("{0}".format(repository_mame))
for i in files:
    i = i[:-4]
    idou(i)

