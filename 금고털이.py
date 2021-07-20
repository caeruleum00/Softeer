import sys

W, N = map(int, sys.stdin.readline().split(' '))
gold = [0] * N  # 금속의 종류만큼 입력받을 리스트를 미리 생성
total = 0

for i in range(N):
        gold[i] = list(map(int, sys.stdin.readline().split(' ')))  # 빈 리스트에 append를 할 때보다 시간이 단축됨

gold.sort(key = lambda x : x[1], reverse = True) # 무게당 가격이 높은 값부터 차례로 정렬

for i in range(len(gold)):                       # 무게가 배낭 무게만큼 가득 차면 stop
        if gold[i][0] >= W:                      
                total += W*gold[i][1]            
                break
        elif gold[i][0] < W:                     # W를 배낭의 무게이자 남은 저장 공간의 개념으로 본다.
                total += gold[i][0]*gold[i][1]   # 배낭에 남은 공간보다 금속의 무게가 작으면 (금속 무게 * 무게 당 가격)을 저장하고
                W -= gold[i][0]                  # 남은 공간을 재정의해준다.
        
print(total)

```
득점  
100.0 / 100   
실행시간    
1975ms   
메모리  
191.16Mb  
```
