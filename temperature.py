from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win5=Tk()
con_win5.title("Temperature Converter")
con_win5.geometry('1000x600')
con_win5.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()

len_options = ["Celsius","Fahrenheit","Kelvin"
]


len_clicked1=StringVar()
len_clicked1.set(len_options[0])
len_drop1=OptionMenu(con_win5,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","22","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[1])
len_drop2=OptionMenu(con_win5,len_clicked2,*len_options)
len_drop2.place(x=250,y=550,height=50,width=250)
len_drop2.config(bg="green",font=("Times New Roman","22","bold"))

#-------------------------------------------------------------------------------------------------------------------------------------

len_value=""
len_num = 0
len_oper = ""


def len_CE_clicked():
    global len_value
    global len_num
    global len_oper
    len_value=""
    len_num = 0
    len_oper=""
    len_data1.set(len_value)

def len_bt1_clicked():
    global len_value
    len_value = len_value + "1"
    len_data1.set(len_value)

def len_bt2_clicked():
    global len_value
    len_value = len_value + "2"
    len_data1.set(len_value)

def len_bt3_clicked():
    global len_value
    len_value = len_value + "3"
    len_data1.set(len_value)

def len_bt4_clicked():
    global len_value
    len_value = len_value + "4"
    len_data1.set(len_value)

def len_bt5_clicked():
    global len_value
    len_value = len_value + "5"
    len_data1.set(len_value)

def len_bt6_clicked():
    global len_value
    len_value = len_value + "6"
    len_data1.set(len_value)

def len_bt7_clicked():
    global len_value
    len_value = len_value + "7"
    len_data1.set(len_value)

def len_bt8_clicked():
    global len_value
    len_value = len_value + "8"
    len_data1.set(len_value)

def len_bt9_clicked():
    global len_value
    len_value = len_value + "9"
    len_data1.set(len_value)

def len_bt0_clicked():
    global len_value
    len_value = len_value + "0"
    len_data1.set(len_value)
    print(len_value)

def len_btdot_clicked():
    global len_value
    len_value = len_value + "."
    len_data1.set(len_value)

#-----------------------------------------------------------------------------------------------------------------------------------

def speed_convert():
    newlen_value=float(len_value)
    if len_clicked1.get()==len_options[0]:
        if len_clicked2.get()==len_options[0]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*33.8
            len_data2.set(temp)
        else:
            temp=newlen_value*274.15
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[1]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*(-17.22222)
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            len_data2.set(len_value)
        else:
            temp=newlen_value*255.9278
            len_data2.set(temp)
    else:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*(-272.15)
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*(-457.87)
            len_data2.set(temp)
        else:
            len_data2.set(len_value)

#-------------------------------------------------------------------------------------------------------------------------------------



con_win5_label1=Label(con_win5,textvariable=len_data1,text="BOX 1",background='#666666',fg="white",font=("Times New Roman","26","bold"))
con_win5_label1.place(x=0,y=0,height=250,width=500)
con_win5_label3=Label(con_win5,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win5_label3.place(x=0,y=250,height=50,width=250)


con_win5_label2=Label(con_win5,textvariable=len_data2,text="BOX 2",background='#666666',fg="white",font=("Times New Roman","26","bold"))
con_win5_label2.place(x=0,y=300,height=250,width=500)
con_win5_label3=Label(con_win5,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win5_label3.place(x=0,y=550,height=50,width=250)


con_win5_b10=Button(con_win5,text="CE",command=len_CE_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win5_b10.place(x=500,y=0,height=120,width=166.6)
con_win5_b1=Button(con_win5,text="7",command=len_bt7_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b1.place(x=500,y=120,height=120,width=166.6)
con_win5_b2=Button(con_win5,text="8",command=len_bt8_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win5_b3=Button(con_win5,text="9",command=len_bt9_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win5_b4=Button(con_win5,text="4",command=len_bt4_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b4.place(x=500,y=240,height=120,width=166.6)
con_win5_b5=Button(con_win5,text="5",command=len_bt5_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win5_b6=Button(con_win5,text="6",command=len_bt6_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win5_b7=Button(con_win5,text="1",command=len_bt1_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b7.place(x=500,y=360,height=120,width=166.6)
con_win5_b8=Button(con_win5,text="2",command=len_bt2_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win5_b9=Button(con_win5,text="3",command=len_bt3_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win5_b11=Button(con_win5,text="0",command=len_bt0_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b11.place(x=500,y=480,height=120,width=332)
con_win5_b12=Button(con_win5,text=".",command=len_btdot_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win5_b13=Button(con_win5,text="Convert",command=speed_convert,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win5_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win5.mainloop()