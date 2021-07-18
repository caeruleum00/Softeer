import sys

line = list(map(int, (input().split(' '))))

if sorted(line) == line:
        print('ascending')
elif sorted(line, reverse = True) == line:
        print('descending')
else: print('mixed')

        
'''
input()으로 '1 2 3 4 5 6 7 8'을 받았다면 .split(' ') 함수를 이용해 공백을 기준으로 나눠 리스트 형태로 변환해준다.
-> result: ['1', '2', '3', ...]

원소를 문자가 아닌 숫자로 변환해주기 위해 map함수를 이용해 int형으로 변환해준뒤 line 이라는 리스트에 저장한다.
-> result: [1, 2, 3, 4,...]

해당 리스트가 sorted(line)과 같다면 즉, 애초부터 오름차순으로 정렬 되어있다면 line 5에서 True가 반환되어 'ascending'이 print 된다.
반대로 sorted(line, reverse = True)와 같다면, 내림차순으로 정렬 되어있었기 때문에 'descending'을 출력한다.

위 두가지 경우에 해당하지 않는다면 'mixed'를 출력한다.

입력형식에서 1 ~ 8사이의 숫자를 입력한다고 명시되어있으므로 해당 부분에 관한 디버깅은 진행하지 않았다.


컴파일
true
득점
100.0 / 100
실행시간
106ms
메모리
37.03Mb
'''
