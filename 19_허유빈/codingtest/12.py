print("구구단 프로그램을 실행합니다.\n 1. 홀수 구구단\n 2. 짝수 구구단\n 3. 종료")

while True :
    num = int(input("숫자를 입력하세요: "))
    if (num==1):
        for i in range(3, 10, 2):
            print(i, "단")
            for j in range (1, 10):
                print("%d * %d = %d" % (i, j, i*j))
    elif (num == 2):
        for i in range(2, 9, 2):
            print(i, "단")
            for j in range (1, 10):
                print("%d * %d = %d" % (i, j, i*j))
    elif (num == 3):
        break
    else :
        print("잘못 입력 하셨습니다. 1~3번 숫자를 입력하세요.")



def gugudan1(num):
    for i in range(3, 10, 2):
        print(i, "단")
        for j in range (1, 10):
            print("%d * %d = %d" % (i, j, i*j))
    return

def gugudan2(num):
    for i in range(2, 9, 2):
        print(i, "단")
        for j in range (1, 10):
            print("%d * %d = %d" % (i, j, i*j))
    return