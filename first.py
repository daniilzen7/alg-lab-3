import random

n = random.randint(10, 100)

m, s = [], []

for i in range(4):
    m.append(random.randint(0, 15)) # количество монет
    s.append(random.randint(1, 15)) # номинал

s.sort()
s.reverse()
answer = [0, 0, 0, 0] # сколько монет использовалось (s1, s2, s3, s4 соотв)
print('необходимо выдать сдачу: ', n)

def greedy(n, m, s, key):
    global answer
    ans = 0
    while n >= s and m > ans:
        n -= s
        ans += 1
    answer[3 - key] = ans
    return n

for i in range(4):
    n = greedy(n, m[i], s[i], i)
    if n == 0:
        break

if n != 0:
    print('сдачу не удалось набрать полностью, осталось: ', n)

print('монеты и количество монет: ', s, m)
print('выдача от самой маленькой монеты, до самой большой: ', answer)