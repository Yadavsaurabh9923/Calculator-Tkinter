from tkinter import *
from tkinter import messagebox
import math

pro_win1=Tk()
pro_win1.title("Programmmer's Calculator")
pro_win1.geometry('1200x800')
pro_win1.config(background="#C0CBCF")

#---------------------------------------------------------------------------------------------------------------------------
data=StringVar()
entrybox=StringVar()




bin_data=StringVar()
oct_data=StringVar()
dec_data=StringVar()
hex_data=StringVar()



#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#mainfunction

def program_main1():
    pro_num=int(value)
    if(number_verify==0):
        messagebox.showerror("Error !","Make sure you have clicked the entered number's type ! ")
    elif(number_verify==1):
        bin_data.set(value)
        pro_num=int(value)
        oct_data.set(oct(pro_num))
        #-------------------
        def BinaryToDecimal(provalue): 
            global prodecimal
            prodecimal = 0 
            for digit in provalue: 
                prodecimal = prodecimal*2 + int(digit) 
            # print("The decimal value is:", prodecimal)
        BinaryToDecimal(value)
        dec_data.set(prodecimal)

        binary_string = value
        decimal_representation = int(binary_string, 2)
        hexadecimal_string = hex(decimal_representation)
        hex_data.set(hexadecimal_string)
    elif(number_verify==2):
        dec_data.set(value)
        # print(bin(pro_num))
        bin_data.set(bin(pro_num))
        oct_data.set(oct(pro_num))
        hex_data.set(hex(pro_num))
    elif(number_verify==3):
        oct_data.set(pro_num)
        def OctToBin(octnum): 
            binary = "" 
            while octnum != 0: 
                d = int(octnum % 10) 
                if d == 0: 
                    binary = "".join(["000", binary])
                elif d == 1: 
                    binary = "".join(["001", binary]) 
                elif d == 2:  
                    binary = "".join(["010", binary]) 
                elif d == 3:
                    binary = "".join(["011", binary]) 
                elif d == 4:
                    binary = "".join(["100", binary]) 
                elif d == 5: 
                    binary = "".join(["101", binary]) 
                elif d == 6: 
                    binary = "".join(["110",binary]) 
                elif d == 7:
                    binary = "".join(["111", binary]) 
                else:  
                    binary = "Invalid Octal Digit"
                    break
                octnum = int(octnum / 10)
            return binary
        octnum = pro_num
        final_bin = "" + OctToBin(octnum)
        bin_data.set(final_bin)
        #-----------------------------------------------------------
        def octalToDecimal(n): 
            num = n; 
            dec_value = 0; 
            base = 1; 
            temp = num; 
            while (temp):
                last_digit = temp % 10; 
                temp = int(temp / 10);
                dec_value += last_digit * base; 
                base = base * 8; 

            return dec_value;
        return_oct_dec=octalToDecimal(pro_num)
        dec_data.set(return_oct_dec)
        oct_to_dec=int(value,8)
        hex_data.set(hex(oct_to_dec))
        #-----------------------------------------------------------
    else:
        hexa_bin=int(value,16)
        bin_data.set(bin(hexa_bin))

        hexa_oct=int(value,16)
        oct_data.set(oct(hexa_oct))

        hexa_dec=int(value,16)
        dec_data.set(hexa_dec)
        hex_data.set(value)

def program_main2():
    if(number_verify==4):
        entry_hex=entrybox.get()
        hexa_bin=int(entry_hex,16)
        bin_data.set(bin(hexa_bin))

        hexa_oct=int(entry_hex,16)
        oct_data.set(oct(hexa_oct))

        hexa_dec=int(entry_hex,16)
        dec_data.set(hexa_dec)
        hex_data.set(entry_hex)
    else:
        messagebox.showerror("Error !"," Only for Hexadecimal numbers")




        
#----------------------------------------------------------------------------------------------------------------

number_verify=0

def togglecolor1():
    global number_verify
    if(b21['background']=='grey'):
        b21['background']='red'
        b22['background']='grey'
        b23['background']='grey'
        b24['background']='grey'
        number_verify=1
    elif(b21['background']=='red'):
        b21['background']='grey'
        number_verify=0
def togglecolor2():
    if(b22['background']=='grey'):
        global number_verify
        b21['background']='grey'
        b22['background']='red'
        b23['background']='grey'
        b24['background']='grey'
        number_verify=2
    elif(b22['background']=='red'):
        b22['background']='grey'
        number_verify=0
