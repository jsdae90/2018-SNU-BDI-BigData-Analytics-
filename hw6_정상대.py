### File & Writer Info
# Assignment Number : 06
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw6_정상대
# Program Description : 새로운 함수를 정의 하는 법을 익히며, Lambda function을 익히기 위함
# Submit Date................ : 2018-07-05
### Variable Description
# area_triangle................ : 삼각형의 높이와 밑변 값을 입력받아 삼각형 면적값을 갖는 함수
# distance........................ : 2차원 공간 상 두 점 사이의 거리를 계산하는 변수
# dist................................ : distance의 로컬변수로 for문 내에서 값을 저장하기 위해 사용한 변수
# count............................ : 재귀호출을 통해 카운트다운과 같은 출력을 하는 재귀함수
# area_triangle_id.......... : 삼각형의 높이와 밑변 값을 입력받아 삼각형 넓이값을 갖는 람다함수



# Q1. 삼각형의 면적을 구하는 area_triangle() 함수를 정의

def area_triangle(h, w):       # h, w값을 입력받는 area_triangle 함수를 정의
    return print(0.5 * h * w)         # area_triangle 함수에 h,w 값이 입력될 경우
                                   # 0.5 * h * w 값을 반환함.

area_triangle(10, 15)   #h=10, w=15로 값을 할당하여 area_triangle 함수를 call

# Q2. 2차원 공간 상에서 두 점 사이의 거리를 계산하는 distance() 함수를 정의
# 문제에 맞는 입력값이 어떤형식인지를 몰라 

def distance(a, b):     #a, b값을 받는 distance 함수를 정의
    dist = 0             #로컬변수로 사용할 dist를 0으로 초기화
    for i in range(2):   # for문을 통해 거리 계산식 계산, 2번 반복함
        dist += pow(a[i] - b[i], 2) # 처음 돌때는 x1 - x2의 제곱을 dist에 값을 넣으며
                                        # 두번 돌때는 y1 - y2의 제곱을 dist값에 더해준다.
    return print(dist **0.5)                # 반복문이 끝난 뒤, dist에 저장된 값에 루트를 씌운 값을 출력

distance([1,2], [5,7])                # 문제에 주어진 바와 같이, a = (1,2), b=(5,7)값을 리스트로 주어 함수 사용


# Q3. 재귀함수 count()를 생성해 임의의 양의 정수부터 0까지 세어본다.

def count(n):            # n을 받는 카운트함수를 정의
    if n > 0:              # n이 0보다 클 경우 if문 하위 실행
        print(n)           # n의 값을 출력함
        count(n-1)       # 함수 자신을 재귀호출하여 입력된 n값을 줄여줌
    else:                  # n이 1보다 작아져 0보다 크다는 조건에 부합하면
        print("zero!!")   # zero!! 문구를 출력함

count(5)                  # n값에 5를 넣어 count함수를 사용

# Q4. 삼각형의 넓이를 계산하는 람다함수 area_triangle_id()를 생성
# h=10, w=15의 인자값을 전달해 그 결과를 출력

area_triangle_id = lambda h, w : print(0.5 * h * w)   # 람다를 사용하여 h,w의 값을 받으며
                                                         # 0.5*h*w 값을 출력하는 area_triangle_id 함수 생성
area_triangle_id(10, 15)                            # area_triangle_id의 h에 10, w에 15값을 입력하여 사용