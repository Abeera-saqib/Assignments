from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import pyttsx3


class MathsApp:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "Python Maths App")
        self.root.resizable(width=False, height=False)
        self.root.geometry("1360x700+0+0")

        # Corrected variable initializations
        FirstValue = IntVar()
        SecondValue = IntVar()
        CorrectAnswer = StringVar()
        EnterAnswer = StringVar()
        PointAwarded = IntVar()
        RandomOperator = StringVar()

        # Assigning operator and random values
        op = ['+', '-', '/', '*']
        RandomOperator.set(random.choice(op))
        FirstValue.set(random.randint(1, 50))
        SecondValue.set(random.randint(1, 50))
        EnterAnswer.set("")

        # Main frame
        MainFrame = Frame(self.root, bd=10, width=1350, height=1350, relief=RIDGE, bg="cadet blue")
        MainFrame.grid()
        TitleFrame = Frame(MainFrame, bd=10, width=1320, height=100, relief=RIDGE, bg="cadet blue")
        TitleFrame.grid(row=0, column=0, padx=6)

        # Maths Frame
        MathsFrame = Frame(MainFrame, bd=10, width=1320, height=480, relief=RIDGE)
        MathsFrame.grid(row=1, column=0)
        ButtonFrame = Frame(MainFrame, bd=10, width=1320, height=50, relief=RIDGE)
        ButtonFrame.grid(row=2, column=0)

        LeftFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        LeftFrame.grid(row=0, column=0)

        MidFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        MidFrame.grid(row=0, column=1)

        RightFrame = Frame(MathsFrame, bd=10, width=440, height=400, relief=RIDGE)
        RightFrame.grid(row=0, column=2)

        # Speech initialization
        Sapi = pyttsx3.init()
        Sapi.say("Welcome to the Maths App created using Python.")
        Sapi.runAndWait()

        # Functions
        def CallOperator():
            operator = RandomOperator.get()
            if operator == "+":
                Sapi.say(f"{FirstValue.get()} plus {SecondValue.get()}")
            elif operator == "-":
                Sapi.say(f"{FirstValue.get()} minus {SecondValue.get()}")
            elif operator == "*":
                Sapi.say(f"{FirstValue.get()} multiplied by {SecondValue.get()}")
            elif operator == "/":
                Sapi.say(f"{FirstValue.get()} divided by {SecondValue.get()}")
            Sapi.runAndWait()

        def iExit():
            confirm_exit = tkinter.messagebox.askyesno("Maths App", "Confirm if you want to exit")
            if confirm_exit:
                root.destroy()

        def Reset():
            FirstValue.set(random.randint(1, 50))
            SecondValue.set(random.randint(1, 50))
            CorrectAnswer.set("")
            EnterAnswer.set("")
            PointAwarded.set(0)
            RandomOperator.set(random.choice(op))

        def GenerateNum():
            FirstValue.set(random.randint(1, 50))
            SecondValue.set(random.randint(1, 50))
            RandomOperator.set(random.choice(op))
            EnterAnswer.set("")
            CallOperator()

        def CheckAnswer():
            num1 = float(FirstValue.get())
            num2 = float(SecondValue.get())
            operator = RandomOperator.get()
            user_answer = float(EnterAnswer.get())
            correct_answer = 0

            if operator == "+":
                correct_answer = num1 + num2
            elif operator == "-":
                correct_answer = num1 - num2
            elif operator == "*":
                correct_answer = num1 * num2
            elif operator == "/":
                correct_answer = num1 / num2

            if user_answer == correct_answer:
                CorrectAnswer.set("Correct!")
                PointAwarded.set(PointAwarded.get() + 1)
                Sapi.say("Correct Answer!")
            else:
                CorrectAnswer.set(f"Incorrect! Correct is: {correct_answer:.2f}")
                Sapi.say(f"Incorrect. The correct answer is {correct_answer:.2f}.")
            Sapi.runAndWait()
            GenerateNum()

        # GUI Widgets
        Label(TitleFrame, text="Python Maths App", font=('arial', 50, 'bold'), bg="cadet blue").grid(row=0, column=0)

        Label(LeftFrame, text="First Value:", font=('arial', 20, 'bold')).grid(row=0, column=0)
        Entry(LeftFrame, textvariable=FirstValue, font=('arial', 20)).grid(row=0, column=1)

        Label(LeftFrame, text="Second Value:", font=('arial', 20, 'bold')).grid(row=1, column=0)
        Entry(LeftFrame, textvariable=SecondValue, font=('arial', 20)).grid(row=1, column=1)

        Label(MidFrame, text="Operator:", font=('arial', 20, 'bold')).grid(row=0, column=0)
        Entry(MidFrame, textvariable=RandomOperator, font=('arial', 20)).grid(row=0, column=1)

        Label(MidFrame, text="Your Answer:", font=('arial', 20, 'bold')).grid(row=1, column=0)
        Entry(MidFrame, textvariable=EnterAnswer, font=('arial', 20)).grid(row=1, column=1)

        Label(RightFrame, text="Points:", font=('arial', 20, 'bold')).grid(row=0, column=0)
        Entry(RightFrame, textvariable=PointAwarded, font=('arial', 20)).grid(row=0, column=1)

        Label(RightFrame, text="Feedback:", font=('arial', 20, 'bold')).grid(row=1, column=0)
        Entry(RightFrame, textvariable=CorrectAnswer, font=('arial', 20)).grid(row=1, column=1)

        Button(ButtonFrame, text="Check Answer", command=CheckAnswer, font=('arial', 20)).grid(row=0, column=0)
        Button(ButtonFrame, text="New Question", command=GenerateNum, font=('arial', 20)).grid(row=0, column=1)
        Button(ButtonFrame, text="Reset", command=Reset, font=('arial', 20)).grid(row=0, column=2)
        Button(ButtonFrame, text="Exit", command=iExit, font=('arial', 20)).grid(row=0, column=3)

        CallOperator()


if __name__ == "__main__":
    root = Tk()
    app = MathsApp(root)
    root.mainloop()
