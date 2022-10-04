# 백준 10989번 (수 정렬하기 3)
N = int(input())

data = list()

for _ in range(N):
    a = int(input())
    data.append(a)
    
data.sort()

for i in data:
    print(i)
    
    
# 백준 11050번 (이항 계수 1) = 조합 nCm
import sys
M = list(map(int, sys.stdin.readline().split()))

a = 1
for i in range(M[0],M[0]-M[1],-1):
    a = a*i

b = 1
for i in range(1,M[0]+1):
    b = b*(i+1)
    
print(int(a/b))


# 백준1181 (단어 정렬)
N = int(input())

word = []
for i in range(N) :
    word.append(input())
    
for i in range(len(word)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(word)):
        if len(word[min_index]) > len(word[j]) :
            min_index = j
        elif len(word[min_index]) == len(word[j]):
            if word[min_index] > word[j] :
                min_index = j
                
    word[i], word[min_index] = word[min_index], word[i] #스와프
    
print(word)


# 백준 1436번 (영화감독 숌)
N =  int(input())

name = 666
count = 0

while True:
    if '666' in str(name):
        count += 1
        
    if count == N:
        break
    
    name += 1
    
print(name)


N = int(input())

num = list(map(int, input().split()))
    
print(num)

count = 0
na = 0

for i in num :
    if i == 1:
        count += 0
        print("1")
        
    elif i == 2:
        count += 1
        print("2")
    
    
    elif i>2 :
        for j in range(2,i):
            if i%j == 0:
                na += 1
                print("another")     
                
        if na == 0:
            count += 1
            print("prime")
    
print(count)
    
    
# 백준 2751번 (수 정렬하기2 )

# //sorted함수 이용
N = int(input())
new = []

for i in range(N):
    new.append(int(input()))

new = sorted(new)

print(new)


# 백준 2869번 (달팽이는 올라가고 싶다)
A,B,V = map(int, input().split())

day = 0
count = 1

day += A
while (day < V):
    count += 1
    
    day -= B
    day += A
    
print(count)

# 백준7568 (덩치)
N=int(input())

array = []
for i in range(N):
    array.append(input().split())

length=len(array)

res=[]
for i in range(length):
    count=1
    for j in range(length):
        if array[i][0] < array[j][0] and array[i][1]<array[j][i]:
            count += 1
    res.append(count)

for i in res:
    print(i, end='')
    

# 백준10814 (나이순 정렬)
N = int(input())

array = []
for i in range(N) :
    [a,b] = input().split() 
    # split() = 띄어쓰기로 수를 입력받기
    array.append([a,b])

# map(자료형, 입력받는 수) = 입력받는 수를 원하는 자료형으로 바꾸기

for i in range(N) :
    array[i][0] = int(array[i][0])
    
print(array)
    
for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index][0] > array[j][0]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] #스와프
    
print('1', array)


# 백준11650 (좌표 정렬하기)

import sys
input = sys.stdin.readline

N = int(input())

#좌표 입력받기
array = []
for i in range(N) :
    [a,b] = map(int, input().split()) 
    # split() = 띄어쓰기로 수를 입력받기
    # map(자료형, 입력받는 수) = 입력받는 수를 원하는 자료형으로 바꾸기
    array.append([a,b])
    
array.sort()

for i in range(N) :
    print(array[i][0], array[i][1])
    

# 백준11651 (좌표 정렬하기 2)
import sys
input = sys.stdin.readline

N = int(input())

#좌표 입력받기
array = []
for i in range(N) :
    [a,b] = map(int, input().split()) 
    # split() = 띄어쓰기로 수를 입력받기
    # map(자료형, 입력받는 수) = 입력받는 수를 원하는 자료형으로 바꾸기
    array.append([b,a])
    
array.sort()

for i in range(N) :
    print(array[i][1], array[i][0])
    
