'''백준 1904번 (01타일)'''

global count1 
count1 = 0

def fib(n):    
    if n==1 or n==2:
        count1 += 1
        return 1
    else:
        count1 += 1
        return fib(n-1)+fib(n-2)
    
    
global count2
count2 = 0

def fibonacci(n):
    
    # 결과를 저장하기 위한 DP 테입블 초기화
    d = [0]*(n+1)

    # 첫 번쩨 피보나치 수와 두 번째 피보나치 수는 1
    d[1] = 1
    d[2] = 1

    # 피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
        count2 += 1
    
    return d[i]
    

n = int(input())
print(fib(n), fibonacci(n))
print(count1, count2)



'''백준 9184번 (신나는 함수 실행)'''

# // 제가 풀이한 부분입니다.
def w(a,b,c):

    # 종료조건
    if (a <=0 or b<=0 or c<=0 ):
        return 1
    if (a>20 or b>20 or c>20) :
        return w(20,20,20)
    
    # 이미 계산한적 있는 문제
    if dp[a][b][c]:
        return dp[a][b][c]
    
    # 아직 계산하지 않은 문제라면 점화식
    if (a<b<c):
        dp[a][b][c] = w(a,b,c-1) + w(a,b,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    
    else : 
        dp[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return(dp[a][b][c])

dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

while(True):
    a,b,c = map(int, input().split())

    if(a==-1 and b==-1 and c==-1):
       break
    
    print("w(",a,",",b,",",c,") =",w(a,b,c))


# // 다른 사람 문제 풀이 참고해서 완전히 이해했습니다!
import sys
input = sys.stdin.readline

def w(a, b, c):
    # 종료조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # dp에 저장되어있다면 그대로 반환
    if dp[a][b][c] :
        return dp[a][b][c]

    # 아직 계산하지 않은 문제라면 점화식 주어진것 사용
    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    # 더이상 함수를 재귀하지 않고, 종료조건까지 완료한다면!
    return dp[a][b][c]



dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))



'''백준 1904번 (01타일)'''

# // 제가 풀이 했지만, 틀렸습니다.

# 팩토리얼 함수
def fac(n) :
    if n == 1 :
        return 1
    
    if dp[n]:
        print("yo")
        return dp[n]
    
    else :
        dp[n] = n*fac(n-1)
        return dp[n]

# 동적계획법 dp크기 만들기
dp = [0 for _ in range(21)]

# 입력
N = int(input())

# 루프 돌릴 숫자 범위 정하기
k = N//2
print(k)

# k+1만큼 상황에 따라 값을 저장할 배열 선언
buf=[]

# 같은 수가 있는 조합식을 이용해서 해결하려고 했지만, 실패
for i in range(k+1):
    buf[i] = fac(6-i) / (fac(6-2*i) * fac(i))

print("buf")
print(buf)

sum_list = sum(buf)
print("sum_list")
print(sum_list)

# 예시
# N=6이라면, k=6//2=3이된다
# 00이 0개 일때, 00이 1개 일때, 00이 2개 일때, 00이 3개 일때로 구분할 수 있다
# 즉, k+1개 만큼의 상황으로 나눌 수 있다.

# -------------------------------------------

# // 인터넷 문제 풀이를 참고하여, 문제의 규칙성을 찾았습니다.
# // 첫번째, 두번째만 주어지면 뒤부터는 앞의 값 + 앞앞의 값이란 점화식을 파악했습니다.
dp = [0]*1000001

def tile(n):
    # 종료 조건
    dp[1] = 1
    dp[2] = 2
    
    # for문을 이용한 점화식
    for i in range(3, n+1):
        dp[i]=(dp[i-1]+dp[i-2])%15746
        
    return dp[n]

N = int(input())
print(tile(N))



'''백준 9461번 (파도반 수열)'''
dp = [0]*101

def padoban(n):
    # 종료 조건
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    # for문을 이용한 점화삭
    for i in range(4, n+1):
        dp[i]=dp[i-3]+dp[i-2]
        
    return dp[n]

N = int(input())
for i in range(N):
    Q = int(input())
    print(padoban(Q))

# // 질문이요!
# 탑다운(하향식), 보텀업(상향식) 어떤 상황에서 쓰이는지 구분을 잘 못하겠습니다,,ㅠㅠ
# 이 문제를 두가지로 다 했는데  아래에 코드는 실행이 안됩니다,,ㅜㅜ(탑다운)
d = [0]*101

def pado(x):
    if x==1 and x==2 and x==3 :
        return 1
    
    if d[x]:
        return d[x]
    
    d[x] = pado(x-3) + pado(x-2)
    return d[x]

N = int(input())
for i in range(N):
    Q = int(input())
    print(pado(Q))


'''백준 1912번 (연속합)'''

# // 최찬 틀림
# 입력
import sys
N = int(input())

buf = list(map(int, sys.stdin.readline().split()))

dp =[0]*(len(buf))

# 초깃값 (종료조건)
dp[0] = buf[0]

# 점화식
for i in range(1, len(buf)):
    dp[i] = dp[i-1] + buf[i]

print(dp)
print(max(dp))

