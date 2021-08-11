## 변수 선언
movie, time = [None]*2
couponList = [3000]

## 함수 선언
def twoLine():
    for i in range(0,36):
        print('=',end="")
    print()

def underLine():
    for i in range(0,36):
        print('_',end="")
    print()

def line():
    for i in range(0,15):
        print('-',end="")

## 할인 쿠폰 여부
if len(couponList) != 0:
    print("현재 " + str(couponList[0]) + "원 할인쿠폰이 있습니다.")
    print("할인쿠폰을 사용하시겠습니까?(yes/no)")
    reply = input(">>")

    if reply == 'yes':
        print("할인쿠폰을 사용하였습니다.") 
        couponList.remove(3000)
    elif reply == 'no':
        print("")
else:
    print("")
print("\n")

## 영수증 ##
twoLine()
line()
print("영수증", end='')
line()
print()

#영화, 상영관, 상영시간
print("  영화 : ", movie)
print("  상영관 좌석")
print("  상영 시간:", time)
underLine()

## 가격
print("  영화 티켓 가격\n")

print("  어른    10000")
print("  청소년   8000")
print("  어린이   5000")

