# 2839번 (설탕배달)
N = int(input())

count = 0

while(N<5):
    count += 1
    N /= 5
    
if (N/3 == 0):
    while(N<3):
        count+=1
        N /=3
        result = count
else :
    result = -1

print(result)
print(count)

sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
    
# 2869번 (달팽이는 올라가고 싶다)

import sys
import math

A,B,V = map(int,sys.stdin.readline().split())

V = V-A # 정상에 올라갔을 때
result = (V/(A-B))+1
printf(math.ceil(result)) # 날짜는 올림처리를 해주어야 한다.

# 4153번 (직각삼각형)
while True:
        N = list(map(int, input().split()))
        max_num = max(N)
        
        if sum(N) == 0:
                break
            
        N.remove(max_num)
        
        if N[0] ** 2 + N[1] ** 2 == max_num ** 2:
                print('right')
                
        else:
                print('wrong')
                
# 4949번 (균형잡힌 세상)

# 7568번 (덩치)
N = int(input())
List = []

for _ int range(N):
    x,y=map(int, input().split())
    List.append((x,y))
    
for i in List:
    rank = 1
    for j in List:
        if i[0]<j[0] and i[1]<j[1]:
            rank += 1
    print(rank, end = '')
    
# 9012번 (괄호)
N = int(input())
for _ in range(N):
    list = []
    s = input()
    
    for ch in s:
        if ch == '(':
            list.append('(')
        if ch == ')':
            if list:
                list.pop()
            elif not list:
                VPS = False
                break
    if not list and VPS:
        printf("YES")
    elif list or not VPS:
        printf("NO")
        
    
    