from tkinter import *

window = Tk()
window.title("BMI calculator")
window.minsize(200, 200)

myText = Label(window, text="Enter the weight(kg)")
myText.config(pady=10)
myText.pack()

myWeight = Entry(width=10)
myWeight.pack()

myText2 = Label(window, text="Enter the height(cm)")
myText2.config(pady=10)
myText2.pack()

myHeight = Entry(width=10)
myHeight.pack()


def clickedBtn():
    if myWeight.get() == "" or myHeight.get() == "":
        labelText("Enter both weight and height!")
    else:

        try:
            weight = int(myWeight.get())
            height = int(myHeight.get())
            bmi = weight / (height * 0.01 * height * 0.01)
            if bmi < 18.5:

                labelText(f"your BMI is {round(bmi, 2)}. You are under weight.")
            elif 18.5 < bmi < 24.9:
                labelText(f"your BMI is {round(bmi, 2)}. You are normal weight.")
            elif 25 < bmi < 29.9:
                labelText(f"your BMI is {round(bmi, 2)}. You are over weight.")
            elif 30 < bmi:
                labelText(f"Your BMI is {round(bmi, 2)}. You are obase.")
        except:
            labelText("Enter a valid number!")


myButton = Button(text="calculate")
myButton.config(padx=10, bg="blue", fg="white", command=clickedBtn)
myButton.pack()


label = Label()
def labelText(text):
    label.config(text=text)
    label.pack()



mainloop()
