'''백준 11659번 (구간 합 구하기4)'''
#시간초과

import sys
N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

arr.insert(0,0)
   
# M개 갯수만큼 넣어주기
plus=0
for i in range(M):
    a, b = map(int, input().split())
    
    for j in range(a,b+1):
        plus += arr[j]
    
    print(plus)
    plus = 0


'''백준 2559번 (수열)'''
#시간초과

import sys
N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

buf=[]
result = []
for i in range(0,N+1-M):
    for j in range(i,M+i):
        buf.append(arr[j])
    
    result.append(sum(buf))
    buf = []

print(max(result))


'''백준 16139번 (인간-컴퓨터 상호작용)'''

'''백준 10986번 (나머지 합)'''
# 

import sys
N, M = map(int,sys.stdin.readline().split())


tem = list(map(int,sys.stdin.readline().split()))

namogi = [0 for _ in range(M)]

result = 0


for k in range(0,N):
    for i in range(k,N):
        result += tem[i]
    
        print(result)
        namogi[result%M] +=1
        
    result = 0

print(namogi[0])

# 풀이과정 : 노트참고

# 인터넷풀이 (아직 이해못함)
import sys
total, tar = map(int,sys.stdin.readline().split())
tem = list(map(int,sys.stdin.readline().split()))

prepix = [0 for i in range(tar)]
presum = 0

prepix[0] = 1

for i in range(total):
    presum+=tem[i]
    # prepix.append(presum%tar)

    print(presum)
    
    prepix[presum%tar] += 1

print(prepix)

# print(prepix)
'''
#나머지가 같은 두 부분합을 고르면 두 구간은 결국 tar의 배수가 된다.
#나머지가 0인 경우는 부분합 자체가 tar의 배수인 경우이므로 두 구간이 아니라 본인 구간도 될 수 있기 때문에
#index가 0인 (부분합 0) 것을 포함
'''
ans=0
for i in prepix:
    ans += i*(i-1)//2

print(ans)


'''백준 11660번 (구간 합 구하기 5)'''

import sys
from webbrowser import MacOSX

N,M = map(int, sys.stdin.readline().split())

# NxN배열 입력받기
Matrix = [[0 for i in range(N+1)] for i in range(N+1)]
arr = [0 for i in range(N+1)]

# 2차원 배열 입력받는 과정 숙지하기.

for i in range(1,N+1):
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    print(arr)
    
    for j in range(1,N+1):
        
         Matrix[i][j] = arr[j]


# M개 줄로 순서쌍 입력받기

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(x1, y1, x2, y2)
    sum = 0
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            sum = sum + Matrix[i][j]

    print(sum)
    
