from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

now = datetime.now()

win1=Tk()
win1.title("Calculator")
win1.geometry('1000x800')
win1.config(background="#808080")
#----------------------------------------------------------------------------------------------------------------
#Functions
#----------------------------------------------------------------------------------------------------------------
def programmer():
    os.system("programmer.py")
def con_length():
    os.system("length.py")
def con_speed():
    os.system("speed.py")
def con_currency():
    os.system("currency.py")
def con_time():
    os.system("time.py")
def con_power():
    os.system("power.py")
def con_temperature():
    os.system("temperature.py")
def con_energy():
    os.system("energy.py")
def con_bmi():
    os.system("bmi.py")
def con_date():
    os.system("date.py")


#----------------------------------------------------------------------------------------------------------------
#MenuBar
#----------------------------------------------------------------------------------------------------------------

def hello():
    print ("hello!")


menubar = Menu(win1)

filemenu1 = Menu(menubar, tearoff=0)
filemenu1.add_command(label="Standard")
filemenu1.add_command(label="Programmer", command=programmer)
filemenu1.add_separator()
filemenu1.add_command(label="BMI Calculator", command=con_bmi)
filemenu1.add_command(label="Date Calculation", command=con_date)
menubar.add_cascade(label="Calculator", menu=filemenu1)

filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Currency", command=con_currency)
# filemenu2.add_command(label="Volume", command=hello)
filemenu2.add_command(label="Length", command=con_length)
# filemenu2.add_command(label="Weight and Mass", command=hello)
filemenu2.add_command(label="Temperature", command=con_temperature)
filemenu2.add_command(label="Energy", command=con_energy)
# filemenu2.add_command(label="Area", command=hello)
filemenu2.add_command(label="Speed", command=con_speed)
filemenu2.add_command(label="Time", command=con_time)
filemenu2.add_command(label="Power", command=con_power)
# filemenu2.add_command(label="Data", command=hello)
menubar.add_cascade(label="Converter", menu=filemenu2)

# menubar.add_cascade(label="About", menu=hello)

menubar.add_cascade(label="Quit", command=win1.quit)



win1.config(menu=menubar)

#----------------------------------------------------------------------------------------------------------------
def show_file():
    file="notepad.exe hist.txt"
    os.system(file)



#----------------------------------------------------------------------------------------------------------------

file1 = open("hist.txt","a")
file1.write("x-----x-----x-----x-----x-----x-----x \n")
time_1=now.strftime("%Y-%m-%d %H:%M:%S")
file1.write("History is recorded on : \n")
file1.writelines(time_1)
file1.write("\n \n")
lbl1=""

def write_file(i1,i2,i3):
    global lbl1
    VAL=""
    I1=str(i1)
    I2=str(i2)
    I3=str(i3)
    VAL+=I1
    if oper=='+':
        VAL+=" + "
    if oper=='-':
        VAL+=" - "
    if oper=='*':
        VAL+=" * "
    if oper=='/':
        VAL+=" / "
    if oper=='%':
        VAL+=" % "
    VAL+=I2
    VAL+=" = "
    VAL+=I3
    lbl1=""
    lbl1+=VAL
    data1.set(lbl1)

    file1.writelines(lbl1)
    file1.write("\n")
#----------------------------------------------------------------------------------------------------------------

value=""
num = 0
oper = ""

def bt1_clicked():
    global value
    value = value + "1"
    data.set(value)

def bt2_clicked():
    global value
    value = value + "2"
    data.set(value)

def bt3_clicked():
    global value
    value = value + "3"
    data.set(value)

def bt4_clicked():
    global value
    value = value + "4"
    data.set(value)

def bt5_clicked():
    global value
    value = value + "5"
    data.set(value)

def bt6_clicked():
    global value
    value = value + "6"
    data.set(value)

def bt7_clicked():
    global value
    value = value + "7"
    data.set(value)

def bt8_clicked():
    global value
    value = value + "8"
    data.set(value)
    
def bt9_clicked():
    global value
    value = value + "9"
    data.set(value)

def bt0_clicked():
    global value
    value = value + "0"
    data.set(value)

#---------------------------

def btA_clicked():
    global value
    global num
    global oper
    num=float(value)
    oper="+"
    value = value + "+"
    data.set(value)

def btS_clicked():
    global value
    global num
    global oper
    num=float(value)
    oper="-"
    value = value + "-"
    data.set(value)

def btM_clicked():
    global value
    global num
    global oper
    num=float(value)
    oper="*"
    value = value + "*"
    data.set(value)

def btD_clicked():
    global value
    global num
    global oper
    num=float(value)
    oper="/"
    value = value + "/"
    data.set(value)

def btMD_clicked():
    global value
    global num
    global oper
    num=float(value)
    oper="%"
    value = value + "%"
    data.set(value)

