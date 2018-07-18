### File & Writer Info
# Assignment Number : 08
# Student ID................... : 14
# Student Name............ : 정상대
# File Name.................... : hw8_정상대
# Program Description : 패키지(Package)와 모듈(Module)을 불러오는 법을 익힘.
# Submit Date................ : 2018-07-10
### Variable Description
# now............................... : 현재의 시간값을 갖는 변수
# text................................ : 입력받은 값을 Counter함수를 적용한 값을 갖는 변수
# voweldic....................... : 딕셔너리 형태로 text값이 갖는 값들 중 모음만을 저장시키기 위한 변수
# vowels.......................... : 리스트 형식으로 모음값을 갖는 변수
# srtvowel....................... : voweldic이 가진 값을 reverse하여 sort한 값을 갖는 변수
# replac............................ : reverse하여 sort한 값의 첫번째 문자를 갖는 변수
# x..................................... : 사용자가 함수 사용시 입력한 값중 가장 많이 카운팅된 모음을 대문자로 변경한 값을 가짐

# Q1
import datetime                                      #datetime 모듈 내 함수를 사용하기위해 모듈을 import함
now = datetime.datetime.now()                #datetime 모듈 내 함수를 이용하여 현재 시간을 now변수에 저장
print(now.strftime('%Y-%m-%d %H:%M:%S'))#저장한 변수를 '%Y-%m-%d %H:%M:%S' 형식으로 지정하기 위해 srftime 함수를 사용

# Q2
import calendar                                      # calendar 모듈을 import
print(calendar.isleap(2050))                        # isleap 함수를 이용해 2050년이 윤년인지 여부를 출력함
print(calendar.weekday(2050, 7, 7))              # weekday 함수를 이용해 2050년 7월 7일의 요일을 출력함

# Q3

from collections import Counter                  # collections 모듈로부터 Counter 함를 import
def vowel(x):                                          # vowel(x)함수를 아래와 같은 조건으로 선언
    text = Counter(x)                                # 입력받은 x를 Counter함수를 사용하여 text에 저장
    voweldic = {'a' : 0,                               # 각 모음 별 갖는 값을 저장하기 위해 변수를 생성
                'e' : 0,
                'i' : 0,
                'o' : 0,
                'u' : 0}  # text변수가 값는 딕셔너리에 직접 voweldic.get을 통한 출력 시
                          # u의 딕셔너리 value가 0이 아닌 None이기에 voweldic을 생성함
    vowels = ['a', 'e', 'i', 'o', 'u']  # 입력받은 값 내 모음에 대한 문자열 카운팅만을 위해
                                        # 문자열 카운팅을 위한 값 저장
    
    for t in vowels:                                                  
        print('The number of', t+': {}'.format(text[t]))          # 반복문을 돌며 정해진 멘트의 출력을 위해 print 사용
        voweldic[t] = text[t]                                        # vowels 내의 t가 현재 보는 값일 경우,
                                                                         # voweldic의 해당 값에 값을 저장 
    srtvowel = sorted(voweldic.items(), key = lambda k : k[1], reverse=True)   # voweldic의 딕셔너리가 가진 값을 보며
                                                                                                 # value값 기준으로 reverse하여 정렬
    replac = srtvowel[0][0]                                         # reverse sorted의 맨 첫 값은 카운팅이 가장 높은 값이므로,
                                                                         # 해당 값의 문자를 replac에 저장
    x = x.replace(replac, replac.upper())                         # replac에 저장된 값을 대문자로 변경하여 x에 값을 덧씌움
    print(x)                                                            # x를 출력함

vowel('The regret after not doing something is bigger than that of doing something.')     #문자열을 입력해 함수 사용