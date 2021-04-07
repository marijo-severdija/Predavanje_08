from tkinter import *
from tkinter import Tk
from random import randint

root = Tk()
root.title('Guess')
root.geometry('550x300')

attempt = StringVar()
guess = IntVar()
poruka = StringVar()

attempt_no = 0
attempt.set(attempt_no)

def guessing():
    global attempt_no
    if attempt_no <= 5:
        if int(guess.get()) == a:
            poruka.set("Bravo, pogodili ste zamišljen broj!")
        elif int(guess.get()) > a:
            poruka.set("Zamišljen broj je manji od Vašeg...")
        elif int(guess.get()) < a:
            poruka.set("Zamišljen broj je veći od Vašeg...")
    else:
        poruka.set("Iskoristili ste max broj pokušaja...")


def submit():
    global attempt_no
    attempt_no += 1
    if attempt_no <= 5:
        attempt.set(attempt_no)
        guessing()
        entry1.focus_set()
        entry1.select_range(0, END)

def submit_event(e):
    submit()


a = randint(1, 30)

# -----GUI----------------------
frame = Frame(root)
frame.pack()
naslov = Label(frame, text="Igra pogađanja broja od 1-30", font="Helvetica 16 bold")
naslov.grid(row=0, column=0, columnspan=3, pady=20)
label0 = Label(frame, text="Probaj pogoditi zamišljeni broj iz 5 pokušaja")
label0.grid(row=1, column=0, columnspan=3, pady=(0, 20))
label1 = Label(frame, text="Pogodi zamišljeni broj: ")
label1.grid(row=2, column=0, padx=10)
entry1 = Entry(frame, width=20, textvariable=guess)
entry1.grid(row=2, column=1)
entry1.focus_set()
entry1.select_range(0, END)
entry1.bind('<Return>', submit_event)
btn1 = Button(frame, text="Submit", width=10, command=submit)
btn1.grid(row=2, column=2, padx=(10, 0))
label2 = Label(frame, text="Broj dosadašnjih pokušaja: ")
label2.grid(row=3, column=0, pady=10)
label3 = Label(frame, textvariable=attempt)
label3.grid(row=3, column=1)
label4 = Label(frame, textvariable=poruka, font="Helvetica 16 bold")
label4.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
