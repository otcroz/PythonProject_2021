from tkinter import*
from tkinter import ttk

####기본 설정####
window = Tk()
window.title("단위계산기")
window.geometry("400x300")
window.resizable(width=FALSE,height=FALSE)

####변수 선언####

unitList = [['밀리미터(mm)','cm', 10],['밀리미터(mm)','m', 10*2],['밀리미터(mm)','km', 10*6],['밀리미터(mm)','in',]

]


####함수 정의####
def conversion():
    inputValue = inputBox.get()
    unit1 = text1.get() #선택된 콤보박스 값을 가져온다
    unit2 = text2.get()

    if unit1 == unit2:
        res = inputValue

    else:
        res = inputValue*b

    return res



####입력창, 결과창 구현####

label1 = Label(window, text="단위계산기", font=("System", 20))
label1.pack(padx = 10, pady=10)

#1. 콤보박스 구현
text1 = StringVar() #문자열형 타입 변수 선언
text2 = StringVar()
combo1 = ttk.Combobox(window, textvariable = text1, width = 11) #콤보 박스 선언
combo1['value'] = ['밀리미터(mm)','센티미터(cm)','미터(m)','킬로미터(km)','인치(in)','피트(ft)'] #콤보 박스 요소 삽입
combo1.current(0)

combo2 = ttk.Combobox(window, textvariable = text2, width = 11)
combo2['value'] = ['밀리미터(mm)','센티미터(cm)','미터(m)','킬로미터(km)','인치(in)','피트(ft)'] #콤보 박스 요소 삽입
combo2.current(0)

combo1.place(x=50 ,y=100)
combo2.place(x=250 ,y=100)

#2. 입력, 결과창 구현

inputBox = Entry(window, font=("System", 10))
inputBox.insert(0,"")
inputBox.place(x=50, y=150, width = 100, height = 25)

outputBox = Entry(window, font=("System", 10))
outputBox.insert(0,"")
outputBox.place(x=250, y=150, width = 100, height = 25)


#3. 변환 버튼 구현

converButton = Button(window, text = "변환", font=("System", 10), command = conversion)

converButton.place(x=180, y=150)



window.mainloop()