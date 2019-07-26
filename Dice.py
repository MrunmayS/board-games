import random
ans = input('So you want roll a dice?\nAnswer in Y/N:')
if ans == "Y":
    num = random.randint(1, 6)
    print(num)
else:
    exit()
input()
