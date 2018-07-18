### File & Writer Info
# Assignment Number : 02
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw2_정상대
# Program Description : 문자열 자료형의 변수를 생성하고 slicing하며,  
#                             문자열 이스케이프를 활용한 값의 출력
# Submit Date............... : 2018-06-25
### Variable Description
# cellphone.................... : 휴대폰의 제조사와 모델명 정보를 갖는 변수
# company..................... : cellphone 변수의 값 중 제조사를 갖는 변수
# model.......................... : cellphone 변수의 값 중 모델명을 갖는 변수

cellphone = 'Samsung Galaxy8' #휴대폰 정보를 문자열 자료형으로 cellphnoe변수에 문자열 자료형으로 저장
print(cellphone) #cellphone 변수에 저장한 휴대폰 정보를 출력하기위해 print 함수를 사용

company = cellphone.split(' ')[0] #만약 입력을 받는 프로그램을 작성시, 글자수로 나눌 경우 
                                         #회사명, 모델명이 길이가 다를 수 있기에 (제조사, 모델)의 양식으로서
                                         #입력받을 거라 가정하여 공백의 앞을 제조사, 공백의 뒤를 모델로 지정.
                                         #ex) 애플 아이폰7+의 경우 -> Apple IPhone7+

print(company) #print 함수를 사용하여 company변수에 들어있는 제조사명을 출력

model = cellphone.split(' ')[1] #cellphone 변수를 공백 기준으로 나눈 뒤를 모델변수에 저장
print(model) #print 함수를 사용하여 model 변수에 들어있는 모델명을 출력

print(type(company)) #company 변수의 자료형을 출력하기위해 type(company)를 print함수를 사용하여 출력
print(type(model)) #model 변수의 자료형을 출력하기위해 type(model)를 print함수를 사용하여 출력

# 문자열 이스케이프('\')를 활용한 print 함수 한번으로 장문의 텍스트 출력
# \n을 이용한 줄바꿈으로 한개의 print 함수 내 3줄의 문장을 작성할 수 있도록 하였습니다.
print('It had been that way for days and days. \n And then, just before the lunch bell rang, he walked into our class room. \n Stepped through that door white and softly as the snow.')
