from tkinter import *
#-------------------------------------------------------------------------------------------------------------------------------------


con_win2=Tk()
con_win2.title("Volume Converter")
con_win2.geometry('1000x600')
con_win2.config(background="#C0CBCF")


len_data1=StringVar()
len_data2=StringVar()

len_options = ["Millilitres","Cubic centimetres","Litres","Cubic metres","Teaspoons(US)","Fluid Ounces(US)","Cups(US)","Pints(US)","Quarts(US)","Gallons(US)","Cubic inches","Cubic feet","Cubic Yards","Tea Spoons(UK)","Tablespoons(UK)","Fluid ounces(UK)","Pints(UK)","Quarts(UK)","Gallons(UK)"
]


len_clicked1=StringVar()
len_clicked1.set(len_options[4])
len_drop1=OptionMenu(con_win2,len_clicked1,*len_options)
len_drop1.place(x=250,y=250,height=50,width=250)


len_clicked2=StringVar()
len_clicked2.set(len_options[4])
len_drop2=OptionMenu(con_win2,len_clicked2,*len_options)
len_drop2.place(x=250,y=550,height=50,width=250)
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
    newlen_value=int(len_value)
    if len_clicked1.get()==len_options[0]:
        if len_clicked2.get()==len_options[0]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*1
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*0.202884
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.067628
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*0.033814
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*0.0422675
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.00211338
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.00105669
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.000264171
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*0.0610237
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.0000353147
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.00000130795
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*0.168936
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*0.0563121
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*0.0351951
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.00175975
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.000879877
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000219969
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[1]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*1
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.000001
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*0.202884
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.067628
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*0.033814
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*0.00422675
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.00211338
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.001105669
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.000264172
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*0.0610237
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.0000353147
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.00000130795
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*0.168936
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*0.0563121
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*0.0351951
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.00175975
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.000879877
            len_data2.set(temp)
        else:
            temp=newlen_value*0.000279969
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[2]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.001
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*202.8841
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*67.62805
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*33.81402
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*4.226753
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*2.113376
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*1.056688
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.264172
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*61.02374
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.0353147
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.00130795
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*168.09364
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*56.31213
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*35.19508
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*1.759754
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.879877
            len_data2.set(temp)
        else:
            temp=newlen_value*0.219969
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[3]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*1000000
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*1000000
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*1000
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*202844.1
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*67628.05
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*33814.02
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*4226.753
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*2113.376
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*1056.688
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*264.1721
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*61023.74
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*35.31467
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*1.307951
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*168936.4
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*56312.13
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*35195.08
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*1759.754
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*879.877
            len_data2.set(temp)
        else:
            temp=newlen_value*219.9692
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[4]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*4.928922
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*4.928922
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.00492892
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.00000492892
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*0.333333
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*0.166667
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*0.0208333
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.0104167
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.00520833
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.00130208
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*0.300781
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.000174063
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.00000644679
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*0.832674
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*0.277558
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*0.173474
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.00867369
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.00433684
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00108421
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[5]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*14.78676
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*14.78676
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.0147868
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.0000147868
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*3
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*0.5
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*0.0625
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.03125
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.015625
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.00390625
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*0.902344
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.00052219
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.0000193404
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*2.498023
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*0.832674
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*0.520421
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.0260211
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.0130105
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00325263
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[6]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*29.57353
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*29.57353
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.0295735
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.0000295735
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*6
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*2
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*0.125
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.0625
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.03125
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.0078125
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*1.804688
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.00104438
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.0000386807
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*4.996045
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*1.665348
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*1.040843
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.0520421
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.0260211
            len_data2.set(temp)
        else:
            temp=newlen_value*0.00650527
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[7]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*236.5882
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*236.5882
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.236588
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.000236588
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*48
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*16
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*8
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*0.5
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.25
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.0625
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*14.4375
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.60835503
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.000309446
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*39.96836
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*13.32279
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*8.326742
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.416337
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.208169
            len_data2.set(temp)
        else:
            temp=newlen_value*0.0520421
            len_data2.set(temp)
    elif len_clicked1.get()==len_options[8]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*473.1765
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*473.1765
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.473176
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.000473176
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*96
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*32
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*16
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*2
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[9]:
            temp=newlen_value*0.5
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.125
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*28.875
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.0167101
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.000618891
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*79.93672
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*26.64557
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*16.65348
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*0.832674
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.416337
            len_data2.set(temp)
        else:
            temp=newlen_value*0.104084
            len_data2.set(temp)
    if len_clicked1.get()==len_options[9]:
        if len_clicked2.get()==len_options[0]:
            temp=newlen_value*946.3529
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[1]:
            temp=newlen_value*946.3529
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[2]:
            temp=newlen_value*0.946353
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[3]:
            temp=newlen_value*0.000946353
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[4]:
            temp=newlen_value*192
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[5]:
            temp=newlen_value*64
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[6]:
            temp=newlen_value*32
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[7]:
            temp=newlen_value*4
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[8]:
            temp=newlen_value*2
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[9]:
            len_data2.set(len_value)
        elif len_clicked2.get()==len_options[10]:
            temp=newlen_value*0.25
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[11]:
            temp=newlen_value*57.75
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[12]:
            temp=newlen_value*0.0334201
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[13]:
            temp=newlen_value*0.00123778
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[14]:
            temp=newlen_value*159.8734
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[15]:
            temp=newlen_value*53.29115
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[16]:
            temp=newlen_value*33.30697
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[17]:
            temp=newlen_value*1.665348
            len_data2.set(temp)
        elif len_clicked2.get()==len_options[18]:
            temp=newlen_value*0.832674
            len_data2.set(temp)
        else:
            temp=newlen_value*0.208169
            len_data2.set(temp)
    
