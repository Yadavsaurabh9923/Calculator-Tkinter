from tkinter import * 
from currency_converter import CurrencyConverter

def calculate():
    amt=e11.get()
    curr_a=len_clicked1.get()
    curr_b=len_clicked2.get()
    c = CurrencyConverter()
    answer=c.convert(amt, curr_a, curr_b)
    answer=round(answer,4)
    len_data2.set(answer)




con_win1=Tk()
con_win1.title("Currency Converter")
con_win1.geometry('1000x600')
con_win1.config(background="#626262")


#--------------------------------------------------------------------------------------------------------------------------
len_data2=StringVar()

len_options = ["USD" ,"JPY" ,"BGN", "CZK", "DKK", "GBP" ,"HUF", "PLN", "RON" ,"SEK" ,"CHF", "ISK" ,"NOK", "HRK", "RUB" ,"TRY", "AUD", "BRL" ,"CAD" ,"CNY", "HKD" ,"IDR" ,"ILS" ,'INR', "KRW", "MXN", "MYR", "NZD" ,"PHP" ,"SGD", "THB", "ZAR" 
]

#-------------------------------------------------------------------------------------------------------------------------

len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win1,len_clicked1,*len_options)
len_drop1.place(x=50,y=330,height=50,width=350)
len_drop1.config(bg="green",font=("Times New Roman","22","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win1,len_clicked2,*len_options)
len_drop2.place(x=550,y=330,height=50,width=350)
len_drop2.config(bg="green",font=("Times New Roman","22","bold"))

#--------------------------------------------------------------------------------------------------------------------------

e11_value=IntVar()
e11=Entry(con_win1,textvariable=e11_value,text="BOX 2",background='#262626',borderwidth="5",fg="white",font=("Comic Sans MS","26","bold"))
e11.place(x=50,y=50,height=250,width=350)

con_win1_label2=Label(con_win1,textvariable=len_data2,text="BOX 2",background='#262626',borderwidth="5",fg="white",font=("Comic Sans MS","26","bold"))
con_win1_label2.place(x=550,y=50,height=250,width=350)

con_win1_label3=Label(con_win1,text="->",background='#C0CBCF',font=("Comic Sans MS","40","bold"))
con_win1_label3.place(x=435,y=100,height=100,width=80)


con_win1_b10=Button(con_win1,text="Convert",command=calculate,activebackground='#00b300',background='#000000',borderwidth="6",fg="white",font=("Comic Sans MS","35","bold"))
con_win1_b10.place(x=300,y=450,height=100,width=300)


con_win1.mainloop()