from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win8=Tk()
con_win8.title("Speed Converter")
con_win8.geometry('1000x600')
con_win8.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()

len_options = [
"Centimeters per second",
"Meters per second",
"Kilometers per hour",
"Feet per second",
"Miles per hour",
"Knots",
"Mach"
]


len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win8,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","16","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win8,len_clicked2,*len_options)
len_drop2.place(x=250,y=550,height=50,width=250)
len_drop2.config(bg="green",font=("Times New Roman","16","bold"))

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
            temp=newlen_value*0.01
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.036
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.0328084
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*0.0223714
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.0194401
            len_data2.set(temp)
        else:
            temp=newlen_value*0.0000293858
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[1]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*100
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*3.6
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*3.280884
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*2.237136
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*1.944012
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00293858
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[2]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*27.77778
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*0.277778
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.911344
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*0.621427
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.540003
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000816273
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[3]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*3048
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*0.3048
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*1.9728
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*0.681879
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.592535
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00089568
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[4]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*44.7
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*0.447
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*1.6092
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*1.466535
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[4]:
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.868984
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00131355
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[5]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*51.44
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*0.5144
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*1.85184
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*1.687664
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*1.150783
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00151161
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[6]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*34030
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*340.3
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*125.8
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*116.47
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*761.2975
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*661.5457
            len_data2.set(temp)
        else:
            len_data2.set(temp)

#-------------------------------------------------------------------------------------------------------------------------------------



con_win8_label1=Label(con_win8,textvariable=len_data1,text="BOX 1",background='#666666',font=("Times New Roman","26","bold"))
con_win8_label1.place(x=0,y=0,height=250,width=500)
con_win8_label3=Label(con_win8,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win8_label3.place(x=0,y=250,height=50,width=250)


con_win8_label2=Label(con_win8,textvariable=len_data2,text="BOX 2",background='#666666',font=("Times New Roman","26","bold"))
con_win8_label2.place(x=0,y=300,height=250,width=500)
con_win8_label3=Label(con_win8,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win8_label3.place(x=0,y=550,height=50,width=250)


con_win8_b10=Button(con_win8,text="CE",command=len_CE_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b10.place(x=500,y=0,height=120,width=166.6)
con_win8_b1=Button(con_win8,text="7",command=len_bt7_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b1.place(x=500,y=120,height=120,width=166.6)
con_win8_b2=Button(con_win8,text="8",command=len_bt8_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win8_b3=Button(con_win8,text="9",command=len_bt9_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win8_b4=Button(con_win8,text="4",command=len_bt4_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b4.place(x=500,y=240,height=120,width=166.6)
con_win8_b5=Button(con_win8,text="5",command=len_bt5_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win8_b6=Button(con_win8,text="6",command=len_bt6_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win8_b7=Button(con_win8,text="1",command=len_bt1_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b7.place(x=500,y=360,height=120,width=166.6)
con_win8_b8=Button(con_win8,text="2",command=len_bt2_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win8_b9=Button(con_win8,text="3",command=len_bt3_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win8_b11=Button(con_win8,text="0",command=len_bt0_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b11.place(x=500,y=480,height=120,width=332)
con_win8_b12=Button(con_win8,text=".",command=len_btdot_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win8_b13=Button(con_win8,text="Convert",command=speed_convert,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win8_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win8.mainloop()