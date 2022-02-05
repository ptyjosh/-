import random
x = random.randint(1,50)

while True:
    num = int(input("1에서 50사이로 입력하세요:"))
    if x == num:
        print("정답")
        break
    elif x > num:
        print("down")
    else:
        print("up")