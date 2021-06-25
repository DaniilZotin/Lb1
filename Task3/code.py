import http.client
import json
from tkinter import *

win = Tk()
w = 1300
h = 600
win.geometry(f"{w}x{h}-10+10")
win.title('Статистика корони')
win['bg'] = '#E20D0D'


#pole = Entry(win, width=15 , borderwidth=5)
#pole.grid(row=1,column=2,columnspan=2)
#pole.pack()







frameTop = Frame(win, bg='#242424', padx=10, pady=10)
frameTop.place(relwidth=3, relheight=3)




text = Text(width=50, font = ('Segoe UI',13), height=50)
text['bg'] = '#E20D0D'
text['fg'] = '#FFFFFF'
text.pack()




def refresh():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    po = data.decode("utf-8")
    json = json.loads(po)

    n = 1

    for i in range (n):
        text.insert('1.0','\n')
        text.insert('1.0',  list(json[i].items())[14])
        text.insert('1.0','\n')
        text.insert('1.0', list(json[i].items())[10])
        text.insert('1.0','\n')
        text.insert('1.0', list(json[i].items())[11])
        text.insert('1.0','\n')
        text.insert('1.0', list(json[i].items())[7])
        text.insert('1.0','\n')
        text.insert('1.0', list(json[i].items())[6])
        text.insert('1.0','\n')
        text.insert('1.0', list(json[i].items())[2])
        text.insert('1.0','\n')
        text.insert('1.0', '-' * 34)
    

refreshButton = Button(win, text="REFRESH",height = 1, width = -10, font=('Segoe UI', 10), command=refresh)
refreshButton.place(relwidth=0.4, relx=0.674)












conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "36a2225d4cmsh0ead8e8f23c0bb7p1c8f91jsn3ecbd0c3befe",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
po = data.decode("utf-8")
json = json.loads(po)

n = 35

for i in range (n):
    text.insert('1.0','\n')
    text.insert('1.0',  list(json[i].items())[14])
    text.insert('1.0','\n')
    text.insert('1.0', list(json[i].items())[10])
    text.insert('1.0','\n')
    text.insert('1.0', list(json[i].items())[11])
    text.insert('1.0','\n')
    text.insert('1.0', list(json[i].items())[7])
    text.insert('1.0','\n')
    text.insert('1.0', list(json[i].items())[6])
    text.insert('1.0','\n')
    text.insert('1.0', list(json[i].items())[2])
    text.insert('1.0','\n')
    text.insert('1.0', '-' * 34)








text.configure(state="disabled")
win.mainloop()


