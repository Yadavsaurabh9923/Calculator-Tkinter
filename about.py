from tkinter import * 


abt_win1=Tk()
abt_win1.title("About")
abt_win1.geometry('800x500')
abt_win1.config(background="#C0CBCF")



abt_label1=Label(abt_win1,text="By : Saurabh Yadav ",background='#C0CBC0',font=("Comic Sans MS","16","bold"))
abt_label1.place(x=20,y=20,height=60,width=300)

abt_label1=Label(abt_win1,text="Email : yadavsaurabh9923@gmail.com ",background='#C0CBC0',font=("Comic Sans MS","16","bold"))
abt_label1.place(x=20,y=100,height=100,width=400)


photo1= PhotoImage(file = r"D:\Python programs\Projects\Calculator\logo")
Button1=Button(abt_win1, text = 'Click Me !', image = photo1)
Button1.place(x=20,y=400,height=50,width=50)


abt_win1.mainloop()
