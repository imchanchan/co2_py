'''백준 2630번 (색종이 만들기)'''
import sys

N = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

blue = 0
white = 0

# 재귀함수, 종료부분이 어디인지 모르겠습니다.
def cutting(x,y,N):
    global white, blue
    
    check_color = table[x][y]
    for i in range(x, x+N) :
        for j in range(y,y+N) :
            if check_color != table[i][j]:
                cutting(x,y,N//2)
                cutting(x,y+N//2,N//2)
                cutting(x+N//2,y,N//2)
                cutting(x+N//2,y+N//2,N//2)
                return
                # 이부분에서 return이 쓰이는게 이해가 가지않습니다.
            
    if check_color == 0 :
        white += 1
    else :
        blue += 1
        
cutting(0,0,N)
print(white)
print(blue)



'''백준 1992번 (쿼드트리)'''
import sys

N = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

# 재귀함수, 종료부분이 어디인지 모르겠습니다.
def cutting(x,y,N):
    global white, black
    check_color = table[x][y]
    for i in range(x, x+N) :
        for j in range(y,y+N) :
            if check_color != table[i][j]:
                # 분할시작 = ()를 출력해주는 것으로 생각
                print("(", end="")
                cutting(x,y,N//2)
                cutting(x,y+N//2,N//2)
                cutting(x+N//2,y,N//2)
                cutting(x+N//2,y+N//2,N//2)
                print(")", end="")
                return                 
                    
                # 이부분에서 return이 쓰이는게 이해가 가지않습니다.
            
    if check_color == 0 :
        print(0, end="")
    else :
        print(1, end="")
        
cutting(0,0,N)



'''백준 1780번 (종이의 개수)'''
import sys

N = int(sys.stdin.readline())

table = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
minus=0 
zero=0 
plus=0

def T_cutting(x,y,N):
    global minus, zero, plus
    check = table[x][y]
    
    for i in range(x, x+N):
        for j in range(y,y+N):
            if check != table[i][j]:
                T_cutting(x,y,N//3)                   #(0,0)
                T_cutting(x,y+N//3,N//3)              #(0,3)
                T_cutting(x,y+(N//3)*2,N//3)          #(0,6)
                
                T_cutting(x+N//3,y,N//3)              #(3,0)
                T_cutting(x+N//3,y+N//3,N//3)         #(3,3)
                T_cutting(x+N//3,y+(N//3)*2,N//3)     #(3,6)

                T_cutting(x+(N//3)*2,y,N//3)          #(6,0)
                T_cutting(x+(N//3)*2,y+N//3,N//3)     #(6,3)
                T_cutting(x+(N//3)*2,y+(N//3)*2,N//3) #(6,6)
                return
            
    if check == -1 :
        minus += 1
    elif check == 0 :
        zero += 1
    else :
        plus += 1

T_cutting(0,0,N)
print(minus)
print(zero)
print(plus)



'''백준 1629번 (곱셈)'''
import sys

A, B, C = map(int, input().split())

# 풀이과정
# 나머지 분배법칙 : (A*B)%C = (A%C)*(B%C)%C

def multi(x,y):
    global C
    
    # 종결조건
    if (y==1):
        return x%C
    
    else:
        if y%2 ==0:
            return (multi(x,y//2)*multi(x,y//2))%C
        else :
            return (multi(x,y//2)*multi(x,y//2)*x)%C
        
print(multi(A,B))



'''백준 11401번 (이항 계수3)'''
import sys
N,K = map(int, input().split())
p = 1000000007

# 팩토리얼 (다음숫자를 곱해줄 때마다 %p를 계산해준다.)
def factorial(N):
    n=1
    for i in range(2,N+1):
        n=(n*i)%p
    return n

# 거듭제곱 계산 (나머지 연산 적용)
def multi(x,y):
    
    # 종결조건
    if y== 0 :
        return 1
    elif y==1 :
        return x
    
    else:
        if y%2 ==0:
            return (multi(x,y//2)*multi(x,y//2))%p
        else :
            return (multi(x,y//2)*multi(x,y//2)*x)%p
        
# top=N!, bottom=((N-K)!K!)^(p-2)%p
top = factorial(N)
bottom = factorial(N-K)*factorial(K)%p

# 페르마 소정리에 의하여
#  N!/((N-K)!K!)^(-1)%p = N!/((N-K)!K!)^(p-2)%p
# -1승을 p-2승으로 바꿀 수 있었다.
print(top*multi(bottom, p-2)%p)


'''백준 10830번 (행렬제곱)'''

# 인터넷 풀이 참고, 완전 이해

import sys
a,b = map(int, input().split())
matrix = [list(map(lambda x: x % 1000, map(int, input().split()))) for _ in range(a)]

def power(m, y):
    if y == 1:
        return m
    partial = power(m, y // 2)
    partial_square = multiply_matrix(partial, partial)
    if y % 2 == 0:
        return partial_square
    elif y % 2 == 1:
        return multiply_matrix(partial_square, m)


def multiply_matrix(matrix_1, matrix_2):
    length = len(matrix_1)
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            result[i][j] = sum([(matrix_1[i][k] * matrix_2[k][j])%1000 for k in range(length)])%1000
    return result

answer = power(matrix, b)
for i in range(a):
    print(' '.join(map(str, answer[i])))


'''백준 11444번 (피보나치 수6)'''
# 위 행렬의 곱셈 함수 이용


        
