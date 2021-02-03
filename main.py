from tkinter import *
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from tkinter import messagebox


#=======================Creating Basic Window===================================#
window = Tk()
window.geometry("700x600+0+0")    # size of the window width:- 500, height:- 375
#window.resizable(0,0)          # To make window size constant
window.iconbitmap("C:\\Users\winsa\Desktop\Semester_3\INT_213(Python)\Project\\my_icon.ico")
window.title("Currency Converter")   # title of the window

#=======================Importing values from file================================#
CountryName=[]
CurrencyName=[]
Cvalue=[]
f=open("C:\\Users\winsa\Desktop\Semester_3\INT_213(Python)\Project\Currency rate.txt","r")
a=f.read()
b=a.split()
for i in range(len(b)):
    if(i%3==0):
        CountryName.append(b[i])
    elif(i%3==1):
        CurrencyName.append(b[i])
    else:
        Cvalue.append(float(b[i]))
f.close()
#==================================================================================#

#===========================Defining Variable and Functions =======================#
Curr1=StringVar(window)
Curr1.set("NIL")
Curr2=StringVar(window)
Curr2.set("NIL")
Value1=StringVar(window)
Value1.set(0)
Value2=StringVar(window)
Value2.set(0)

def convert():
    if (var1.get() not in CountryName) or (var2.get()not in CountryName):
        messagebox.showinfo("Country Name Error","Sorry!!!\nPlease, Check your selected country Name?")
    if(Value1.get().isnumeric()==False ):
        messagebox.showerror("Value Error","Please check the value you inserted.")
    val=int()
    a=CountryName.index(var1.get())
    x=int(Value1.get())/Cvalue[a]
    b=CountryName.index(var2.get())
    z=str("%d"%int(Cvalue[b]*x))
    a1=z[::-1]
    r=len(str(z))
    c=str()
    for i in range(0,r,3):
        if(len(a1[i:])>3):
            c=c+a1[i:3+i]+","
        else:
            c=c+a1[i:3+i]
    Value2.set(c[::-1])
    
def FindCurrency1():
    for i in range(len(CountryName)):
        if(CountryName[i]==var1.get()):
            Curr1.set(CurrencyName[i])
def FindCurrency2():
    for i in range(len(CountryName)):
        if(CountryName[i]==var2.get()):
            Curr2.set(CurrencyName[i])

def change1(*args):
    var1.get()
    FindCurrency1()
def change2(*args):
    var2.get()
    FindCurrency2()
    
#==========================================================================================#

#=================================Creating Frames==========================================#

TopFrame=Frame(window,height=80,width=700,relief=FLAT,bg='black')
TopFrame.pack(side=TOP,fill=X)
MidFrame=Frame(window,height=180,width=700,relief=SUNKEN)
MidFrame.pack(side=TOP)
BottomFrame=Frame(window,height=340,width=700,relief=GROOVE)
BottomFrame.pack(side=TOP,fill=X,pady=10)
#================================================================================#

#======================Designing TopFrame =======================================#
Banner=ImageTk.PhotoImage(Image.open("C:\\Users\winsa\Desktop\Semester_3\INT_213(Python)\Project\image.gif"))
Banner1=Label(TopFrame,image=Banner)
Banner1.pack(side=TOP,fill=X)

#=================================================================================#

#============================Designing MidFrame ==================================#
var1=StringVar(window)                                             #Declaring variable for Country Name1
var1.set("--From Country1--")                                           #Setting variable to first element from array CountryName
var1.trace("w",change1)                                            
Menu=OptionMenu(MidFrame,var1,*CountryName,command=FindCurrency1())    
Menu.grid(row=0,column=0,sticky='ew')

var2=StringVar(window)                                            #Declaring ariable for Country Name1
var2.set('--To Country2--')                                          #Setting variable to first element from array CountryName
var2.trace("w",change2)                                           
Menu2=OptionMenu(MidFrame,var2,*CountryName,command=FindCurrency2()) 
Menu2.grid(row=0,column=2,sticky='ew')

