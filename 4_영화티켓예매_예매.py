##변수 선언
dayList = ['Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat', 'Sun']
movieList = ['Harry Potter', 'Gravity Fall', 'Iron Man', 'The Avengers']
ScreenTimeList = ['13:00', '15:00', '17:00', '19:00']
theaterNum = 1

## 예매 날짜 선택

print("\n예매 날짜를 선택해주세요.")

for d in dayList:
    print(d, end=' ')
print()

while True:
    day = input(">>")

    if day in dayList:
        break
    else:
        print("요일을 다시 선택해주십시오.")

## 영화 선택
print("\n" + day + "에 상영되는 영화입니다.")
print("영화를 선택해주십시오.\n")
for m in movieList:
    print(m)

while True:
    movie = input(">>")

    if movie in movieList:
        break
    else:
        print("영화를 다시 선택해주십시오.")

##상영 시간 선택
print("\n" + day + " " + movie +" 상영시간표 입니다. 상영시간을 선택해주십시오.\n")
for t in ScreenTimeList:
    print( t +"___제" + str(theaterNum) + "상영관_[?/80]") # 남은 자리 수 연결?
    theaterNum+=1
    
while True:
    time = input(">>")

    if time in ScreenTimeList:
        break
    else:
        print("상영시간을 다시 선택해주십시오.")