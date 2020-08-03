from tkinter import *
from tkinter import ttk
from datetime import date
from tkcalendar import Calendar


def date_convert():
    print(date1,date2)
    delta = date2 - date1
    Label(date_win, text=date1,bg="#737373",relief="ridge",font=("Comic Sans MS","20","bold")).place(x=20,y=250,height=100,width=200)
    Label(date_win, text=date2,bg="#737373",relief="ridge",font=("Comic Sans MS","20","bold")).place(x=270,y=250,height=100,width=200)
    Label(date_win, text="Difference :",relief="ridge",bg="#737373",font=("Comic Sans MS","20","bold")).place(x=20,y=380,height=100,width=200)
    Label(date_win, text=delta.days,relief="ridge",bg="#737373",font=("Comic Sans MS","20","bold")).place(x=270,y=380,height=100,width=200)
    print(delta.days)


def dateexample1():
    def print_sel():
        global date1
        date1=cal.selection_get()
        datetop.destroy()
    def quit1():
        datetop.destroy()

    datetop = Toplevel(date_win)

    cal = Calendar(datetop,
                   font="Ariel 14", selectmode='day',
                   cursor="hand1", year=2020, month=8, day=4)
    cal.pack(fill="both", expand=True)
    Button(datetop, text="OK", bg="black",fg="white",command=print_sel).pack()
    Button(datetop, text="Exit", bg="black",fg="white",command=quit1).pack()

def dateexample2():
    def print_sel():
        global date2
        date2=cal.selection_get()
        datetop.destroy()
    def quit1():
        datetop.destroy()

    datetop = Toplevel(date_win)

    cal = Calendar(datetop,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2020, month=8, day=5)
    cal.pack(fill="both", expand=True)
    Button(datetop, text="OK",bg="black",fg="white", command=print_sel).pack()
    Button(datetop, text="Exit", bg="black",fg="white",command=quit1).pack()


date_win = Tk()
date_win.title("Date Calculation")
date_win.geometry('500x500')
date_win.config(background="#a6a6a6")
s = ttk.Style(date_win)
s.theme_use('clam')

a="Saurabh"

Button(date_win, text='Last Date',bg="#666666", borderwidth=5,command=dateexample1,font=("Times New Roman","22","bold")).place(x=50,y=20,height=100,width=150)

Button(date_win, text='Next Date',bg="#666666",  borderwidth=5,command=dateexample2,font=("Times New Roman","22","bold")).place(x=270,y=20,height=100,width=150)

# Label(date_win,textvariable=a,background='#E7EFB2',).place(x=50,y=150,height=100,width=150)
# Label(date_win,textvariable=DATE2,background='#E7EFB2').place(x=270,y=150,height=100,width=150)

Button(date_win, text="CONVERT", bg="#2eb82e",command=date_convert,font=("Times New Roman","14","bold")).place(x=185,y=150,height=70,width=100)

date_win.mainloop()