def togglecolor3():
    if(b23['background']=='grey'):
        global number_verify
        b21['background']='grey'
        b22['background']='grey'
        b23['background']='red'
        b24['background']='grey'
        number_verify=3
    elif(b23['background']=='red'):
        b23['background']='grey'
        number_verify=0
def togglecolor4():
    entry_box.delete(0, END)
    if(b24['background']=='grey'):
        global number_verify
        b21['background']='grey'
        b22['background']='grey'
        b23['background']='grey'
        b24['background']='red'
        number_verify=4
    elif(b24['background']=='red'):
        b24['background']='grey'
        number_verify=0
    
    
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
    num=int(value)
    oper="+"
    value = value + "+"
    data.set(value)

def btS_clicked():
    global value
    global num
    global oper
    num=int(value)
    oper="-"
    value = value + "-"
    data.set(value)

def btM_clicked():
    global value
    global num
    global oper
    num=int(value)
    oper="*"
    value = value + "*"
    data.set(value)

def btD_clicked():
    global value
    global num
    global oper
    num=int(value)
    oper="/"
    value = value + "/"
    data.set(value)

def btMD_clicked():
    global value
    global num
    global oper
    num=int(value)
    oper="%"
    value = value + "%"
    data.set(value)

def len_btdot_clicked():
    global value
    value = value + "."
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
        one = int((value2.split("+")[1]))
        two= num + one
        write_file(num,one,two)
        data.set(two)
        value=str(two)
    elif oper=="-":
        one = int((value2.split("-")[1]))
        two= num - one
        write_file(num,one,two)
        data.set(two)
        value=str(two)
    elif oper=="*":
        one = int((value2.split("*")[1]))
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
            two= int(num / one)
            write_file(num,one,two)
            data.set(two)
            value=str(two)
    else:
        one = int((value2.split("%")[1]))
        two= int(num % one)
        write_file(num,one,two)
        data.set(two)
        value=str(two)



#---------------------------------------------------------------------------------------------------------------------------

pro1=Label(pro_win1,text="BINARY :",background='#E7EFD2',font=("Times New Roman","22","bold"),relief="ridge",anchor=W)
pro1.place(x=0,y=0,height=200,width=300)
pro_1=Label(pro_win1,textvariable=bin_data,background='#A7EFD2',font=("Times New Roman","18","bold"),relief="ridge")
pro_1.place(x=300,y=0,height=200,width=300)
pro2=Label(pro_win1,text="OCTAL :",background='#E7EFF2',font=("Times New Roman","22","bold"),anchor=W,relief="ridge")
pro2.place(x=0,y=200,height=200,width=300)
pro_2=Label(pro_win1,textvariable=oct_data,background='#A7EFF2',font=("Times New Roman","18","bold"),relief="ridge")
pro_2.place(x=300,y=200,height=200,width=300)
pro3=Label(pro_win1,text="DECIMAL :",background='#E7EFD2',font=("Times New Roman","22","bold"),anchor=W,relief="ridge")
pro3.place(x=0,y=400,height=200,width=300)
pro_3=Label(pro_win1,textvariable=dec_data,background='#A7EFD2',font=("Times New Roman","18","bold"),relief="ridge")
pro_3.place(x=300,y=400,height=200,width=300)
pro4=Label(pro_win1,text="HEXADECIMAL :",background='#E7EFF2',font=("Times New Roman","22","bold"),anchor=W,relief="ridge")
pro4.place(x=0,y=600,height=200,width=300)
pro_4=Label(pro_win1,textvariable=hex_data,background='#A7EFF2',font=("Times New Roman","18","bold"),relief="ridge")
pro_4.place(x=300,y=600,height=200,width=300)

#---------------------------------------------------------------------------------------------------------------------

