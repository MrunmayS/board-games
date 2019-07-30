import random
ans = int(input('So you want roll a dice?\nHow many dice/s you want to throw?:'))
for _ in range(1, ans + 1):
    num = random.randint(1, 6)
    print(num)
input()
