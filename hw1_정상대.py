### File & Writer Info
# Assignment Number : 01
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw1_정상대
# Program Description : 함수들의 최종 print를 고려한 형변환 및 값을 입력받고 정해진 멘트와 같이 출력하는 과제입니다.
# Submit Date............... : 2018-06-22
### Variable Description
# season.......................... : 사용자가 좋아하는 계절로 대답한 값을 포인팅함
# date.............................. : 사용자가 태어난 날짜(일)로 대답한 값을 포인팅함


season = input('What is your favorite season? ')  # 사용자의 좋아하는 계절을 입력받기 위해 input 함수를 사용
print(season)  # 입력받은 값을 출력하기 위해 print 함수 사용

date = input('Which date were you born? ') # 사용자의 태어난 날짜를 입력받기 위해 input 함수를 사용
print(type(date))   #date함수의 class 출력하기 위해 print 함수 사용
date = float(date) #date함수의 값을 float로 변환하여 date가 포인팅하게함
print(type(date))   #float로 변환된 date함수의 class를 확인

#정해진 멘트와 함께 입력받은 계절, 생일자를 출력하기 위해 print 함수를 사용
#입력받은 계절을 포인팅하는 season을 멘트를 닫고 다시 열지않기위해 ({},.format.(season)을 사용
#date값과 th 사이 공백이 없어야 하나, 프로그램으로서 사용하여 여러 값을 입력받는다면
#date를 str로서 출력하여 date+th를 하기엔 함수 핸들링 시 불편해질 것이라 생각하여
#정해진 멘트의 끝임을 이용하여 end옵션값을 'th'로 주어 season값 바로 뒤
#th를 받아 0th 형식이 될 수 있도록 함 
print('My favorite season is {}. I was born on the'.format(season), int(date), end='th.')