### File & Writer Info
# Assignment Number : 05
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw5_정상대
# Program Description : if-elif-else문, for, while문을 활용하는 법을 익힘
# Submit Date................ : 2018-07-02
### Variable Description
# a..................................... : 수의 비교를 위해 정수값을 할당받는 변수
# b..................................... : 수의 비교를 위해 정수값을 할당받는 변수
# c..................................... : 수의 비교를 위해 정수값을 할당받는 변수
# city................................ : 도시의 이름들을 리스트로 가진 변수
# size................................ : city에 따른 면적(km^2)을 저장하기 위해 만든 변수



#Q1

a = int(input('Enter a: '))   # a에 들어갈 값을 입력받고 integer로 변환하여 a에 할당
b = int(input('Enter b: '))  # b에 들어갈 값을 입력받고 integer로 변환하여 b에 할당
c = int(input('Enter c: '))   # c에 들어갈 값을 입력받고 integer로 변환하여 c에 할당

if a > b and a > c :   # a가 b보다 크고, a가 c보다 클 경우 
    print(b+c)           # b+c의 값을 출력
 
elif b > a and b > c : # b가 a보다 크고, b가 c보다 클 경우
    print(a+c)           # a+c의 값을 출력
    
elif c > a and c > b : # c가 a보다 크고, c가 b보다 클 경우
    print(a+b)           # a+b의 값을 출력


# Q2   

city = ['Seoul', 'New York', 'Beijing','그 외']   # 도시들의 목록을 순서대로 작성하여 리스트로 city 변수에 할당

cityname = input('Enter the name of the city: ') # 찾고자 하는 도시의 이름을 사용자에게 입력받기 위해 input 함수 사용

if cityname == city[0]:   #입력받은 cityname의 값이 city[0]인 Seoul과 같을 경우
    size = 605              # size에 605 값을 할당
    
elif cityname == city[1]: #입력받은 cityname의 값이 city[1]인 Seoul과 같을 경우
    size = 789              # size에 789 값을 할당
    
elif cityname == city[2]: #입력받은 cityname의 값이 city[2]인 Seoul과 같을 경우
    size = 16808           # size에 16808 값을 할당
    
else:                         #입력받은 cityname의 값이 위의 조건에 해당하지 않을 경우
    size = 'Unknown'      # size에 'Unknown'
    
print('The size of {} is {}'.format(cityname, size))  #정해진 멘트와 함께 사용자가 입력한 도시와 그 도시가 갖는 size를 출력




# Q3
from math import factorial     #factorial 함수 사용을 위해 math 라이브러리로부터 factorial 함수를 import

x = 0  # x값 초기화
for x in range(0, 10):         #x는 정해진 범위인 0부터 10까지(0부터 9의 값까지) 
    print(factorial(x))          # factorial(0), factorial(1), ㆍㆍㆍ, factorial(9) 와 같이 계산하여 출력



# Q4

y = 0  # y값 초기화
while y < 10:                 # y가 10보다 작다는 조건이 True일 경우(y가 10미만일 경우)
    print(factorial(y))         # y는 0부터 계산하며 factorial(y)를 계산하여 출력함
    y += 1                     # y의 값을 +1 증가시켜서 y에 재할당