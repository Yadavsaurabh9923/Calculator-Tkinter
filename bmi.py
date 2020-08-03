from tkinter import *
from tkinter import messagebox
import math

bmi_win1=Tk()
bmi_win1.title("Body Mass Index Calculator")
bmi_win1.geometry('1000x400')
bmi_win1.config(background="#626262")

#------------------------------------------------------------------------------------------------------------------------------

len_data1=StringVar()
len_data2=StringVar()
bmi_ANS=StringVar()


len_options1 = [
"Kilogram",
"Pounds"
]

len_clicked1=StringVar()
len_clicked1.set(len_options1[1])
len_drop1=OptionMenu(bmi_win1,len_clicked1,*len_options1)
len_drop1.place(x=370,y=55,height=50,width=150)
len_drop1.config(bg="green",font=("Times New Roman","16","bold"))


len_options2 = [
"Centimeters",
"Meters",
"Feets",
"Inches"
]

len_clicked2=StringVar()
len_clicked2.set(len_options2[1])
len_drop2=OptionMenu(bmi_win1,len_clicked2,*len_options2)
len_drop2.place(x=370,y=170,height=50,width=150)
len_drop2.config(bg="green",font=("Times New Roman","16","bold"))




#---------------------------------------------------------------------------------------------------------------------------

def BMI(wei,hei):
    bmi_ANS=StringVar()
    bmi_con=StringVar()
    bmi_ans = wei/(hei**2)
    bmi_fans=round(bmi_ans,3)
    bmi_ANS.set(bmi_fans)
    bmi_win2=Toplevel(bmi_win1)
    bmi_win2.title("Results")
    bmi_win2.geometry('500x344')
    bmi_win2.config(background="#99ccff")

    if(bmi_fans)<=(18.5):
        bmi_con.set("UNDERWEIGHT")
    elif(bmi_fans>=18.5) and (bmi_fans<=25.0):
        bmi_con.set("HEALTHY")
    else:
        bmi_con.set("OVERWEIGHT")

    pro1=Label(bmi_win2,textvariable=bmi_ANS,background='#ccccff',relief="ridge",font=("Times New Roman","26","bold"))
    pro1.place(x=0,y=0,height=133.3,width=200)
    pro2=Label(bmi_win2,text="BMI",background='#ccccff',relief="ridge",font=("Times New Roman","20","bold"))
    pro2.place(x=200,y=0,height=66.65,width=300)
    pro3=Label(bmi_win2,textvariable=bmi_con,background='#ccccff',relief="ridge",font=("Times New Roman","20","bold"))
    pro3.place(x=200,y=66.65,height=66.65,width=300)

    pro4=Label(bmi_win2,text="INFORMATION AND RANGE",background='#d580ff',relief="ridge",font=("Times New Roman","20","bold"))
    pro4.place(x=0,y=133.3,height=86.65,width=500)
    pro5=Label(bmi_win2,text="UNDERWEIGHT",background='#3399ff',font=("Times New Roman","16","bold"))
    pro5.place(x=0,y=210,height=66.65,width=166.6)
    pro6=Label(bmi_win2,text="NORMAL",background='#33cc33',font=("Times New Roman","16","bold"))
    pro6.place(x=166.6,y=210,height=66.65,width=166.6)
    pro7=Label(bmi_win2,text="OVERWEIGHT",background='#e60000',font=("Times New Roman","16","bold"))
    pro7.place(x=333.2,y=210,height=66.65,width=166.6) 

    pro8=Label(bmi_win2,text="16.0 ---- 18.5--",background='#3399ff',font=("Times New Roman","16","bold"))
    pro8.place(x=0,y=276.65,height=66.65,width=166.6)
    pro9=Label(bmi_win2,text="---------------------",background='#33cc33',font=("Times New Roman","16","bold"))
    pro9.place(x=166.6,y=276.65,height=66.65,width=166.6)
    pro10=Label(bmi_win2,text="--25.0 ---- 40.0",background='#e60000',font=("Times New Roman","16","bold"))
    pro10.place(x=333.2,y=276.65,height=66.65,width=166.6)



    bmi_win2.mainloop()









def convert_ans():
    bmi_weight=float(len_data1.get())
    bmi_height=float(len_data2.get())
    len_clickedone=len_clicked1.get()
    len_clickedtwo=len_clicked2.get()
    
    if(len_clickedone=="Kilogram"):
        if(len_clickedtwo=="Centimeters"):
            BMI(bmi_weight,bmi_height/100)
        elif(len_clickedtwo=="Meters"):
            BMI(bmi_weight,bmi_height)
        elif(len_clickedtwo=="Feets"):
            BMI(bmi_weight,bmi_height*0.3048)
        else:
            BMI(bmi_weight,bmi_height*0.0254)
    else:
        if(len_clickedtwo=="Centimeters"):
            BMI(bmi_weight*0.453592,bmi_height/100)
        elif(len_clickedtwo=="Meters"):
            BMI(bmi_weight*0.453592,bmi_height)
        elif(len_clickedtwo=="Feets"):
            BMI(bmi_weight*0.453592,bmi_height*0.3048)
        else:
            BMI(bmi_weight*0.453592,bmi_height*0.0254)
#---------------------------------------------------------------------------------------------------------------------------
bmi5=Label(bmi_win1,text="WEIGHT :",background='#999999',font=("Times New Roman","30","bold"))
bmi5.place(x=50,y=25,height=100,width=300)
bmi6=Entry(bmi_win1,textvariable=len_data1,background='#333333',fg="white",borderwidth=5,font=("Times New Roman","25","bold"))
bmi6.place(x=550,y=25,height=100,width=400)
bmi7=Label(bmi_win1,text="HEIGHT :",background='#999999',font=("Times New Roman","30","bold"))
bmi7.place(x=50,y=150,height=100,width=300)
bmi8=Entry(bmi_win1,textvariable=len_data2,background='#333333',fg="white",borderwidth=5,font=("Times New Roman","25","bold"))
bmi8.place(x=550,y=150,height=100,width=400)

bmi_button=Button(bmi_win1,text="CONVERT",command=convert_ans,activebackground='#333333',background='green',font=("Times New Roman","30","bold"))
bmi_button.place(x=300,y=275,height=100,width=400)



    






#-----------------------------------------------------------------------------------------------------------------------------



#------____________---------------______________------------_____________-------------_____________



bmi_win1.mainloop()