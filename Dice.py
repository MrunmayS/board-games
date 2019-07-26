import random
print('So you want roll a dice?\nAnswer in Y/N')
ans = input()
if ans == "Y":
    num = random.randint(1,6)
    print(num)
else:
    exit()
input()
