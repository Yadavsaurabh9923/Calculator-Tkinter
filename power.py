from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win10=Tk()
con_win10.title("Time Converter")
con_win10.geometry('1000x600')
con_win10.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()


len_options = [
"Watts",
"Kilowatts",
"Horsepower(US)",
"Foot-Pound/Minute",
"BTU's/Minute"
]
len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win10,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","18","bold"))


len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win10,len_clicked2,*len_options)
len_drop2.place(x=250,y=550,height=50,width=250)
len_drop2.config(bg="green",font=("Times New Roman","18","bold"))


#----------------------------------------------------------------------------------------------------------------------


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

#-------------------------------------------------------------------------------------------------------------------------------------

def len_convert():
    newlen_value=float(len_value)
    if len_clicked1.get()=="Watts":
        if len_clicked2.get()=="Watts":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Kilowatts":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Horsepower(US)":
            temp=newlen_value*0.00134102
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-Pound/Minute":
            temp=newlen_value*44.25373
            len_data2.set(temp)
        else:
            temp=newlen_value*0.056869
            len_data2.set(temp)
    elif len_clicked1.get()=="Kilowatts":
        if len_clicked2.get()=="Watts":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilowatts":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Horsepower(US)":
            temp=newlen_value*1.341022
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-Pound/Minute":
            temp=newlen_value*44253.73
            len_data2.set(temp)
        else:
            temp=newlen_value*56.86902
            len_data2.set(temp)
    elif len_clicked1.get()=="Horsepower(US)":
        if len_clicked2.get()=="Watts":
            temp=newlen_value*745.6999
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilowatts":
            temp=newlen_value*0.7457
            len_data2.set(temp)
        elif len_clicked2.get()=="Horsepower(US)":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Foot-Pound/Minute":
            temp=newlen_value*33000
            len_data2.set(temp)
        else:
            temp=newlen_value*42.40722
            len_data2.set(temp)
    elif len_clicked1.get()=="Foot-Pund/Minute":
        if len_clicked2.get()=="Watts":
            temp=newlen_value*0.022597
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilowatts":
            temp=newlen_value*0.000022597
            len_data2.set(temp)
        elif len_clicked2.get()=="Horsepower(US)":
            temp=newlen_value*0.000030303
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-Pound/Minute":
            len_data2.set(len_value)
        else:
            temp=newlen_value*0.00128507
            len_data2.set(temp)
    else:
        if len_clicked2.get()=="Watts":
            temp=newlen_value*17.58427
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilowatts":
            temp=newlen_value*0.0175843
            len_data2.set(temp)
        elif len_clicked2.get()=="Horsepower(US)":
            temp=newlen_value*0.235809
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-Pound/Minute":
            temp=newlen_value*778.1694
            len_data2.set(temp)   
        else:
            len_data2.set(len_value)
        
    
            






#-------------------------------------------------------------------------------------------------------------------------------------

con_win10_label1=Label(con_win10,textvariable=len_data1,text="BOX 1",background='#666666',font=("Times New Roman","26","bold"))
con_win10_label1.place(x=0,y=0,height=250,width=500)
con_win10_label3=Label(con_win10,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win10_label3.place(x=0,y=250,height=50,width=250)


con_win10_label2=Label(con_win10,textvariable=len_data2,text="BOX 2",background='#666666',font=("Times New Roman","26","bold"))
con_win10_label2.place(x=0,y=300,height=250,width=500)
con_win10_label3=Label(con_win10,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win10_label3.place(x=0,y=550,height=50,width=250)


con_win10_b10=Button(con_win10,text="CE",command=len_CE_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b10.place(x=500,y=0,height=120,width=166.6)
con_win10_b1=Button(con_win10,text="7",command=len_bt7_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b1.place(x=500,y=120,height=120,width=166.6)
con_win10_b2=Button(con_win10,text="8",command=len_bt8_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win10_b3=Button(con_win10,text="9",command=len_bt9_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win10_b4=Button(con_win10,text="4",command=len_bt4_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b4.place(x=500,y=240,height=120,width=166.6)
con_win10_b5=Button(con_win10,text="5",command=len_bt5_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win10_b6=Button(con_win10,text="6",command=len_bt6_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win10_b7=Button(con_win10,text="1",command=len_bt1_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b7.place(x=500,y=360,height=120,width=166.6)
con_win10_b8=Button(con_win10,text="2",command=len_bt2_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win10_b9=Button(con_win10,text="3",command=len_bt3_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win10_b11=Button(con_win10,text="0",command=len_bt0_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b11.place(x=500,y=480,height=120,width=332)
con_win10_b12=Button(con_win10,text=".",command=len_btdot_clicked,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win10_b13=Button(con_win10,text="Convert",command=len_convert,borderwidth=5,activebackground='#949494',background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win10_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win10.mainloop()