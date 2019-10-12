import random
toss = random.randint(1, 2)
ask = input("Do you want to toss a coin? Tell me in Y/N:")
if ask == 'Y':
    if toss == 1:
        print('Heads!!')
    else:
        print('Tails!!')
else:
    exit()
