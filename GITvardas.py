from tkinter import *

langas = Tk()
paskutinis_vardas = ""


def spausdinti():
    global paskutinis_vardas
    ivesta = laukas1.get()
    if ivesta:
        paskutinis_vardas = ivesta
        rezultatas["text"] = "Labas " + ivesta
        status["text"] = "Sukurta"
    else:
        rezultatas["text"] = "Prašome įvesti vardą."


def enter(event):
    spausdinti()


def valymas():
    rezultatas["text"] = ""
    laukas1.delete(0, END)
    status["text"] = "Išvalyta"  # Rodoma, kad tekstas išvalytas


def atkurti():
    global paskutinis_vardas
    if paskutinis_vardas:
        rezultatas["text"] = "Labas " + paskutinis_vardas
        laukas1.delete(0, END)
        laukas1.insert(0, paskutinis_vardas)
        status["text"] = "Atkurta"


def iseiti():
        langas.destroy()


def uzdaryti(event):
    iseiti()


langas.bind("<Return>", enter)
langas.bind("<Escape>", uzdaryti)

uzrasas1 = Label(langas, text="Įveskite vardą")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
rezultatas = Label(langas, text="")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=valymas)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=2, columnspan=3, sticky=W + E)


langas.title("NORIMAS_PAVADINIMAS")
langas.iconbitmap(r'papai.ico')


langas.mainloop()

