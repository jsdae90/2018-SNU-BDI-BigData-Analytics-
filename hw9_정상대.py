### File & Writer Info
# Assignment Number : 09
# Student ID................... : 14
# Student Name............ : 정상대
# File Name.................... : hw9_정상대
# Program Description : csv 파일을 불러와 읽는 방법, txt 파일을 파싱하는 방법을 익힘
# Submit Date................ : 2018-07-11
### Variable Description
# file................................. : open 함수를 통해 불러온 파일을 갖는 변수
# sentences.................... : 데이터의 각 행들을 저장하기 위한 변수
# rdr................................. : reader 함수를 이용한 file 데이터를 갖는 변수

import os                  # 경로 설정을 위해 os 모듈을 불러옴
os.chdir('C:/Users/renz/Desktop/pyprg/hw/hw9')  # 파일이 위치한 경로로 기본경로 설정

# Q1

with open('cars.csv') as file:                            # cars.csv 파일을 file로 사용함
    for line in file:                                        # for문을 통해 각 줄을 출력하도록 함
        print(line)

# Q2

sentences = []                                            # 문자열을 저장하기 위해 sentences 변수에 빈 리스트를 줌

with open('cars.csv') as file:                            # cars.csv 파일을 file로 사용함
    for line in file:
        sentences.append(tuple(line.split(',')))        # for문을 돌면서 ',' 기준으로 나눈 파일의 각 줄을 tuple로 하여 sentences에 저장 

print(sentences)                                          # sentences의 값 출력 


# Q3, Q4를 별개의 퀴즈로 안보고 하나의 py파일이므로 하나로 보아 4번에서 사용할 저장과 동시에
# 3번의 조건인 프린트도 하였습니다. 

file = open('My way.txt', 'r')                            # My way.txt 파일을 읽기전용으로 열어 file에 저장함
sentences = []                                            # 문자열 저장을 위해  sentences 변수에 빈 리스트를 줌
for line in file:
    sentences.append(line)                              # sentences에 각 행의 내용을 추가한다
    print(line)                                              # 해당 line들을 for문을돌며 출력해준다


# Q4
print(sentences[2])                                       # for문이 끝난 뒤, sentences[2] (3번째원소)를 출력함
file.close()                                                 # 파일을 닫는다

file = open('My way.txt', 'a')                                        # My way.txt 파일의 마지막 행에 데이터 추가를 위해 mode='a'로 불러옴
file.write("\nI'll state my case, of which I'm certain")          # 마지막 행에 해당 문구를 작성
file.close()                                                              # 열었던 파일을 닫는다.

file = open('My way.txt', 'r')                                        # 읽기전용으로 My way파일을 불러와서 file에 저장
print(file.read(), end='')                                                       # file.read()를 이용하여 데이터 전체를 하나의 문자열로 프린트
file.close()                                                              # 열었던 파일을 닫는다.
'''
아래 코드는 reader로 코딩했던것입니다.
import csv                                                             # reader 함수를 사용하기 위해 csv모듈을 불러옴
file = open('My way.txt', 'a')                                        # My way.txt 파일의 마지막 행에 데이터 추가를 위해 mode='a'로 불러옴
file.write("\nI'll state my case, of which I'm certain")      # 마지막 행에 해당 문구를 작성
file.close()                                                              # 열었던 파일을 닫는다.

file = open('My way.txt', 'r')                                        # 읽기전용으로 My way파일을 불러와서 file에 저장
rdr = csv.reader(file)                                                 # 해당 파일을 reader를 이용한 값을 rdr에 저장
for line in rdr:                                                         # for문을 돌며 rdr의 각 행을 출력함
    print(*line)                                                         # *line 해주지 않고 출력할 경우, 리스트까지 출력되어
                                                                          # 예시와 같이 출력해줄 수 없기에 출력에서 리스트를 제하기 위해 *line
file.close()                                                              # 파일을 닫음
'''