Country1=Entry(MidFrame,textvariable=Value1,justify=RIGHT,font="bold")
Country1.grid(row=2,column=0)
currency=Label(MidFrame,textvariable=Curr1,font="times-new 10 bold")
currency.grid(row=2,column=1,sticky='w')                          #Adjusting to west side of 2row 3coluumn
                      
Country2=Label(MidFrame,textvariable=Value2,bg='white',fg='green',width=12,anchor='w',font=('times-new 10 bold'))
Country2.grid(row=2,column=2,sticky='ew')
currency=Label(MidFrame,textvariable=Curr2,font="times-new 10 bold")
currency.grid(row=2,column=3,sticky='ew')
                      
icon=ImageTk.PhotoImage(Image.open("C:\\Users\winsa\Desktop\Semester_3\INT_213(Python)\Project\Convert_Image.jpg"))
Convert=Button(MidFrame,image=icon,command=convert,height=40,width=100)
Convert.grid(row=1,column=1)   



#==================================================================================================================#

#============================Designing BottomFrame ================================================================#
def CreateWindow():
    top=Toplevel()
    top.title("Currency Rate In Dollar")
    
    def SearchCountry():
        if(search.get().capitalize() not in CountryName):
            messagebox.showerror("Error","Sorry! Country Not Found")
        else:
            CurrencyRate.tag_delete("here")
            i=2.00+float(CountryName.index(search.get().capitalize()))
            CurrencyRate.tag_add("here", str(i),str(i+1))
            CurrencyRate.tag_config("here", background="yellow", foreground="blue")
    
    search=StringVar(top)
    searchbox=Entry(top,textvariable=search, justify=LEFT ,font="times-new 20 bold")
    searchbox.grid(column=0,row=0)
    btn=Button(top,text="Search",command=SearchCountry,font="times-new 20 bold")
    btn.grid(column=1,row=0)
    
    CurrencyRate=Text(top,wrap=WORD)
    CurrencyRate.grid(column=0,row=1,columnspan=2)
    CurrencyRate.insert(INSERT, "S.N\tCurrency Name\t\t\tValue(In U.S. Dollar)")
    for i in range(len(CountryName)):
        CurrencyRate.insert(INSERT,"\n"+str(i+1)+")\t"+CurrencyName[i]+"\t\t\t"+str(Cvalue[i]))
    CurrencyRate.configure(bg='black',fg='green',font=('times-new',18))
    backbtn=Button(top,text="Exit",command=top.destroy,font="times-new 20 bold")
    backbtn.grid(column=0,row=2)
    top.mainloop()

ShowCurr=Button(BottomFrame,text="Show Currency Rate",command=CreateWindow,font=("times-new 10 bold"))
ShowCurr.pack(side=TOP)

scrollbar = Scrollbar(BottomFrame,jump=1)
scrollbar.pack( side = RIGHT, fill = Y )

day=[]
month=[]
value=[]
f=open("C:\\Users\winsa\Desktop\Semester_3\INT_213(Python)\Project\Chart.txt","r")
a=f.read()
f.close()
b=a.split()
for i in range(len(b)):
    if(i%9==1):
        day.append(int(b[i]))
    if(i%9==2):
        month.append(b[i])
    if(i%9==7):
        value.append(float(b[i]))
for i in range(len(day)):
    day[i]=str(day[i])+"-"+month[i][0:3]

fig = Figure(figsize=(6,6))
a=fig.add_subplot(111)
a.plot(day[12:],value[12:])
a.set_title("Graph of Indian Currency rate with respect to US Dollar")
a.set_xlabel("Date")
a.set_ylabel("Value of Currency")
canvas = FigureCanvasTkAgg(fig, master=BottomFrame)
canvas.get_tk_widget().pack(fill=X)
canvas.draw()



#===================================================================================================================#


window.mainloop()


