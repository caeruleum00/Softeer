# Softeer
HYUNDAI GROUP Softeer Code Review  
자세한 코드 리뷰는 해당 문제.py 파일 안에 주석으로 적어놓았습니다.

## List
### Level 2
[1. 8단 변속기](#1-8단-변속기)  
[2. 금고털이](#2-금고털이)

## Level 2  
### 1. 8단 변속기  
### < 힌트 >
sorted 함수만 안다면 쉽게 풀 수 있는 문제입니다.  
시간 단축을 위해 sorted를 사용하지 않고 all, range, zip을 이용해 풀이할 수도 있습니다.  
```
list = [1, 2, 3, 4]
sorted(list) == list 이면 True를 반환
all (list[i] < list[i+1] for i in range(len(list) -1)의 모든 값이 True이면 True를 반환
all (x < y for x, y in zip(list[:-1], list[1:]))의 모든 값이 True이면 True를 반환
```

#### < 문제 >
변속기가 1단 ~ 8단으로 연속적으로 변속하면 ascending,    
8단 ~ 1단으로 연속적으로 변속하면 descending,   
둘다 아니라면 mixed.  
<br>
변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면 mixed인지 출력하는 프로그램을 작성.  

#### < 입력예제 >
```
1 2 3 4 5 6 7 8
```
#### < 출력예제 >
```
ascending
```

### 2. 금고털이
### < 힌트 >
sorted 함수만 안다면 쉽게 풀 수 있는 문제입니다.  
시간 단축을 위해 sorted를 사용하지 않고 all, range, zip을 이용해 풀이할 수도 있습니다.  
```
list = [1, 2, 3, 4]
sorted(list) == list 이면 True를 반환
all (list[i] < list[i+1] for i in range(len(list) -1)의 모든 값이 True이면 True를 반환
all (x < y for x, y in zip(list[:-1], list[1:]))의 모든 값이 True이면 True를 반환
```

#### < 문제 >
변속기가 1단 ~ 8단으로 연속적으로 변속하면 ascending,    
8단 ~ 1단으로 연속적으로 변속하면 descending,   
둘다 아니라면 mixed.  
<br>
변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면 mixed인지 출력하는 프로그램을 작성.  

#### < 입력예제 >
```
1 2 3 4 5 6 7 8
```
#### < 출력예제 >
```
ascending
```
