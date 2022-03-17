a = int(input())
b = int(input())
c = int(input())
if (a+b+c) % 3 == 0:
    print("Делится на три")
elif (a+b+c) % 9 == 0:
    print("Делится на девять")
else:
    print("Не делится")