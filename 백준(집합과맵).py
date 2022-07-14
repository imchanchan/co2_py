# 백준10815 ( 숫자 카드 )
'''
실패한 입력 방법

Rcard=[]

for i in range(N):
    Rcard = int(input().split())

print(Rcard)

M= int(input())

Ccard=[]
for i in range(M):
    Ccard = int(input().split())
''' 
from selectors import EpollSelector
import sys

# 입력 ( 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때 )
n = int(input())
Rcard = list(map(int, sys.stdin.readline().split()))
m = int(input())
Ccard = list(map(int, sys.stdin.readline().split()))

result=[]

# 비교
for j in Ccard:
    for i in Rcard:
        if i == j :
            result.append(1)
            break
    result.append(0)

# 마지막에 쓸모없는 0이 자꾸 추가되어서
result.pop()
        
# 출력
for i in result :        
    print(i, end=' ')


# 이진탐색 이용한 풀이
n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for i in range(m) :
    if binary_search(card, check[i], 0, n-1) is not None:
        print(1, end=' ')
    else :
        print(0, end=' ')
        
        
# 백준14425번 (문자열 집합)

# 입력
N, M = map(int, sys.stdin.readline().split())

# 틀린 이유 : 배열을 선언하고, 루프를 돌리면 
# M_word[1]에는 한글자만 입력받을 수 있다.
'''
M_word = []
for j in range(M):
    M_word[i] = sys.stdin.readline()
'''    

# 배열 안에서 입력 받아서 넣어주기
N_word = [input() for _ in range(N)]
M_word = [input() for _ in range(M)]

# 비교
count = 0
for i in N_word:
    for j in M_word:
        if i==j :
            count += 1
            
print(count)


# 백준1620번 ( 나는야 포켓몬 마스터 이다솜 ) // 문제이해를 못했습니다,,ㅜㅜ
N, M = map(int, sys.stdin.readline().split())


# 백준10816번 ( 숫자 카드 2 )
n = int(input())
Sang = list(map(int, sys.stdin.readline().split()))
m = int(input())
Rcard = list(map(int, sys.stdin.readline().split()))

count = [0 for _ in range(len(Rcard))]
for i in range(len(Rcard)):
    for j in Sang:
        if j == Rcard[i] :
            count[i] += 1
        
    print(count[i], end=' ')
    

# 백준1764번 ( 듣보잡 )

# 입력
N, M = map(int, sys.stdin.readline().split())
Listen = [input() for _ in range(N)]
See = [input() for _ in range(M)]

Listen.sort()
See.sort()

# 비교
count = 0
result = []
for i in Listen:
    for j in See:
        if i == j :
            count += 1
            result.append(i)
            
print(count)
for i in result :
    print(i)
    

# 백준1269번 (대칭차집합)
N, M = map(int, sys.stdin.readline().split())

A = set(list(map(int, sys.stdin.readline().split())))
B = set(list(map(int, sys.stdin.readline().split())))

a = list(A-B)
b = list(B-A)

a.sort()
b.sort()

sum_a = len(a)
sum_b = len(b)

print(sum_a + sum_b)
            

# 백준11478번 (서로 다른 부분 문자열의 개수)
N = input()

result = []

see = []
for i in range(len(N)):
    see.append(i)
    for j in range(i, len(N)):
        buf=N[i:j+1]
        result.append(buf)
        
re_set = set(result)

print(len(re_set))

# N에 문자열을 넣어준다.
