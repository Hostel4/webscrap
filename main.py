import wget
import tkinter
from bs4 import BeautifulSoup

import requests
from tkinter import *
root = Tk()
root.geometry('500x400')
label=tkinter.Label(text="place your link here")
label.pack()
E1 = Entry(root)
E1.place(x=200,y=80)

def download_html():
    url = E1.get()

    r = requests.get(url)
    response = r.text
    soup = BeautifulSoup(response, 'html.parser')
    f1 = open('copy.html', 'w',encoding='utf-8')
    print(soup.prettify())
    for data in soup.prettify():
        f1.write(data)
    label1 = tkinter.Label(text="Your file is downloaded in ")
    label1.pack()
    label2 = tkinter.Label(text="C:\\Users\\ray85\\PycharmProjects\\webscrap\\copy.html")

    label2.pack()
    tags = soup.find_all('img')
    for img in tags:
        url_tags=url + img.get('src')
        print(url_tags)
        wget.download(url_tags)





Button=tkinter.Button(root,text="Extract Html and images" ,command=download_html,bg='blue')

Button.place(x=192,y=120)



root.mainloop()






