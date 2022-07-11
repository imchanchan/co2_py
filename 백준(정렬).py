#백준 2750번

# //선택정렬 이용
N = int(input())
array = []

#입력받기
for i in range(N) :
    array.append(int(input()))

# 삽입정렬
for i in range(len(array)):
    
    min_index = i
    for j in range(i,len(array)):
        if(array[min_index] > array[j]):
            min_index = j
            
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 정리
# 1. 2개의 인덱스를 설정한다. 
# 2. j루프를 돌려 최솟값을 찾아준다.
# 3. i번째 값과 j루프를 돌려 찾은 최솟값을 바꿔준다. // 스와프

# //삽입정렬 이용

N = int(input())
array = []

#입력받기
for i in range(N) :
    array.append(int(input()))

for i in range(1, len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 -1씩 반복하는 문법
        if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] #스와프
            
        else:
            break #다 되었으면 if-else문 탈출
       
print("삽입정렬") 
print(array)

# 정리
# 1. range(i,0,-1)문법을 이용하여 하나씩 값을 줄여나가는 방법으로 설정해준다.
# 2. j값이 j-1보다 더 작으면 스와프를 해준다. 
# 3. j값을 하나씩 줄여나가며, 위치를 바꾸다 if문을 만족하지 않을 때 break한다.


# 백준2751

# //sorted함수 이용
N = int(input())
new = []

for i in range(N):
    new.append(int(input()))

new = sorted(new)

print(new)

# 백준10989 ( 수 정렬하기 3 )

# //계수정렬

N = int(input())

# 입력받기
for i in range(N) :
    array.append(int(input()))

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    

print("계수정렬")
for i in range(len(count)) :
    for j in range(count[i]): # j는 i의 값을 몇번 반복할지를 결정해준다
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        
# 정리
# 1. count는 리스트를 원소로 가진 리스트다. -> 리스트 안 리스트
# 2. count에 [0]*(배열의 포함되어있는 숫자들의 종류만큼 크기)
# 3. 각 해당 데이터 값 갯수세기 = for문으로 배열안의 값을 count의 인덱스로 해서 count원소의 값 증가시키기
# 4. for문 2번 필요 = count의 원소 값만큼 count원소의 index를 반환해줘야한다.


# 백준2108 (통계학)

N = int(input())
array = []

# 입력받기
for i in range(N) :
    array.append(int(input()))

# //산술평균
add = 0
for i in array :
    add = add + i
    
ari = add / len(array)
print('산술평균 값 :', round(ari))


# //중앙값
array.sort()

med_index = int((N+1)/2-1)
print('중앙값 :', array[med_index])


# //최빈값
# count 공간 만들어주기
count = [0] * (max(array)+1)

# array길이만큼 루프 돌려서 count값 증가시키기
# count의 인덱스가 출력해야하는 값이된다.
for i in range(len(array)-1) :
    count[array[i]] += 1
    
a = max(count)
print('최빈값 :', count.index(a)) #최빈값 출력


# //범위
ran = max(array) - min(array)
print('범위 :', ran)

# 백준1427 (소트인사이드)

N = int(input())

sot = N
buf = []

while( sot > 0):
    NA = sot % 10
    buf.append(NA)
    sot //= 10
    
print(buf)

buf.sort()

gap = 0
for i in range(len(buf)):
    gap += buf[i]*(10**i)
    
print(gap)


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



# 백준18870 (좌표압축)

# 좌표압축이란?
# {1,2,3,100,150}을 볼 때, 1~3까지는 한개씩 탐색을 하면 되지만,
# 100,150을 찾기 위해서는 3~150까지 탐색해야한다.
# 그러면 시간낭비가 너무 심해지게된다.
# 그래서 이 집합을 오름차순으로 정렬하고, 그 때의 인덱스를 그 값들에 할당해준다.
# 그 때 인덱스 값을 출력해주면 된다.
from multiprocessing.dummy import Array
from re import I
import sys

# 입력
N = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# set함수
array_set = set(array)

# set함수 출력값이 리스트가 아니여서, 정렬함수를 쓸수 없다.
# list로 바꿔주기
array_list = list(array_set)
array_list.sort()

# buf를 이용해서 인덱스 할 필요가 없어졌다.
'''
buf = []
for i in range(len(array_list)):
    buf.append(array_list.index(array_list[i]))
    
print(buf)
'''

# for문을 이용해서 리스트를 인덱스로 바로 연결
d = {}
for i in range(len(array_list)):
    d[array_list[i]] = i

for i in array :
    print(d[i], end=' ')
    




    
    
    
    
    
    
