### File & Writer Info
# Assignment Number.. : 10
# Student ID......... : 14
# Student Name....... : 정상대
# File Name.......... : hw10_정상대
# Program Description : 파일을 열고 자료를 처리하는 법을 익힌다.
# Submit Date........ : 2018-07-15
### Variable Description
# file............... : open한 파일을 가진 변수
# lines.............. : file변수가 가진 값을 리스트 하나에 출력한 값을 가진 변수
# subway_data........ : 리스트 내 딕셔너리별로 해당 데이터의 값을 갖도록 함
# local_dict......... : 로컬변수이며 딕셔너리형으로서 리스트 내 저장할 값을 갖는 변수
# test1.............. : test1의 조건에 해당하는 값들을 가진 변수
# test2.............. : test2의 조건에 해당하는 값들을 가진 변수
# test3.............. : test3의 조건에 해당하는 값들을 가진 변수



file = open('C:/Users/Administrator/Downloads/subway.txt', mode='r', encoding='UTF-8-SIG') # 경로에 있는 파일을 read모드로 불러 파일에 저장하며
                                                                                           # 맨 앞 ufeff를 해결하기 위해 UTF-8-SIG로 인코딩하여 부름

lines = file.readlines()  # 파일변수가 가진 값을 하나의 문자열로 읽어 lines에 저장

for line in range(len(lines)):                        # lines의 length만큼 반복하며
    lines[line] = lines[line].strip().split(',')      # lines[0~len(lines)]까지 돌며 strip과 ,로 split하여 다시 재할당함.

subway_data = []                   # 리스트를 갖는 subway_data를 선언

for i in range(1, len(lines)):                      # lines의 length만큼 반복
                                                    # range를 1부터로 설정하지않을경우 key값의 이름이 자신을 value로 갖는 1개의 딕셔너리가 생기기에 1부터로 함.
    local_dict = {}                                 # 딕셔너리를 갖는 로컬변수 local_dict를 선언
                                                    # 이를 로컬로 선언하지않고 글로벌로 선언하여 사용할 경우,
                                                    # 반복문의 맨 마지막 값만 저장되어 있는 문제가 있다.
    for j in range(len(lines[i])):                  # lines[i]의 length만큼 반복
        local_dict[lines[0][j]] = lines[i][j]       # local_dict[lines[0][j]] 키값에 lines[i][j]를 value 값으로 넣음
    subway_data.append(local_dict)                  # local_dict에 있는 값을 subway_data에 추가


# Test 1
print('='*20 + ' 테스트 1 ' + '='*20)               # 테스트 1이라는 문구 양쪽에 =를 20개씩 출력
print('금요일의 하차 정보만 모은 목록'.center(38))  # 정해진 문구를 출력하며 가운데정렬을 해주기 위해 center 값을 조정
test1 = []                                          # test1에 값을 넣고자 빈 리스트를 할당

for i in range(len(subway_data)):                   # subway_data의 length만큼 반복
    if subway_data[i]['요일'] == '금':              # subway_data[0-len(subway_Data)]를 돌며 해당 딕셔너리 내 '요일'Key의 Value값이 '금'일경우 True로서 하위 코드 실행
        if subway_data[i]['구분'] == '승차':        # subway_data[0-len(subway_Data)]를 돌며 해당 딕셔너리 내 '구분'Key의 Value값이 '승차'일 경우 True로서 하위 코드 실행
            test1.append(subway_data[i])            # test1에 subway_data[i] 딕셔너리를 추가함

print(test1)    # test1에 저장된 값들을 출력

# Test 2

print('='*20 + ' 테스트 2 ' + '='*20)                                    # 테스트 2라는 문구 양쪽에 =를 20개씩 출력
print('9시에서 10시 승차 인원이 5000명 이상인 날짜의 목록'.center(32))   # 정해진 문구를 출력하며 가운데정렬을 해주기 위해 center 값을 조정

test2 = []                                                               # test2에 값을 넣고자 빈 리스트를 할당

for i in range(len(subway_data)):                                        # subway_data의 length만큼 반복
    if subway_data[i]['9'] >= '5000' and subway_data[i]['10'] >= '5000': # subway_data[i]의 딕셔너리 내 '9' key의 5000이상, '10' key의 값이 5000이상이면 True, 하위 코드 실행
        test2.append(subway_data[i]['날짜'])                             # 위의 조건에 맞는 데이터들은 딕셔너리 내 '날짜' key값 정보를 test2에 추가

print(test2)     # test2에 저장된 값들을 출력


# Test 3


print('='*20 + ' 테스트 3 ' + '='*20)                                     # 테스트 3이라는 문구 양쪽에 =를 20개씩 출력
print('날짜가 2의 배수인 날짜 중 \n8시에서 9시 승차 인원은 짝수인 날들의 정보를 모은 목록'.center(75))  # 정해진 문구를 출력하며 글이 길어 두줄로 나눔 
                                                                                                        # 그리고 가운데정렬을 위해 center 조정

test3 = []                                                                             # test3에 값을 넣고자 빈 리스트를 할당

for i in range(len(subway_data)):                                                      # subway_data의 length만큼 반복
    if int(subway_data[i]['날짜']) % 2 == 0:                                           # '날짜'key의 value가 2의 배수인 값을 찾기위해 2로 나눈 나머지가 0일경우 True로 하위 코드 실행
        if int(subway_data[i]['8']) % 2 == 0 and int(subway_data[i]['9']) % 2 == 0:    # subway_data의 '8'key의 value값을 2로 나눈 나머지가 0이고, '9'key의 value값을 2로 나눈 나머지가 0일 경우 하위 코드 실행
            test3.append(subway_data[i])                                               # 위 조건에 해당하는 값을 가진 딕셔너리인 subway_data[i]를 test3에 추가

print(test3)     # test3에 저장된 값들을 출력