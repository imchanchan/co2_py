'''백준 11047번 (동전0)'''
N, K = map(int, input().split())
result = 0
coin = []
for i in range(N):
    C = int(input())
    coin.append(C)
    
coins = sorted(coin, reverse=True)

for i in coins:
    if i > K:
        continue
    else:
        while i <= K:
            K -= i
            result += 1

print(result)


'''백준 1931번 (회의실 배정)'''

import sys

N = int(sys.stdin.readline())
buf = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    buf.append((s, e))
    
buf.sort(key=lambda x: (x[0], x[1]))

total = 0
last_start = 0
last_end = 0

for start, end in buf:
    
    if last_end<=start:
        total+=1
        last_start, last_end = start, end
    elif last_end>end :
        last_start, last_end = start, end


'''백준 11399번 (ATM)'''
import sys

N = int(input())
buf = list(map(int, sys.stdin.readline().split()))

buf.sort()
sum = 0

for i in buf:
    sum += i * N
    N -= 1
    
print(sum)


'''백준 1541번 (잃어버린 괄호)'''