# // 정답 이해하는 시간 필요
n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])


print(max(dp))


'''백준 1149번 (RGB거리)'''
import sys

# 입력
N = int(input())

dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

# dp[0][0],dp[0][1],dp[0][2] 
# 빨 초 파 초기조건은 입력부분에서 해결

# 전단계의 색깔이 다른 최솟값을 바로바로 숫자에 더해서 생각을 해준다.
for i in range(1, len(dp)):
    # 빨간색 
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+dp[i][0]
    # 초록색
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+dp[i][1]
    # 파란색
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+dp[i][2]
    
# [[26, 40, 83], [89, 86, 83], [96, 172, 185]] 3을 비교해서 생각해보면
# 마지막 dp[len(dp)] 부분에서 가장 작은 값이 최솟값이 된다.
print (min(dp[len(dp)-1]))



'''백준 1932번 (정수 삼각형) => 출력초과'''
# 입력 
N = int(input())

dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

print(dp)

for i in range(1,N):
    for j in range(0, i+1):
        if (j==0) :
            dp[i][0] = dp[i-1][0]+dp[i][0]
        if (j==i) :
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        
        if (0<j<i):
           dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]


print(max(dp[N-1]))


'''백준 2579번 (계단 오르기)'''
# // 런타임에러 (질문)
N = int(input())

#s=[]
#for i in range(N):
#    s.append(int(input()))

s =[0 for i in range(N)]
for i in range(N):
    s[i] = int(input())
    
dp=[0 for _ in range(N+1)]

dp[0] = s[0]

# // max( 1. 마지막이 1칸으로 끝날 경우, 2. 마지막이 2칸으로 끝날 경우 )
dp[1] = s[0] + s[1] 
# max(s[0]+s[1], s[1]) = 당연히 s[0]+s[1]이기 때문
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

print(dp[N-1])


# // (아래 인터넷 코드와 차이점을 발견하지 못했는데 에러가 났어요,,ㅜㅜ)
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])


'''백준 1463번 (1로 만들기)'''
# 입력
N = int(input())

# dp 공간 만들어주기 (1-N까지 쓰기 때문)
# dp란, N이 1이 될 때까지 최소한으로 연산을 사용한 횟수를 말한다.
dp = [0]*(N+1)

# 생각해보기!

for i in range(2,N+1):
    # dp[N]을 계산할 때,
    # 1. N에서 1을 뺀 후(+1), dp[N-1]을 더해준다.
    dp[i] = dp[i-1]+1


    # N이 2로 나뉠 때!
    # 2. N에서 2을 나눈 후(+1), dp[N//2]값을 더한다.
    # 3. 1,2방법을 비교해 최소값을 저장해준다.
    if (i%2==0):
        dp[i] = min(dp[i], dp[i//2]+1)

    # N이 3으로 나뉠 때!
    # 2. N에서 3을 나눈 후(+1), dp[N//3]값을 더한다.
    # 3. 1,2방법을 비교해 최소값을 저장해준다.
    if (i%3==0):
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])


'''백준 10844번 (쉬운 계단 수)'''


'''백준 2156번 (포도주 시식)'''
# // 계단오르기와 비슷하다고 생각이 들어, 그 문제의 원리로 풀었다.
# // 제가 발견한 차이점은 계단오르기 부분은 마지막 s값을 꼭 지나쳐야만 한다는 것이고,
# // 이 문제는 마지막 Z값을 꼭 밟지 않아도 된다는 것이다.
# // 그 부분을 참고하면, Z[N-1]이 Z[N]보다 클 수 있겠다는 생각이 들었다.
# // dp로 나온 결과의 최대값을 구하면 되겠다고 생각하여 max(dp)를 추가했다.

N = int(input())

# 잔 입력
Z=[]
for i in range(N):
    Z.append(int(input()))

dp = [0]*N
dp[0] = Z[0]
dp[1] = Z[0]+Z[1]

# max(두칸으로 끝나는것, 한칸으로 끝나는 것)

dp[2] = max(Z[0]+Z[2], Z[1]+Z[2])

for i in range(3,N):
    dp[i] = max(dp[i-1],dp[i-3]+Z[i-1]+Z[i], dp[i-2]+Z[i])

print(dp[N-1])

#----------------------수정하면서, 필요없는 부분이 되었다,,
# 이부분을 짧게 수정해서 max함수로 이용했다.
#if (dp[N-2] > dp[N-1]):
#    print(dp[N-2])
    
#else :
#    print(dp[N-1])
# -    -     -    -     -    -
#print(max(dp))    
#-------------------------

#하지만 결과는 틀렸습니다--------(틀린 부분 수정 완료!)


# // 인터넷 코드와 비교 (오답풀이)
# => 풀이과정에서 틀린 이유!!
# 마지막 단계만 비교해주는게 아니라,
# 각 단계별 결과도 비교해줘야 한다.
'''
    (찬) max(dp[i-3]+Z[i-1]+Z[i], dp[i-2]+Z[i])
(인터넷) max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i])
'''
# dp[i-1]은 Z[i]를 지나지 않는 경우를 말한다.

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])