#----------------------------

def CE_clicked():
    global value
    global num
    global oper
    value=""
    num = 0
    oper=""
    data.set(value)

def answer():
    global value
    global num
    global oper
    value2=value
    if oper=="+":
        one = float((value2.split("+")[1]))
        two= num + one
        write_file(num,one,two)
        data.set(two)
        value=str(two)
    elif oper=="-":
        one = float((value2.split("-")[1]))
        two= num - one
        write_file(num,one,two)
        data.set(two)
        value=str(two)
    elif oper=="*":
        one = float((value2.split("*")[1]))
        two= num * one
        write_file(num,one,two)
        data.set(two)
        value=str(two)
    elif oper=="/":
        one = int((value2.split("/")[1]))
        
        if one==0:
            messagebox.showerror("Error","Divison by 0 is not possible ! ")
            num=0
            value= ""
            data.set(value)
        else:
            two= float(num / one)
            write_file(num,one,two)
            data.set(two)
            value=str(two)
    else:
        one = float((value2.split("%")[1]))
        two= float(num % one)
        write_file(num,one,two)
        data.set(two)
        value=str(two)
#-----------------------------------------------------------------------------------------------------------------

data=StringVar()
data1=StringVar()

l1=Label(win1,text="Label 1",textvariable=data1,background='#262626',fg="white",font=("Times New Roman","26","bold"))
l1.place(x=5,y=5,height=120,width=990)

l2=Label(win1,text="Label 2",textvariable=data,anchor="e",background='#262626',fg="white",font=("Times New Roman","45","bold"))
l2.place(x=5,y=130,height=166,width=990)
#-----------------------------------------------------------------------------------------------------------------

b1=Button(win1,text="C",command=CE_clicked,activebackground='#666666',borderwidth="6",background='#1a1a1a',fg="white",font=("Times New Roman","35","bold"))
b1.place(x=0,y=300,height=98,width=498)
b2=Button(win1,text="7",command=bt7_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b2.place(x=0,y=400,height=98,width=248)
b3=Button(win1,text="4",command=bt4_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b3.place(x=0,y=500,height=98,width=248)
b4=Button(win1,text="1",command=bt1_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b4.place(x=0,y=600,height=98,width=248)
b5=Button(win1,text="HISTORY",command=show_file,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","22","bold"))
b5.place(x=0,y=700,height=98,width=248)

#-----------------------------------------------------------------------------------------------------------------

# b6=Button(win1,text="DEL",activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
# b6.place(x=250,y=300,height=100,width=250)
b7=Button(win1,text="8",command=bt8_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b7.place(x=250,y=400,height=98,width=248)
b8=Button(win1,text="5",command=bt5_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b8.place(x=250,y=500,height=98,width=248)
b9=Button(win1,text="2",command=bt2_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b9.place(x=250,y=600,height=98,width=248)
b10=Button(win1,text="0",command=bt0_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b10.place(x=250,y=700,height=98,width=248)

#-----------------------------------------------------------------------------------------------------------------

b11=Button(win1,text="%",command=btMD_clicked,activebackground='#666666',background='#1a1a1a',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b11.place(x=500,y=300,height=98,width=248)
b12=Button(win1,text="9",command=bt9_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b12.place(x=500,y=400,height=98,width=248)
b13=Button(win1,text="6",command=bt6_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b13.place(x=500,y=500,height=98,width=248)
b14=Button(win1,text="3",command=bt3_clicked,activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b14.place(x=500,y=600,height=98,width=248)
b15=Button(win1,text=".",activebackground='#666666',background='#000000',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b15.place(x=500,y=700,height=98,width=248)


#-----------------------------------------------------------------------------------------------------------------

b16=Button(win1,text="/",command=btD_clicked,activebackground='#666666',background='#1a1a1a',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b16.place(x=750,y=300,height=98,width=248)
b17=Button(win1,text="*",command=btM_clicked,activebackground='#666666',background='#1a1a1a',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b17.place(x=750,y=400,height=98,width=248)
b18=Button(win1,text="-",command=btS_clicked,activebackground='#666666',background='#1a1a1a',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b18.place(x=750,y=500,height=98,width=248)
b19=Button(win1,text="+",command=btA_clicked,activebackground='#666666',background='#1a1a1a',fg="white",borderwidth="6",font=("Times New Roman","35","bold"))
b19.place(x=750,y=600,height=98,width=248)
b20=Button(win1,text="=",command=answer,activebackground='#666666',background='#00b300',fg="black",borderwidth="6",font=("Times New Roman","35","bold"))
b20.place(x=750,y=700,height=98,width=248)

#---------------------------------------------------------------------------------------------------------------
win1.mainloop()
file1.close()