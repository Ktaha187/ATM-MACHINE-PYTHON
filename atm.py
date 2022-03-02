from tkinter import*
win=Tk()
win.title("ATM MACHINE")
Label =Label (win, text="ENTER YOUR TRANSACTION",font=('arial', 20))
Label.pack()

win.geometry("500x500")
def close_windows(self):
    self.master.destroy()

def yes():
    top=Toplevel()
    
    def btnClick(number):
        global operator
        operator=operator+str(number)
        text_input.set(operator)
    def btnClear():
        global operator
        operator=" "
        text_input.set(" ")
    def btnEqual():
        global operator
        sumup=str(eval(operator))
        text_input.set(sumup)
        operator=" "
    
    win.title("WELCOME")
    operator=" "
    text_input=StringVar()

    display_box=Entry(top,font=("algerian",50),textvariable=text_input,bd=20,insertwidth=4,bg="indigo",justify="right").grid(columnspan=4)
    button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="500", command=lambda: btnClick("500 ")).grid(row=1, column=0)
    button1 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo", font="algerian",text="1000", command=lambda: btnClick("1000")).grid(row=3, column=0)
    button13 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="5000", command=lambda: btnClick("5000")).grid(row=5, column=0)
    button13 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="10000", command=lambda: btnClick("10000")).grid(row=6, column=0)
    buttonClear = Button(top, padx=20, pady=10, bd=8, fg="white",bg="indigo" ,font="algerian", text="clear", command=btnClear).grid(row=6, column=1)
    buttonEquals=Button(top,padx=16,pady=10,bd=8,fg="white",bg="indigo",text="Only",command=btnEqual).grid(row=6,column=2)
    button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="arial", text="Enter", command=lambda: btnClick("Processing")).grid(row=6, column=3)
    button =Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="arial", text = 'Quit', width = 25, command = close_windows).grid(row=6, column=4)
yes=Button(win,text="FAST CASH", padx=5, pady=5, bd=8,font="algerian", fg="white",bg="black",command=yes).place(x=10, y=70)
def ok():
        top=Toplevel()
        def btnClick(number):
            global operator
            operator = operator + str(number)
            text_input.set(operator)
        def btnClear():
            global operator
            operator = " "
            text_input.set(" ")


        def btnEqual():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = " "

        
        top.title("Menu")
        global operator
        operator=" "
        text_input = StringVar()
        display_box = Entry(top, font=("calibiri", 50), textvariable=text_input, bd=50, insertwidth=5, bg="indigo",
                    justify="right").grid(columnspan=10)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="K.E", command=lambda: btnClick("Bill Account number ")).grid(row=1, column=0)
        button1 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo", font="algerian",text="W.B", command=lambda: btnClick("Bill Account number")).grid(row=3, column=0)
        button13 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="SSG", command=lambda: btnClick("Bill Account number")).grid(row=5, column=0)
        button13 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="ACCOUNT NUMBER", command=bsh).grid(row=6, column=0)
        buttonClear = Button(top, padx=20, pady=10, bd=8, fg="white",bg="indigo" ,font="algerian", text="clear", command=btnClear).grid(row=6, column=1)
        
btOK=Button(win,text="BILL PAYMENTS", padx=5, pady=7, bd=8,font="algerian", fg="white",bg="black",command=ok).place(x=10, y=190)

                
def bsh():
        top=Toplevel()
        def btnClick(number):
            global operator
            operator = operator + str(number)
            text_input.set(operator)

        def btnClear():
            global operator
            operator = " "
            text_input.set(" ")


        def btnEqual():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = " "

        
        top.title("Account number")
        global operator
        operator=" "
        text_input = StringVar()
        display_box = Entry(top, font=("calibiri", 30), textvariable=text_input, bd=5, insertwidth=2, bg="indigo",
                    justify="right").grid(columnspan=10)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="1", command=lambda: btnClick("1 ")).grid(row=1, column=0)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="2", command=lambda: btnClick("2 ")).grid(row=1, column=1)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="3", command=lambda: btnClick("3 ")).grid(row=1, column=2)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="4", command=lambda: btnClick("4 ")).grid(row=2, column=0)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="5", command=lambda: btnClick("5 ")).grid(row=2, column=1)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="6", command=lambda: btnClick("6 ")).grid(row=2, column=2)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="7", command=lambda: btnClick("7 ")).grid(row=3, column=0)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="8", command=lambda: btnClick("8 ")).grid(row=3, column=1)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="9", command=lambda: btnClick("9 ")).grid(row=3, column=2)
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="0", command=lambda: btnClick("0")).grid(row=4, column=0)
        
        buttonClear = Button(top, padx=20, pady=10, bd=8, fg="white",bg="indigo" ,font="algerian", text="clear", command=btnClear).grid(row=6, column=1)
        

    
def csh():
        top=Toplevel()
        def btnClick(number):
            global operator
            operator = operator + str(number)
            text_input.set(operatoar)

        def btnClear():
            global operator
            operator = " "
            text_input.set(" ")


        def btnEqual():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = " "

        
        top.title("account Number")
        global operator
        operator=" "
        text_input = StringVar()
        top.geometry("400x400")
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="ACCOUNT NUMBER", command=bsh).grid(row=1, column=0)
        

btcsh=Button(win,text="BALANCE INQUIRY", padx=5, pady=7, bd=8,font="algerian", fg="white",bg="black",command=csh).place(x=10, y=290)
def dsh():
        top=Toplevel()
        def btnClick(number):
            global operatora
            operator = operator + str(number)
            text_input.set(operator)
 
        def btnClear():
            global operator
            operator = " "
            text_input.set(" ")


        def btnEqual():
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = " "

        
        top.title("Menu")
        global operator
        operator=" "
        text_input = StringVar()
        top.geometry("400x400")
        button7 = Button(top, padx=16, pady=10, bd=8, fg="white",bg="indigo",font="algerian", text="ACCOUNT NUMBER", command=bsh).grid(row=1, column=0)
        
btdsh=Button(win,text="FUNDS TRANSFER", padx=5, pady=7, bd=8,font="algerian", fg="white",bg="black",command=csh).place(x=10, y=390)

  