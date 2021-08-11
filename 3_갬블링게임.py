from tkinter import* 
from random import*

## 함수 구현

#1. 숫자를 클릭했을 때
def clickNum1():
    ran1 = randrange(4)
    num1.configure(text = ran1, fg= "blue")

def clickNum2():
    ran2 = randrange(4)
    num2.configure(text = ran2, fg= "blue")

def clickNum3():
    ran3 = randrange(4)
    num3.configure(text = ran3, fg= "blue")

#2. 숫자가 같은지의 여부 판단
def equalNum(num1, num2, num3):
    if (num1 == num2 == num3):
        sentence.configure(text = ">> Success!!", fg= "red")
    else :
        sentence.configure(text = ">> Failure..", fg= "red")

#3. 리셋하기

def reset():
    num1.configure(text="0", fg = "black")
    num2.configure(text="0", fg = "black")
    num3.configure(text="0", fg = "black")
    sentence.configure(text=">> Success or failure is printed here.", fg = "black")

##레이아웃 구성

window = Tk()
window.title("Gambling game")
window.geometry("350x350")
window.resizable(width = FALSE, height = FALSE)
window.configure(bg="lemonchiffon")

#1. 설명 작성

title = Label(window, text="Gambling game", font = ("System", 30), bg="lemonchiffon")
label1 = Label(window, text="각 숫자를 클릭하면 1~3 사이의 난수로 바뀝니다.", font = ("NanumGothic", 10), bg="lemonchiffon")
label2 = Label(window, text="모두 같은 수가 나오면 승리입니다.", bg="lemonchiffon")
label3 = Label(window, text="숫자들을 차례대로 클릭해주세요.", bg="lemonchiffon")

title.pack(padx = 10, pady = 10)
label1.pack()
label2.pack()
label3.pack()

#2. 갬블링 구현

num1 = Button(window, text = "0", font = ("System", 30), bg="palegoldenrod", command = clickNum1, relief = "ridge")
num2 = Button(window, text = "0", font = ("System", 30), bg="palegoldenrod", command = clickNum2, relief = "ridge")
num3 = Button(window, text = "0", font = ("System", 30), bg="palegoldenrod", command = clickNum3, relief = "ridge")

num1.place(x = 100, y = 140 )
num2.place(x = 155, y = 140 )
num3.place(x = 210, y = 140 )

#3. 클릭 버튼 출력

clickButton = Button(window, text = "Click!", font = ("System", 14), relief = "ridge", bg="khaki",
command = lambda: equalNum(num1['text'], num2['text'], num3['text']))

clickButton.place(x = 130, y = 215)

#4. 실패, 성공 여부 출력

sentence = Label(window, width="30", text="Success or failure is printed here.", font = ("System", 20), bg="lemonchiffon", justify="center")

sentence.place(x = 25, y = 250)

#5. 리셋 버튼 출력
resetGame = Button(window, text = "Reset", font = ("System", 14), bg="khaki", command=reset, relief = "ridge")
resetGame.place(x = 180, y = 215)

window.mainloop()