import random

from random import randint

amount_coin = int(input('введите количество монет: '))

m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'все монеты {coins}')
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f'всего монет {m, k}')

if m > k:
    L = k
else:
    L = m

print(f"минимальное количество монет, которые нужно перевернуть {L}")