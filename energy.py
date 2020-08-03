from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win6=Tk()
con_win6.title("Energy Converter")
con_win6.geometry('1000x600')
con_win6.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()


len_options = [
"Electron volts",
"Joules",
"Kilojoules",
"Thermal calories",
"Food calories",
"Foot-pounds",
"British thermal units"
]
len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win6,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","18","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win6,len_clicked2,*len_options)
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
    if len_clicked1.get()=="Electron volts":
        if len_clicked2.get()=="Electron volts":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*0.0000000000000000001602177
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*0.0000000000000000000001020177
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*0.00000000000000000003829294
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.00000000000000000000003829294
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*0.000000000000000000181705
            len_data2.set(temp)
        else:
            temp=newlen_value*0.0000000000000000000001518570
            len_data2.set(temp)
    elif len_clicked1.get()=="Joules":
        if len_clicked2.get()=="Electron volts":
            len_data2.set(len_value)
            temp=newlen_value*624150900000000000000000
        elif len_clicked2.get()=="Joules":
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*0.239006
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.000239006
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*0.737562
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000947817
            len_data2.set(temp)
    elif len_clicked1.get()=="Kilojoules":
        if len_clicked2.get()=="Electron volts":
            temp=newlen_value*6241509000000000000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*239.0057
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.239006
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*737.5621
            len_data2.set(temp)
        else:
            temp=newlen_value*0.947817
            len_data2.set(temp)
    elif len_clicked1.get()=="Thermal calories":
        if len_clicked2.get()=="Electron volts":
            temp=newlen_value*2611448000000000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*4.184
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*0.004184
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*3.08596
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00396567
            len_data2.set(temp)
    elif len_clicked1.get()=="Food calories":
        if len_clicked2.get()=="Electron volts":
            temp=newlen_value*26114480000000000000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*4184
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*4.184
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*3085.96
            len_data2.set(temp)
        else:
            temp=newlen_value*3.965666
            len_data2.set(temp)
    elif len_clicked1.get()=="Foot-pounds":
        if len_clicked2.get()=="Electron volts":
            temp=newlen_value*8462350000000000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*1.355818
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*0.00135582
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*0.324048
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.000324048
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            len_data2.set(len_value)
        else:
            temp=newlen_value*0.00128507
            len_data2.set(temp)
    else:
        if len_clicked2.get()=="Electron volts":
            temp=newlen_value*6585142000000000000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Joules":
            temp=newlen_value*1055.056
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilojoules":
            temp=newlen_value*1.055056
            len_data2.set(temp)
        elif len_clicked2.get()=="Thermal calories":
            temp=newlen_value*252.1644
            len_data2.set(temp)
        elif len_clicked2.get()=="Food calories":
            temp=newlen_value*0.252164
            len_data2.set(temp)
        elif len_clicked2.get()=="Foot-pounds":
            temp=newlen_value*778.1694
            len_data2.set(temp)
        else:
            len_data2.set(len_value)





#-------------------------------------------------------------------------------------------------------------------------------------

con_win6_label1=Label(con_win6,textvariable=len_data1,text="BOX 1",background='#666666',fg="white",font=("Times New Roman","26","bold"))
con_win6_label1.place(x=0,y=0,height=250,width=500)
con_win6_label3=Label(con_win6,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win6_label3.place(x=0,y=250,height=50,width=250)


con_win6_label2=Label(con_win6,textvariable=len_data2,text="BOX 2",background='#666666',fg="white",font=("Times New Roman","26","bold"))
con_win6_label2.place(x=0,y=300,height=250,width=500)
con_win6_label3=Label(con_win6,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win6_label3.place(x=0,y=550,height=50,width=250)


con_win6_b10=Button(con_win6,text="CE",command=len_CE_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b10.place(x=500,y=0,height=120,width=166.6)
con_win6_b1=Button(con_win6,text="7",command=len_bt7_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b1.place(x=500,y=120,height=120,width=166.6)
con_win6_b2=Button(con_win6,text="8",command=len_bt8_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win6_b3=Button(con_win6,text="9",command=len_bt9_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win6_b4=Button(con_win6,text="4",command=len_bt4_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b4.place(x=500,y=240,height=120,width=166.6)
con_win6_b5=Button(con_win6,text="5",command=len_bt5_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win6_b6=Button(con_win6,text="6",command=len_bt6_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win6_b7=Button(con_win6,text="1",command=len_bt1_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b7.place(x=500,y=360,height=120,width=166.6)
con_win6_b8=Button(con_win6,text="2",command=len_bt2_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win6_b9=Button(con_win6,text="3",command=len_bt3_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win6_b11=Button(con_win6,text="0",command=len_bt0_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b11.place(x=500,y=480,height=120,width=332)
con_win6_b12=Button(con_win6,text=".",command=len_btdot_clicked,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win6_b13=Button(con_win6,text="Convert",command=len_convert,activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
con_win6_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win6.mainloop()