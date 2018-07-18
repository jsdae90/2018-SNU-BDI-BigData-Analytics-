### File & Writer Info
# Assignment Number : 03
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw3_정상대
# Program Description : 문자열, 리스트, 튜플을 생성 및 활용하며
#                             리스트와 튜플을 슬라이싱하는 방법을 익힘.
# Submit Date............... : 2018-06-27
### Variable Description
# foodprice................... : 순수 음식 가격을 가진 변수
# vat................................ : VAT를 가진 변수
# totalprice.................... : 음식 가격과 VAT까지 계산된 음식의 총 가격을 가진 변수
# s.................................... : 문자열을 가진 변수
# numbers..................... : 특정한 정수를 갖는 튜플을 가진 변수
# fruits............................ : 과일들을 원소로 갖는 리스트를 가진 변수
# fruits_sub.................... : fruits 변수에서 첫 세 요소를 slicing하여 해당 값을 가진 변수


#Q1
foodprice = 30000  #순수 음식 가격을 foodprice변수에 할당
vat = 0.15             #VAT 15%를 0.15로 계산하여 vat변수에 할당
totalprice = int(foodprice + (foodprice * vat))         # foodprice * vat는 int형 * float형이기에 결과값이 float로 나오므로 
                                                                  # 위의 값과 foodprice를 더한 값도 마찬가지로 float형이기에 int형으로 형변환을 해준다.
print('스테이크의 원래 가격은 {} 원입니다. 하지만 VAT가 {}%로, 계산하셔야 할 가격은 {} 원입니다.'.format(foodprice, int(vat*100), totalprice))  #vat라는 float형 변수의 값을 15로 프린트해야하므로
                                                                                                                                                                              #vat에 100을 곱하여 나타내도록 만들어주며 int형으로 형변환.


#Q2
s = '@^TrEat EvEryonE yOu meet likE you want tO be treated.$%'    # 정해진 문자열을 s 변수에 할당
import re                                                                          # re.sub을 통해 특수문자를 제거하기 위해 re를 import
s = re.sub('[@^$%]', '', s)                                                       # s 변수에 들어있는 특수문자인 @, ^, $, %를 ''로 대체하여 공백도 없이 삭제되도록 하여 s에 재할당
s = s.capitalize()                                                                  # capitalize 메소드를 이용해 s 변수에 들어있는 값의 첫 문자를 대문자로 하며 첫 문자를 제외한 나머지는 소문자로 변환하여 재할당
print(s)                                                                             # s 값을 출력하기위해 print()를 사용.

#Q3
numbers = (2, 18, 26, 89, 45, 39, 14)        # 정해진 값들을 튜플로 생성하여 numbers 변수에 할당
print(numbers)                                   # numbers 튜플을 print 함수를 사용하여 출력

#Q4
print(len(numbers))            # len함수를 이용해 numbers 변수의 길이를 구하고, 그 값을 print()를 이용해 출력

#Q5
fruits = ['apple', 'orange', 'strawberry', 'pear', 'kiwi']       # 정해진 원소들을 리스트로 생성하기 위해 [ ] 를 사용, 그 리스트를 fruits 변수에 할당
print(fruits)                                                         # fruits 변수를 print()를 이용하여 출력

#Q6
fruits_sub = fruits[0:3]            # fruits변수의 원소중 앞에서부터 세개의 원소 0, 1, 2를 뽑아내기 위해 [0:3]으로 slicing,  해당 값들을 fruits_sub에 할당
print(fruits_sub)                    # fruits_sub가 가진 값을 print()를 이용하여 출력
