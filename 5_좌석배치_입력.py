from tkinter import* 
from random import*
from tkinter import messagebox

###변수 선언
seatList = [None]*25
num = 0
click = 0

###함수 선언
def randomSeat(): #랜덤으로 이름을 넣는 함수
    name = inputName.get()
    global click
    while(True):
        ran = randrange(0,25)
        if name == "":
            messagebox.showinfo("오류","이름을 입력해주세요.")
            break

        if click<25:
            if seatList[ran]['text'] =="":
                seatList[ran].configure(text=name)
                click+=1
                break
        else:  
            messagebox.showinfo("오류","자리가 없습니다.")
            break
            
### 좌석 배치 화면
#기본 설정
window = Tk()
window.title("Gambling game")
window.geometry("480x450")
window.resizable(width = FALSE, height = FALSE)

#좌석 배치
title = Label(window, text="좌석 배치", width=10)
title.grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5)

#칠판
board = Label(window, text="칠판", bg="lightgrey", width=10)
board.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)

#좌석 배치 구성
for i in range(0,25):
    seatList[i] = Label(window, text="", bg="white", width=10)

for i in range(2,7):
    for k in range(0,5):
        seatList[num].grid(row=i, column=k, padx=5, pady=5, ipadx=5, ipady=5)
        num+=1

#입력창 구현
inputName = Entry(window)
inputName.place(x=165, y= 310)

#랜덤 버튼 
randomButton = Button(window, text="랜덤 배치", command=randomSeat)
randomButton.place(x= 205, y= 340)

#시스템네임
SystemName = Label(window, text="Seating system, 2021", font=("System", 3))
SystemName.place(x= 163, y= 420)

window.mainloop()