b1=Button(pro_win1,text="C",command=CE_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b1.place(x=600,y=250,height=110,width=300)
b2=Button(pro_win1,text="7",command=bt7_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b2.place(x=600,y=360,height=110,width=150)
b3=Button(pro_win1,text="4",command=bt4_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b3.place(x=600,y=470,height=110,width=150)
b4=Button(pro_win1,text="1",command=bt1_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b4.place(x=600,y=580,height=110,width=150)
cb5=Button(pro_win1,text="CONVERT",command=program_main1,activebackground='dark green',borderwidth=5,background='green',fg="white",font=("Times New Roman","20","bold"))
cb5.place(x=600,y=690,height=110,width=300)

cb6=Button(pro_win1,text="CONVERT",command=program_main2,activebackground='dark green',borderwidth=5,background='green',fg="white",font=("Times New Roman","20","bold"))
cb6.place(x=1000,y=200,height=50,width=200)


#-----------------------------------------------------------------------------------------------------------------

# b6=Button(pro_win1,text="DEL",activebackground='#949494',background='#000000',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
# b6.place(x=750,y=250,height=110,width=150)
b7=Button(pro_win1,text="8",command=bt8_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b7.place(x=750,y=360,height=110,width=150)
b8=Button(pro_win1,text="5",command=bt5_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b8.place(x=750,y=470,height=110,width=150)
b9=Button(pro_win1,text="2",command=bt2_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b9.place(x=750,y=580,height=110,width=150)
b10=Button(pro_win1,text="0",command=bt0_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b10.place(x=900,y=690,height=110,width=150)

#-----------------------------------------------------------------------------------------------------------------

b11=Button(pro_win1,text="%",command=btMD_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b11.place(x=900,y=250,height=110,width=150)
b12=Button(pro_win1,text="9",command=bt9_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b12.place(x=900,y=360,height=110,width=150)
b13=Button(pro_win1,text="6",command=bt6_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b13.place(x=900,y=470,height=110,width=150)
b14=Button(pro_win1,text="3",command=bt3_clicked,activebackground='#007BA7',borderwidth=5,background='#646F72',fg="white",font=("Times New Roman","35","bold"))
b14.place(x=900,y=580,height=110,width=150)
# b15=Button(pro_win1,text=".",command=len_btdot_clicked,activebackground='#949494',background='#646F72',borderwidth=5,fg="white",font=("Times New Roman","35","bold"))
# b15.place(x=900,y=690,height=110,width=150)


b16=Button(pro_win1,text="/",command=btD_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b16.place(x=1050,y=250,height=110,width=150)
b17=Button(pro_win1,text="*",command=btM_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b17.place(x=1050,y=360,height=110,width=150)
b18=Button(pro_win1,text="-",command=btS_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b18.place(x=1050,y=470,height=110,width=150)
b19=Button(pro_win1,text="+",command=btA_clicked,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
b19.place(x=1050,y=580,height=220,width=150)
# b20=Button(pro_win1,text="=",command=answer,activebackground='#949494',borderwidth=5,background='#000000',fg="white",font=("Times New Roman","35","bold"))
# b20.place(x=1050,y=690,height=110,width=150)

#------____________---------------______________------------_____________-------------_____________

pro5=Label(pro_win1,text="NUMBER :",background='#E7EFB2',font=("Times New Roman","26","bold"),anchor=W,relief="ridge")
pro5.place(x=600,y=0,height=200,width=200)
pro6=Label(pro_win1,textvariable=data,background='#E7EFB2',font=("Times New Roman","22","bold"),anchor=W,relief="ridge")
pro6.place(x=800,y=0,height=200,width=200)

# pro7=Label(pro_win1,textvariable=text_data,background='#E7EFB2',font=("Times New Roman","22","bold"),anchor=W)
# pro7.place(x=800,y=0,height=200,width=200)

b21=Button(pro_win1,text="BIN",command=togglecolor1,borderwidth=5,background='grey',font=("Times New Roman","32","bold"))
b21.place(x=1000,y=0,height=100,width=100)
b22=Button(pro_win1,text="DEC",command=togglecolor2,borderwidth=5,background='grey',font=("Times New Roman","32","bold"))
b22.place(x=1100,y=0,height=100,width=100)
b23=Button(pro_win1,text="OCT",command=togglecolor3,borderwidth=5,background='grey',font=("Times New Roman","32","bold"))
b23.place(x=1000,y=100,height=100,width=100)
b24=Button(pro_win1,text="HEX",command=togglecolor4,borderwidth=5,background='grey',font=("Times New Roman","32","bold"))
b24.place(x=1100,y=100,height=100,width=100)

entry_box=Entry(pro_win1,fg='blue',textvariable=entrybox,borderwidth=5,background='white',font=("Times New Roman","18","bold"))
entry_box.place(x=600,y=200,height=50,width=400)
entry_box.insert(0,'Enter HexaDecimal numbers')


pro_win1.mainloop()
