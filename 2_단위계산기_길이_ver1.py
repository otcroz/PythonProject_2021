from tkinter import*
from tkinter import ttk

####기본 설정####
window = Tk()
window.title("단위계산기")
window.geometry("300x200")
window.resizable(width=FALSE, height=FALSE)


####변수 선언####
unitList_length = {'밀리미터(mm)': 'mm', '센티미터(cm)': 'cm',
                   '미터(m)': 'm', '킬로미터(km)': 'km'}


####함수 정의####


def conversion():
    inputValue = float(inputBox.get())
    unitStr = lengUnit.get()

    unitKey = unitList_length.get(unitStr)  # 단위 값 얻기

    #단위를 mm 기준으로 맞춰줌
    mm, cm, m, km = [inputValue]*4

    if unitKey == 'mm':
        mm = mm
        cm = cm / 10
        m = m / 1000
        km = km / 1000000

    elif unitKey == 'cm':
        mm = mm*10
        cm = cm
        m = m/100
        km = km / 100000

    elif unitKey == 'm':
        mm = mm*1000
        cm = cm*100
        m = m
        km = km / 1000

    elif unitKey == 'km':
        mm = mm*1000000
        cm = cm*100000
        m = m*1000
        km = km

    outputBox1.configure(text= " mm: " + str(mm) + " 밀리미터(mm)")
    outputBox2.configure(text= " cm: " + str(cm) + " 센티미터(cm)")
    outputBox3.configure(text= " m: " + str(m) + " 미터(m)")
    outputBox4.configure(text= " km: " + str(km) + " 킬로미터(km)")


####입력창, 결과창 구현####
#1. 라벨
label1 = Label(window, text="측정 범주")
label2 = Label(window, text="원래 값")
label3 = Label(window, text="원래 단위")

#2. 콤보박스
group = StringVar()  # 문자열형 타입 변수 선언
lengUnit = StringVar()
category = ttk.Combobox(window, textvariable=group, width=11)  # 콤보 박스 선언
category['value'] = ['길이 / 거리']  # 콤보 박스 요소 삽입
category.current(0)

combo2 = ttk.Combobox(window, textvariable=lengUnit, width=11)
combo2['value'] = ['밀리미터(mm)', '센티미터(cm)', '미터(m)', '킬로미터(km)']  # 콤보 박스 요소 삽입
combo2.current(0)

#3. 입력, 결과창

inputBox = Entry(window, font=("System", 10))
inputBox.insert(0, "")
inputBox.place(x=150, y=150, width=100, height=25)

outputBox1 = Label(window, text=" ", width=39, bg="darkgrey")
outputBox2 = Label(window, text=" ", width=39, bg="darkgrey")
outputBox3 = Label(window, text=" ", width=39, bg="darkgrey")
outputBox4 = Label(window, text=" ", width=39, bg="darkgrey")

#4. 변환 버튼

converButton = Button(window, text="변환", command=conversion)

#라벨, 버튼, 박스 구하기

label1.grid(row=0, column=0, padx=5, pady=5)
category.grid(row=0, column=1, padx=5, pady=5)

label2.grid(row=1, column=0, padx=5, pady=5)
inputBox.grid(row=1, column=1, padx=5, pady=5)
converButton.grid(row=1, column=2, padx=5, pady=5)

label3.grid(row=2, column=0, padx=5, pady=5)
combo2.grid(row=2, column=1, padx=5, pady=5)

outputBox1.place(x=10, y=100)
outputBox2.place(x=10, y=120)
outputBox3.place(x=10, y=140)
outputBox4.place(x=10, y=160)

window.mainloop()
