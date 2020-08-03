from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win9=Tk()
con_win9.title("Time Converter")
con_win9.geometry('1000x600')
con_win9.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()


len_options = [
"Microseconds",
"Miliseconds",
"Seconds",
"Minutes",
"Hours",
"Days",
"Weeks",
"Years"
]
len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win9,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","22","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win9,len_clicked2,*len_options)
len_drop2.place(x=250,y=550,height=50,width=250)
len_drop2.config(bg="green",font=("Times New Roman","22","bold"))


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
    if len_clicked1.get()=="Microseconds":
        if len_clicked2.get()=="Microseconds":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*0.000000016666667
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*0.000000000277778
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*0.000000000011574
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.000000000001653
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000000000000032
            len_data2.set(temp)
        newlen_value=int(len_value)
    elif len_clicked1.get()=="Miliseconds":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*0.0000166667
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*0.0000002777777778
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*0.000000011574074
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.000000001653439
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000000000031688
            len_data2.set(temp)
    elif len_clicked1.get()=="Seconds":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*1000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*0.0166667
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*0.000277778
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*0.0000115741
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.00000165344

            len_data2.set(temp)
        else:
            temp=newlen_value*0.000000031688088
            len_data2.set(temp)
    elif len_clicked1.get()=="Minutes":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*60000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*60000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*60
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*0.0166667
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*0.000694444
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.0000992063

            len_data2.set(temp)
        else:
            temp=newlen_value*0.00000190129
            len_data2.set(temp)
    elif len_clicked1.get()=="Hours":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*3600000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*3600000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*3600
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*60
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*0.0416667
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.00595238
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000114077
            len_data2.set(temp)
    elif len_clicked1.get()=="Days":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*86400000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*86400000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*86400
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*1440
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*24
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*0.142857
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00273785
            len_data2.set(temp)
    elif len_clicked1.get()=="Weeks":
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*604800000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*604800000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*604800
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*10080
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*168
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*7
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            len_data2.set(len_value)
        else:
            temp=newlen_value*0.019165
            len_data2.set(temp)
    else:
        if len_clicked2.get()=="Microseconds":
            temp=newlen_value*31557600000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Miliseconds":
            temp=newlen_value*31557600000
            len_data2.set(temp)
        elif len_clicked2.get()=="Seconds":
            temp=newlen_value*31557600
            len_data2.set(temp)
        elif len_clicked2.get()=="Minutes":
            temp=newlen_value*525960
            len_data2.set(temp)
        elif len_clicked2.get()=="Hours":
            temp=newlen_value*8766
            len_data2.set(temp)
        elif len_clicked2.get()=="Days":
            temp=newlen_value*365.25
            len_data2.set(temp)
        elif len_clicked2.get()=="Weeks":
            temp=newlen_value*52.17857
            len_data2.set(temp)
        else:
            len_data2.set(len_value)
            






#-------------------------------------------------------------------------------------------------------------------------------------

con_win9_label1=Label(con_win9,textvariable=len_data1,text="BOX 1",background='#666666',font=("Times New Roman","26","bold"))
con_win9_label1.place(x=0,y=0,height=250,width=500)
con_win9_label3=Label(con_win9,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win9_label3.place(x=0,y=250,height=50,width=250)


con_win9_label2=Label(con_win9,textvariable=len_data2,text="BOX 2",background='#666666',font=("Times New Roman","26","bold"))
con_win9_label2.place(x=0,y=300,height=250,width=500)
con_win9_label3=Label(con_win9,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win9_label3.place(x=0,y=550,height=50,width=250)


con_win9_b10=Button(con_win9,text="CE",command=len_CE_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b10.place(x=500,y=0,height=120,width=166.6)
con_win9_b1=Button(con_win9,text="7",command=len_bt7_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b1.place(x=500,y=120,height=120,width=166.6)
con_win9_b2=Button(con_win9,text="8",command=len_bt8_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win9_b3=Button(con_win9,text="9",command=len_bt9_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win9_b4=Button(con_win9,text="4",command=len_bt4_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b4.place(x=500,y=240,height=120,width=166.6)
con_win9_b5=Button(con_win9,text="5",command=len_bt5_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win9_b6=Button(con_win9,text="6",command=len_bt6_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win9_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win9_b7=Button(con_win9,text="1",command=len_bt1_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win9_b7.place(x=500,y=360,height=120,width=166.6)
con_win9_b8=Button(con_win9,text="2",command=len_bt2_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win9_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win9_b9=Button(con_win9,text="3",command=len_bt3_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win9_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win9_b11=Button(con_win9,text="0",command=len_bt0_clicked,activebackground='#949494',background='#000000',fg="white",borderwidth=5,font=("Times New Roman","35","bold"))
con_win9_b11.place(x=500,y=480,height=120,width=332)
con_win9_b12=Button(con_win9,text=".",command=len_btdot_clicked,activebackground='#949494',background='#000000',fg="white",borderwidth=5,font=("Times New Roman","35","bold"))
con_win9_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win9_b13=Button(con_win9,text="Convert",command=len_convert,activebackground='#949494',background='#000000',fg="white",borderwidth=5,font=("Times New Roman","35","bold"))
con_win9_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win9.mainloop()