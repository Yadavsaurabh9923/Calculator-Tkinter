from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win3=Tk()
con_win3.title("Length Converter")
con_win3.geometry('1000x600')
con_win3.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()


len_options = [
"Nanometers",
"Microns",
"Milimeters",
"Centimeters",
"Meters",
"Kilometers",
"Inches",
"Feet",
"Yards",
"Miles",
"Nautical Miles"
]
len_clicked1=StringVar()
len_clicked1.set(len_options[3])
len_drop1=OptionMenu(con_win3,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)
len_drop1.config(bg="green",font=("Times New Roman","22","bold"))



len_clicked2=StringVar()
len_clicked2.set(len_options[3])
len_drop2=OptionMenu(con_win3,len_clicked2,*len_options)
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
    if len_clicked1.get()=="Nanometers":
        if len_clicked2.get()=="Nanometers":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*0.0000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.000000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.000000000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*0.000000039370079
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*0.00000000328084
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.000000001093613
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000000000000621
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00000000000054
            len_data2.set(temp)
    elif len_clicked1.get()=="Microns":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*0.0001
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.000000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*0.0000393701
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*0.00000328084
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.00000109361
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000000000621
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00000000000054
            len_data2.set(temp)
    elif len_clicked1.get()=="Milimeters":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*0.0000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.000000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.000000000001
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*0.000000039370079
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*0.00000000328084
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.000000001093613
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000000000000621
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00000000000054
            len_data2.set(temp)
    elif len_clicked1.get()=="Centimeters":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*10000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*10000
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*10
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.01
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.00001
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*0.393701
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*0.0328084
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.0109361
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.00000621371
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00000539957
            len_data2.set(temp)
    elif len_clicked1.get()=="Meters":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*1000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*1000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*100
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*39.37008
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*3.28084
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*1.093613
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000621371
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000539957
            len_data2.set(temp)
    elif len_clicked1.get()=="Kilometers":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*1000000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*100000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*1000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*100000
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*29370.08
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*3280.84
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*1093.613
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.621371
            len_data2.set(temp)
        else:
            temp=newlen_value*0.539957
            len_data2.set(temp)
    elif len_clicked1.get()=="Inches":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*25400000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*25400
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*25.4
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*2.54
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.0254
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.40254
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*0.0833333
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.0277778
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.0000157828
            len_data2.set(temp)
        else:
            temp=newlen_value*0.0000137149
            len_data2.set(temp)
    elif len_clicked1.get()=="Feet":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*304800000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*304800
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*304.8
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*30.48
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.3048
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.0003048
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*12
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*0.333333
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000189394
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000164579
            len_data2.set(temp)
    elif len_clicked1.get()=="Yards":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*914400000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*914400
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*914.04
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*91.44
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*0.9144
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*0.0009144
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*36
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*3
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            len_data2.set(len_value)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*0.000568182
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000493737
            len_data2.set(temp)
    elif len_clicked1.get()=="Miles":
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*1609344000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*1609344000
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*1609344
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*160934.4
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*1609.344
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*1.609344
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*63.360
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*5280
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*1760
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            len_data2.set(len_value)
        else:
            temp=newlen_value*0.868976
            len_data2.set(temp)
    else:
        if len_clicked2.get()=="Nanometers":
            temp=newlen_value*1852000000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Microns":
            temp=newlen_value*1852000000
            len_data2.set(temp)
        elif len_clicked2.get()=="Milimeters":
            temp=newlen_value*1852000
            len_data2.set(temp)
        elif len_clicked2.get()=="Centimeters":
            temp=newlen_value*185200
            len_data2.set(temp)
        elif len_clicked2.get()=="Meters":
            temp=newlen_value*1852
            len_data2.set(temp)
        elif len_clicked2.get()=="Kilometers":
            temp=newlen_value*1.852
            len_data2.set(temp)
        elif len_clicked2.get()=="Inches":
            temp=newlen_value*72913.39
            len_data2.set(temp)
        elif len_clicked2.get()=="Feet":
            temp=newlen_value*676.115
            len_data2.set(temp)
        elif len_clicked2.get()=="Yards":
            temp=newlen_value*225.372
            len_data2.set(temp)
        elif len_clicked2.get()=="Miles":
            temp=newlen_value*1.150779
            len_data2.set(temp)
        else:
            len_data2.set(len_value)






#-------------------------------------------------------------------------------------------------------------------------------------

con_win3_label1=Label(con_win3,textvariable=len_data1,text="BOX 1",background='#666666',font=("Times New Roman","26","bold"))
con_win3_label1.place(x=0,y=0,height=250,width=500)
con_win3_label3=Label(con_win3,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win3_label3.place(x=0,y=250,height=50,width=250)


con_win3_label2=Label(con_win3,textvariable=len_data2,text="BOX 2",background='#666666',font=("Times New Roman","26","bold"))
con_win3_label2.place(x=0,y=300,height=250,width=500)
con_win3_label3=Label(con_win3,text="Unit :",background='#333333',font=("Times New Roman","26","bold"))
con_win3_label3.place(x=0,y=550,height=50,width=250)


con_win3_b10=Button(con_win3,text="CE",command=len_CE_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b10.place(x=500,y=0,height=120,width=166.6)
con_win3_b1=Button(con_win3,text="7",command=len_bt7_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b1.place(x=500,y=120,height=120,width=166.6)
con_win3_b2=Button(con_win3,text="8",command=len_bt8_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win3_b3=Button(con_win3,text="9",command=len_bt9_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win3_b4=Button(con_win3,text="4",command=len_bt4_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b4.place(x=500,y=240,height=120,width=166.6)
con_win3_b5=Button(con_win3,text="5",command=len_bt5_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win3_b6=Button(con_win3,text="6",command=len_bt6_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win3_b7=Button(con_win3,text="1",command=len_bt1_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b7.place(x=500,y=360,height=120,width=166.6)
con_win3_b8=Button(con_win3,text="2",command=len_bt2_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win3_b9=Button(con_win3,text="3",command=len_bt3_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win3_b11=Button(con_win3,text="0",command=len_bt0_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b11.place(x=500,y=480,height=120,width=332)
con_win3_b12=Button(con_win3,text=".",command=len_btdot_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win3_b13=Button(con_win3,text="Convert",command=len_convert,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
con_win3_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win3.mainloop()