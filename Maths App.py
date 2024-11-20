from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import pyttsx3

class MathsApp:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(202 * black_space + "Python Maths App")
        self.root.resizable(width =False, height=False)
        self.root.geometry("1360x700+0+0")

        firstValue =IntVar()
        SecondValue =IntVar()
        CorrectAnswer =IntVar()
        EnterAnswer =IntVar()
        PointAwarded =IntVar()
        RandomOperator = StringVar()
        op = StringVar()

        op =['+', '-', '/', '*']
        RandomOperator.set(random.choice(op))
        FirstValue.set(random.randint(1,50))
        SecondValue.set(random.randint(1,50))
        EnterAnswer.set("")

        MainFrame = Frame(Self.root, bd=10, width=1350, height=1350, relief = RIDGE, bg ="cadet blue")
        MainFrame.grid()
        TitleFrames= Frame(MainFrame, bd=10, width=1320, height=100, relief = RIDGE)

        TitleFrames.grid(row = 0, column = 0)

        TitleFrame = Frame(TitleFrames, bd=10, width=1320, height=100, relief = RIDGE, bg="cadet blue")
        TitleFrame.grgid(row = 0, column=0, padx=6)
        Mathsframe = Frame(MainFrame, bd=10, width=1320, height=480, relief = RIDGE)
        MathsFrame.grid(row = 1, column=0)
        ButtonFrame = Frame(MainFrame, bd=10, width=1320, height=50, relief = RIDGE)
        ButtonFrame.grid(row = 2,column=0)

        LeftFrame = Frame(MathsFrame, bd=10, width=440, hieght=400, relief=RIDGE)
        LeftFrame.grid(row = 0,column=0)

        MidFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        MidFrame.grid(row = 0,column=1)

        RightFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        RightFrame.grid(row = 0,column=2)

        Sapi = pyttsx3.init()
        Sapi.say("Welcome to maths app created using python")
        Sapi.runAndWait()

        def CallOperator():
            match RandomOperator.get():
                case "+":
                    Sapi.say("%s Plus %s" % (FirstValue.get() , SecondValue.get()))
                case "-":
                    Sapi.say("%s Subtracted b y %s" % (FirstValue.get() , SecondValue.get()))
                case "*":
                    Sapi.say("%s Multiplication by %s" % (FirstValue.get() , SecondValue.get()))
                case "/":
                    Sapi.say("%s Divided by %s" % (FirstValue.get() , SecondValue.get()))
            Sapi.runAndWait()
        CallOperator()

        def iExit():
            Sapi.say("Confirm if you want to exit")
            Sapi.runAndWait()
            iExit = tkinter.messagebox.askyesno("Maths App", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            FirstValue.set("")
            SecondValue.set("")
            CorrectAnswer.set("")
            EnterAnswer.set("")
            PointAwarded.set("")
            RandomOperator("")

        def GenerateNum():
            x = ranodm.randint(1,50)
            q = random.randint(1,50)
            FirstValue.set(x)
            SecondValue.set(q)
            op =['+', '-', '/', '*']
            RandomOperator.set(random.choice(op))
            CallOperator()
            EnterAnswer.set("")
            return

        def CheckAnswer():
            num1 = float(FirstValue.get())
            num2 = float(SecondValue.get())
            ans = float(EnterAnswer.get())
            oper = (RandomOperator.get())
            addOne = PointAwarded.get()
            if (oper == "+"):
                num3 = num1 + num2
                if (ans == num3):
                    CorrectAnswer.set("What's Correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    enterAnswer.set("")
                    GenerateNum()
            if (oper == "-"):
                num3 = num1 - num2
                if (ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectANswer.set(str('%.2f'%(num3)))
                    Sapi,say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()
            if (oper == "*"):
                num3 = num1 * num2
                if (ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()
            if (oper == "/"):
                num3 = num1 / num2
                if(ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi,say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    GenerateNum()
                    EnterAnswer.set("")
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()

            ans1 = float(Pointawarded.get())
            if (ans1 == float(2)):
                self.Level2_window()

            self.lblTitle = Label(TitleFrames, font=('arial', 50, 'bold'), text ="Level 2 Python Maths App" , bd=7, bg="cadet blue")
            self.lblTitle.grid(row = 0, column=0, padx=222)

            self.lblFirstValue = Label(LeftFrame, font=('arial',28, 'bold'), text="First Value",bd=7, padx2,pady=40,
                                       justify=LEFT)
            self.lblFirstValue.grid(row=0,column=0, padx=31)
            self.txtFirstValue = Entry(LeftFrame,font=('arial', 28,'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=FirstValue)
            self.txtFirstValue.grid(row=1,column=0, padx=31)

            self.lblCorrectAns = Label(LeftFrame, font=('arial',28,'bold'),text="Correct Answer", bd=7, padx=2,pady=40,
                                       justify='center')
            self.lblCorrectAns.grid(row=2,column=0, padx=31)
            self.txtCorrectAns = Entry(LeftFrame,font=('arial', 28, 'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=CorrectAnswer)
            self.txtCorrectAns.grid(row=3,column=0, padx=31)

            self.lblRandomOp = Label(MidFrame, font=('arial',28, 'bold'),text="Random Operator",bd=7, padx=2,pady=40,
                                     justify=LEFT)
            self.lblRandomOp.grid(row=0,column=0, padx=31)
            self.txtRandomOp = Entry(MidFrame,font=('arial', 28,'bold'), bd=5, width=18,justify = 'center',
                                     textvariable=RandomOperator)
            self.txtRandomOp.grid(row=1,column=0, padx=31)

            self.lblEnterAns = Label(MidFrame, font=('arial',28, 'bold'),text="Enter Answer", bd=7, padx=7, padx=2,pady=40,
                                     justify='center')
            self.lblEnterAns.grid(row=2,column=0, padx=31)
            self.txtEnterAns = Entry(MidFrame,font=('arial',28,'bold'), bd=5, width=18,justify = 'center',
                                     textvariable=EnterAnswer)
            self.txtEnterAns.grid(row=3,column=0, padx=31)
            self.txtEnterAns.focus_set()

            self.lblSecondValue = Label(RightFrame, font=('arial',28, 'bold'),text="Second Value", bd=7, padx=2,pady=38,
                                        justify=LEFT)
            self.lblSecondValue.grid(row=0,column=0, padx=31)
            self.txtSecondValue = Entry(RightFrame, font=('arial', 28,'bold'), bd=5, width=16,justify = 'center',
                                        textvariable=SecondValue)
            self.txtSecondValue.grid(row=1,column=0,  padx=31)

            self.lblPointAward = Label(RightFrame, font=('arial',28,'bold'),text="Point Awarded", bd=7, padx=2,pady=38,
                                       justify='center')
            self.lblPointAward.grid(row=2,column=0, padx=31)
            self.txtPointAward = Entry(RightFrame,font=('arial',28,'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=PointAwarded)
            self.txtPointAward.grid(row=3,column=0, padx=31)

            self.btnResult=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30,'bold'), padx=25,
                                  width=11, height=1, text="Check Result", bg="cadet blue", command=CheckAnswer).grid(row=0,column=0,padx=3)
            self.btnNewGame=Button(ButtonFrame, pady=1, bd=4, font = ('arial', 30,'bold'), padx=25,
                                   width=11, hieght=1, text="New Game", command=GenerateNum).grid(row=0,column=1,padx=3)
            self.btnReset=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30, 'bold'), padx=25,
                                 width=11, height=1, text="Reset", bg="cadet blue", command=Reset).grid(row=0,column=2,padx=3)
            self.btnExit=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30, 'bold'), padx=25,
                                width=11, width=1, text="Exit", command=iExit).grid(row=0,column=3,padx=3)



        def Level2_window(self):
            self.secondLevelWindow = TopLevel(self.root)
            self.app = Level2MathsApp(self.secondLevelWindow)

class Level2MathsApp:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(202 * black_space + "Python Maths App")
        self.root.resizable(width =False, height=False)
        self.root.geometry("1360x700+0+0")

        firstValue =IntVar()
        SecondValue =IntVar()
        CorrectAnswer =IntVar()
        EnterAnswer =IntVar()
        PointAwarded =IntVar()
        RandomOperator = StringVar()
        op = StringVar()

        op =['+', '-', '/', '*']
        RandomOperator.set(random.choice(op))
        FirstValue.set(random.randint(1,50))
        SecondValue.set(random.randint(1,50))
        EnterAnswer.set("")

        MainFrame = Frame(Self.root, bd=10, width=1350, height=1350, relief = RIDGE, bg ="cadet blue")
        MainFrame.grid()
        TitleFrames= Frame(MainFrame, bd=10, width=1320, height=100, relief = RIDGE)

        TitleFrames.grid(row = 0, column = 0)

        TitleFrame = Frame(TitleFrames, bd=10, width=1320, height=100, relief = RIDGE, bg="cadet blue")
        TitleFrame.grgid(row = 0, column=0, padx=6)
        Mathsframe = Frame(MainFrame, bd=10, width=1320, height=480, relief = RIDGE)
        MathsFrame.grid(row = 1, column=0)
        ButtonFrame = Frame(MainFrame, bd=10, width=1320, height=50, relief = RIDGE)
        ButtonFrame.grid(row = 2,column=0)

        LeftFrame = Frame(MathsFrame, bd=10, width=440, hieght=400, relief=RIDGE)
        LeftFrame.grid(row = 0,column=0)

        MidFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        MidFrame.grid(row = 0,column=1)

        RightFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        RightFrame.grid(row = 0,column=2)

        Sapi = pyttsx3.init()
        Sapi.say("Welcome to maths app created using python")
        Sapi.runAndWait()

        def CallOperator():
            match RandomOperator.get():
                case "+":
                    Sapi.say("%s Plus %s" % (FirstValue.get() , SecondValue.get()))
                case "-":
                    Sapi.say("%s Subtracted b y %s" % (FirstValue.get() , SecondValue.get()))
                case "*":
                    Sapi.say("%s Multiplication by %s" % (FirstValue.get() , SecondValue.get()))
                case "/":
                    Sapi.say("%s Divided by %s" % (FirstValue.get() , SecondValue.get()))
            Sapi.runAndWait()
        CallOperator()

        def iExit():
            Sapi.say("Confirm if you want to exit")
            Sapi.runAndWait()
            iExit = tkinter.messagebox.askyesno("Maths App", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            FirstValue.set("")
            SecondValue.set("")
            CorrectAnswer.set("")
            EnterAnswer.set("")
            PointAwarded.set("")
            RandomOperator("")

        def GenerateNum():
            x = ranodm.randint(1,50)
            q = random.randint(1,50)
            FirstValue.set(x)
            SecondValue.set(q)
            op =['+', '-', '/', '*']
            RandomOperator.set(random.choice(op))
            CallOperator()
            EnterAnswer.set("")
            return

        def CheckAnswer():
            num1 = float(FirstValue.get())
            num2 = float(SecondValue.get())
            ans = float(EnterAnswer.get())
            oper = (RandomOperator.get())
            addOne = PointAwarded.get()
            if (oper == "+"):
                num3 = num1 + num2
                if (ans == num3):
                    CorrectAnswer.set("What's Correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    enterAnswer.set("")
                    GenerateNum()
            if (oper == "-"):
                num3 = num1 - num2
                if (ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectANswer.set(str('%.2f'%(num3)))
                    Sapi,say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()
            if (oper == "*"):
                num3 = num1 * num2
                if (ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi.say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    EnterAnswer.set("")
                    GenerateNum()
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()
            if (oper == "/"):
                num3 = num1 / num2
                if(ans == num3):
                    CorrectAnswer.set("What's correct")
                    Sapi.say(num3)
                    Sapi,say("That is the correct answer")
                    Sapi.runAndWait()
                    PointAwarded.set(addOne  + 1)
                    GenerateNum()
                    EnterAnswer.set("")
                else:
                    CorrectAnswer.set(str('%.2f'%(num3)))
                    Sapi.say("Incorrect Answer, the correct answer is")
                    Sapi.say(num3)
                    Sapi.runAndWait()
                    EnterAnswer.set("")
                    GenerateNum()

            ans1 = float(Pointawarded.get())
            if (ans1 == float(2)):
                self.Level2_window()

            self.lblTitle = Label(TitleFrames, font=('arial', 50, 'bold'), text ="Level 2 Python Maths App" , bd=7, bg="cadet blue")
            self.lblTitle.grid(row = 0, column=0, padx=222)

            self.lblFirstValue = Label(LeftFrame, font=('arial',28, 'bold'), text="First Value",bd=7, padx2,pady=40,
                                       justify=LEFT)
            self.lblFirstValue.grid(row=0,column=0, padx=31)
            self.txtFirstValue = Entry(LeftFrame,font=('arial', 28,'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=FirstValue)
            self.txtFirstValue.grid(row=1,column=0, padx=31)

            self.lblCorrectAns = Label(LeftFrame, font=('arial',28,'bold'),text="Correct Answer", bd=7, padx=2,pady=40,
                                       justify='center')
            self.lblCorrectAns.grid(row=2,column=0, padx=31)
            self.txtCorrectAns = Entry(LeftFrame,font=('arial', 28, 'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=CorrectAnswer)
            self.txtCorrectAns.grid(row=3,column=0, padx=31)

            self.lblRandomOp = Label(MidFrame, font=('arial',28, 'bold'),text="Random Operator",bd=7, padx=2,pady=40,
                                     justify=LEFT)
            self.lblRandomOp.grid(row=0,column=0, padx=31)
            self.txtRandomOp = Entry(MidFrame,font=('arial', 28,'bold'), bd=5, width=18,justify = 'center',
                                     textvariable=RandomOperator)
            self.txtRandomOp.grid(row=1,column=0, padx=31)

            self.lblEnterAns = Label(MidFrame, font=('arial',28, 'bold'),text="Enter Answer", bd=7, padx=7, padx=2,pady=40,
                                     justify='center')
            self.lblEnterAns.grid(row=2,column=0, padx=31)
            self.txtEnterAns = Entry(MidFrame,font=('arial',28,'bold'), bd=5, width=18,justify = 'center',
                                     textvariable=EnterAnswer)
            self.txtEnterAns.grid(row=3,column=0, padx=31)
            self.txtEnterAns.focus_set()

            self.lblSecondValue = Label(RightFrame, font=('arial',28, 'bold'),text="Second Value", bd=7, padx=2,pady=38,
                                        justify=LEFT)
            self.lblSecondValue.grid(row=0,column=0, padx=31)
            self.txtSecondValue = Entry(RightFrame, font=('arial', 28,'bold'), bd=5, width=16,justify = 'center',
                                        textvariable=SecondValue)
            self.txtSecondValue.grid(row=1,column=0,  padx=31)

            self.lblPointAward = Label(RightFrame, font=('arial',28,'bold'),text="Point Awarded", bd=7, padx=2,pady=38,
                                       justify='center')
            self.lblPointAward.grid(row=2,column=0, padx=31)
            self.txtPointAward = Entry(RightFrame,font=('arial',28,'bold'), bd=5, width=16,justify = 'center',
                                       textvariable=PointAwarded)
            self.txtPointAward.grid(row=3,column=0, padx=31)

            self.btnResult=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30,'bold'), padx=25,
                                  width=11, height=1, text="Check Result", bg="cadet blue", command=CheckAnswer).grid(row=0,column=0,padx=3)
            self.btnNewGame=Button(ButtonFrame, pady=1, bd=4, font = ('arial', 30,'bold'), padx=25,
                                   width=11, hieght=1, text="New Game", command=GenerateNum).grid(row=0,column=1,padx=3)
            self.btnReset=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30, 'bold'), padx=25,
                                 width=11, height=1, text="Reset", bg="cadet blue", command=Reset).grid(row=0,column=2,padx=3)
            self.btnExit=Button(ButtonFrame, pady=1, bd=4, font =('arial', 30, 'bold'), padx=25,
                                width=11, width=1, text="Exit", command=iExit).grid(row=0,column=3,padx=3)


if __name__=='__main__':
    root = Tk()
    application = MathsApp(root)
    root.mainloop()




