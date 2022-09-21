# 백준 1085번
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# 백준 4153번
while True :
    buf = list(map(int, input().split()))
    if sum(buf) == 0:
        break
    
    long = max(buf)
    buf.remove(long)
    
    if buf[0]**2 + buf[1]**2 == long**2:
        print('right')
    else :
        print('wrong')
        
        
# 백준 2231번
A = int(input())

result = 0
for i in range(1,A+1):
    B = list(map(int, str(i)))
    # ex. 245는 2, 4, 5로 분리되어 리스트에 저장된다.
    
    result = i +sum(B)
    
    if result == A:
        print(i)
        break
    if i==A:
        print(0)
      
       
# 백준 2292번 
n = int(input())

number = 1
count = 1

while n>number :
    number += 6*count
    count += 1
    
# 1 : 1칸, 2-7 : 2칸, 8-19 : 3칸, 20-37 : 4칸, 38-61 : 5칸
# 구간을 이용하여 칸 비교하기
print(count)


# 백준 2798번
n, m = map(int, input.split())
num = list(map(int, input().split()))

L = len(num)

sum = 0

for i in range(0, L-2):
    for j in range(i+1, L-1):
        for k in range(j+1, L):
            # 전체를 쫙 훑어서 더해주는 방법
            
            if num[i] + num[j] + num[k] > m:
                continue
            # m을 넘는것은 pass
            
            else: 
            # m을 안 넘으면 sum에 저장 해놓은다.
                
                sum = max(sum,num[i] + num[j] + num[k])
                # 계속 저장되는 m이하의 값들중 제일 큰값을 반환
print(sum)

