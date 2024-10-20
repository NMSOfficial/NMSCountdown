import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("NMSCountdown")

saat = StringVar()
dakika = StringVar()
saniye = StringVar()

saat.set("00")
dakika.set("00")
saniye.set("00")

saatGirdisi = Entry(root, width=3, font=("SF Pro Display", 18, ""), textvariable=saat)
saatGirdisi.place(x=80, y=20)

dakikaGirdisi = Entry(root, width=3, font=("SF Pro Display", 18, ""), textvariable=dakika)
dakikaGirdisi.place(x=130, y=20)

saniyeGirdisi = Entry(root, width=3, font=("SF Pro Display", 18, ""), textvariable=saniye)
saniyeGirdisi.place(x=180, y=20)

def gonder():
    try:
        temp = int(saat.get()) * 3600 + int(dakika.get()) * 60 + int(saniye.get())
    except:
        print("Lütfen doğru bir değer girin")
    while temp > -1:
        dak = divmod(temp, 60)
        dk = dak[0]
        sn = dak[1]

        saatSayisi = 0
        if dk > 60:
            saatSayisi, dk = divmod(dk, 60)

        saat.set("{0:2d}".format(saatSayisi))
        dakika.set("{0:2d}".format(dk))
        saniye.set("{0:2d}".format(sn))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Zaman Geri Sayım", "Süreniz doldu")

        temp -= 1

btn = Button(root, text='Zaman Geri Sayımı Ayarla', bd='5', command=gonder)
btn.place(x=70, y=120)

root.mainloop()
