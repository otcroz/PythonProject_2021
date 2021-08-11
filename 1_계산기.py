from tkinter import*
from tkinter import messagebox

####변수 정의####
current = ''
btnList = [None]*10
i,k,j = 0,0,0
num = 1
xPos = 0
yPos = 110

####함수 정의####

#1. 입력창에 입력되는 함수
def input(value):
    current = inputBox.get()   
    if current == "0" :
        inputBox.delete(0,"end")
        inputBox.insert(0, str(value))
    else:
        inputBox.delete(0,"end")
        inputBox.insert(0, str(current) + str(value))

#2. 입력창 계산 함수
def calculate():
    try:
        current = inputBox.get()
        ans = eval(current)
        inputBox.delete(0,"end")
        inputBox.insert(0, str(ans))
    except SyntaxError:
        messagebox.showinfo("error","완성되지 않은 수식입니다.")

#3. 입력창 초기화 함수
def reset():
    inputBox.delete(0,"end")
    inputBox.insert(0, str(0))

#4. 입력창 값 하나씩 지우기
def delete():
    current = inputBox.get()
    curCount = len(current)
    inputBox.delete(curCount - 1,"end")

####기본 설정####
window=Tk()
window.title("계산기")
window.geometry("400x560")
window.resizable(width=FALSE,height=FALSE)
window.configure(bg="ghostwhite")

####계산 입력창, 결과창####

inputBox = Entry(window, font=("System", 48), justify='right')
inputBox.insert(0,"")
inputBox.place(x=0, y=0, width = 400, height = 110)

####계산기 버튼####

#1. 기타 버튼

acButton = Button(window, text="AC", width = 8, height = 3, 
    font=("System", 21), bg = "lightslategrey", activebackground = "lightgrey", relief = "ridge",
    command = reset)
calButton = Button(window, text="=", width = 8, height = 3, 
    font=("System", 21), bg = "lightslategrey", activebackground = "lightgrey", relief = "ridge",
    command = calculate)
delButton = Button(window, text="DEL", width = 8, height = 3, 
    font=("System", 21), bg = "lightslategrey", activebackground = "lightgrey", relief = "ridge",
    command = delete)

acButton.place(x=0, y=380)
calButton.place(x=200, y=380)
delButton.place(x=300, y=470)

#2. 숫자 버튼
for i in range(0,10):
    btnList[i] = Button(window, text = str(i), width = 8, height = 3, 
    font=("System", 21), bg = "lightblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda x = i : input(x)) #값 수정

btnList[0].place(x=100, y=380)

for k in range(0,3):
    for j in range(0,3):
        btnList[num].place(x= xPos, y= yPos)
        num += 1
        xPos += 100
    yPos += 90
    xPos = 0

#3. 연산 버튼

divButton = Button(window, text="/", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("/"))
mulButton = Button(window, text="*", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("*"))
sumButton = Button(window, text="+", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("+"))
subButton = Button(window, text="-", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("-"))
dotButton = Button(window, text=".", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("."))
perButton =Button(window, text="%", width = 8, height = 3, 
    font=("System", 21), bg = "lightsteelblue", activebackground = "lightgrey", relief = "ridge",
    command = lambda : input("/100"))

divButton.place(x=300, y=110)
mulButton.place(x=300, y=200)
sumButton.place(x=300, y=290)
subButton.place(x=300, y=380)
dotButton.place(x=200, y=470)
perButton.place(x=100, y=470)

window.mainloop()