#-------------------------------------------------------------------------------------------------------------------------------------



con_win2_label1=Label(con_win2,textvariable=len_data1,text="BOX 1",background='#E7EFF2',font=("Comic Sans MS","26","bold"))
con_win2_label1.place(x=0,y=0,height=250,width=500)
con_win2_label3=Label(con_win2,text="Unit :",background='#E7EFF2',font=("Comic Sans MS","26","bold"))
con_win2_label3.place(x=0,y=250,height=50,width=250)


con_win2_label2=Label(con_win2,textvariable=len_data2,text="BOX 2",background='#E7EFF2',font=("Comic Sans MS","26","bold"))
con_win2_label2.place(x=0,y=300,height=250,width=500)
con_win2_label3=Label(con_win2,text="Unit :",background='#E7EFF2',font=("Comic Sans MS","26","bold"))
con_win2_label3.place(x=0,y=550,height=50,width=250)


con_win2_b10=Button(con_win2,text="CE",command=len_CE_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b10.place(x=500,y=0,height=120,width=166.6)
con_win2_b1=Button(con_win2,text="7",command=len_bt7_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b1.place(x=500,y=120,height=120,width=166.6)
con_win2_b2=Button(con_win2,text="8",command=len_bt8_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b2.place(x=666.6,y=120,height=120,width=166.6)
con_win2_b3=Button(con_win2,text="9",command=len_bt9_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b3.place(x=833.2,y=120,height=120,width=166.6)
con_win2_b4=Button(con_win2,text="4",command=len_bt4_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b4.place(x=500,y=240,height=120,width=166.6)
con_win2_b5=Button(con_win2,text="5",command=len_bt5_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b5.place(x=666.6,y=240,height=120,width=166.6)
con_win2_b6=Button(con_win2,text="6",command=len_bt6_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b6.place(x=833.2,y=240,height=120,width=166.6)
con_win2_b7=Button(con_win2,text="1",command=len_bt1_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b7.place(x=500,y=360,height=120,width=166.6)
con_win2_b8=Button(con_win2,text="2",command=len_bt2_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b8.place(x=666.6,y=360,height=120,width=166.6)
con_win2_b9=Button(con_win2,text="3",command=len_bt3_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b9.place(x=833.2,y=360,height=120,width=166.6)
con_win2_b11=Button(con_win2,text="0",command=len_bt0_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b11.place(x=666.6,y=480,height=120,width=166.6)
con_win2_b12=Button(con_win2,text=".",command=len_btdot_clicked,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b12.place(x=833.2,y=480,height=120,width=166.6)
con_win2_b13=Button(con_win2,text="Convert",command=speed_convert,activebackground='#949494',background='#000000',fg="white",font=("Comic Sans MS","35","bold"))
con_win2_b13.place(x=666.6,y=0,height=120,width=343.6)


con_win2.mainloop()