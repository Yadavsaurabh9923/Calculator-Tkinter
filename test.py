from datetime import date
f_date = date(2020, 2, 1)
l_date = date(2020, 7, 28)
delta = l_date - f_date
print(delta.days)


from tkinter import *
from tkinter import ttk
from datetime import date
from tkcalendar import Calendar


def date_convert():
    print(date1,date2)
    Label(date_win,textvariable=date1,background='#E7EFB2').place(x=50,y=150,height=100,width=150)
    delta = date2 - date1
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
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2020, month=2, day=5)
    cal.pack(fill="both", expand=True)
    Button(datetop, text="OK", command=print_sel).pack()
    Button(datetop, text="Exit", command=quit1).pack()

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
                   cursor="hand1", year=2020, month=2, day=5)
    cal.pack(fill="both", expand=True)
    Button(datetop, text="OK", command=print_sel).pack()
    Button(datetop, text="Exit", command=quit1).pack()

date_win = Tk()
date_win.geometry('500x500')
s = ttk.Style(date_win)
s.theme_use("clam")

Button(date_win, text='Last Date', command=dateexample1).place(x=50,y=20,height=100,width=150)

Button(date_win, text='Next Date', command=dateexample2).place(x=270,y=20,height=100,width=150)

# Label(date_win,textvariable=DATE1,background='#E7EFB2',).place(x=50,y=150,height=100,width=150)
# Label(date_win,textvariable=DATE2,background='#E7EFB2').place(x=270,y=150,height=100,width=150)

Button(date_win, text='CONVERT', command=date_convert).place(x=185,y=150,height=100,width=100)

date_win.mainloop()