'''백준 11053 (가장 긴 증가하는 부분 수열)'''
# // 처음에 짠 코드 (틀렸습니다.)
N = int(input())

# 수열 입력 w[추가,추가,추가,...]
w = list(map(int, input().split()))

# 저장공간 1로 모두 초기화
dp = [1]*(N)

# 비교
i=0
j=1
while(j<N):
    if w[i]<w[j]:
        dp[j] = max(dp) + 1
        i = j
    j+=1
    
print(dp)

# 오답풀이-----------------------
# 제일 큰 수가 앞으로 나오면, 뒷부분은 비교할 때,
# 당연히 작다는 결과밖에 나오지 않아서 if문에 들어가지 않게된다.
# 결론 : 12111111111...과 같은 결과가 나온다.

# 한번에 인터넷 풀이와 내 풀이의 차이점을 알 수 있는 예시
# : 10
# : 1 5 2 1 4 3 4 5 2 1 
# 내 코드와 인터넷 코드에 넣어보면 틀린 점을 찾을 수 있다.
#---------------------------------

# // 인터넷 참고 (수정)
import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
dp = [1] * N

# (틀렸던 부분!)
# i를 기준으로 j가 0-i-1번째를 쭉 훑고,
# A[i]값이 제일 커질때마다, dp[j]값을 한개씩 증가시켜준다
# 그 다음 dp[j]+1 값과 dp[i]값 중 더 큰 값을 dp[i]에 넣어준다.
for i in range(1, N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


'''백준 11054번 (가장 긴 바이토닉 부분 수열)'''

# 아이디어
# 1. "가장 긴 증가하는 부분 수열"방법으로,
#    U리스트로 한번 생각하고, 뒤집어서 한번 생각해준다.
# 2. 그 다음 엇갈려서 값을 더해준다. (result)
# 3. result값 중 제일 큰 값이 답이 된다.

# // 처음에 짠 코드 (틀렸습니다.)
import sys
from urllib.parse import _ResultMixinBytes

N = int(sys.stdin.readline())
U = list(map(int, input().split()))
up = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if U[i] > U[j] :
            up[i] = max(up[i], up[j]+1)

#print(up)

D = []
for i in reversed(U):
    D.append(i)

down = [1]*N
for i in range(1, N) :
    for j in range(i) :
        if D[i] > D[j] :
            down[i] = max(down[i], down[j]+1)
            
#print(down)

#수정 전 (막대기 2개)
result=[]
for i in range(0,N-1):
    result.append(down[i]+up[(len(up)-1)-i]+1)

print(max(result))

#수정 후 (막대기 1개)
result=[]
for i in range(0,N):
    result.append(down[i]+up[N-1-i]-1)
print(max(result))

# (오답 풀이)-------
# 1. result값을 구할때!
#    up리스트와 down리스트에서 막대기를 같은 곳을 두고 생각해야하지만, (막대기 1개)
#    내 풀이는 막대기를 2개를 놓고 생각해서 틀린것이다.

# 2. 애초에 down값을 계산할 때, 
#    reverse로 넣지말고, for문을 이용해 뒤집어진 상태로 구하는게 좋은것같다.
#-------------------

# // 인터넷 참고(수정)
x = int(input())

case = list(map(int, input().split()))

# 정방향의 리스트의 '가장 긴 증가하는 부분 수열 방법' 
increase = [1 for i in range(x)]
for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)

print(increase)

# 역방향 리스트의 '가장 긴 증가하는 부분 수열 방법'
decrease2 = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            decrease2[i] = max(decrease2[i], decrease2[j]+1)

print(decrease2)

# (틀렸던 부분!)
# 막대기가 하나이기 때문에, increase와 decrease2에서 i로 같게 놓고 설정해야한다.
# 그리고 막대기에 해당하는 값을 두번 더해주었기 때문에, 값 한개를 빼주어야 한다.
result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease2[i] -1 

print(max(result))


'''백준 2565번 (전깃줄)'''

# 아이디어
# (최찬)
# 1. 각각 순서쌍이 맞닿는 선을 A좌표 순으로 순서를 매긴다.
# 2. 맞닿는 선들을 넣는 리스트를 만들어준다.(인덱스:선의 값-1, 값:맞닿는 선의 값)
#    ex: [[2,4,5,6,7],[1,4],[4,5,6,7],[1,2,3],[1,3],[1,3],[1,3]]
# 2. 저장된 8개 리스트에서 크기가 제일 큰 리스트의 인덱스+1값을 모든 리스트에서 제거해준다.
# 3. 같은 방법으로 모든 리스트의 값이 사라질 때까지 계산해준다.

# // 구현을 해보려고 했지만, 실패했습니다.
N = int(input())

ptn = []
for i in range(N):
    ptn.append(list(map(int, input().split())))

buf=[]

# A가 1일 때, 
for i in range(1, len(ptn)):
    if ptn[i][1]<ptn[0][1]:
        buf.append(ptn[i][0])
        
# (오답풀이)--------------------

'''
아직 동적계획번 2문제 + 조합론 2문제 , 총 4문제를 완성하지못했습니다,,
오늘 밤까지 최대한 완성시키겠습니다!
'''


