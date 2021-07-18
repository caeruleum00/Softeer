# Softeer
HYUNDAI GROUP Softeer Code Review  
자세한 코드 리뷰는 해당 문제.py 파일 안에 주석으로 적어놓았습니다.

## List
### Level 2
[1. 8단 변속기](#8단-변속기)


## Level 2  
### 1. 8단 변속기  
### < 힌트 >
sorted 함수만 안다면 쉽게 풀 수 있는 문제입니다.  
시간 단축을 위해 sorted 사용 이외에 all과 zip을 이용해 풀이할 수 있습니다.  
sorted = all ~ range | all ~ zip    

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
