### File & Writer Info
# Assignment Number : 04
# Student ID.................. : 14
# Student Name........... : 정상대
# File Name.................... : hw4_정상대
# Program Description : 기존에 가진 식당별 메뉴, 가격 데이터를 통해
#                             사용자가 먹고픈 메뉴가 등록되어 있을 경우,
#                             해당 메뉴를 판매하는 식당, 메뉴의 가격을 반환하며
#                             값이 없을 경우 결과가 없음을 알림.
# Submit Date................ : 2018-06-29
### Variable Description
# restaurant_list............ : 각 식당별 상호, 메뉴, 가격에 대한 key:value로 이루어진 딕셔너리를
#                             리스트로 갖는 변수
# want_to_eat................ : 사용자에게 입력받은 메뉴를 갖는 변수
# hasMenu..................... : 사용자가 입력한 메뉴가 restaurant_list에 있는지 없는지를 확인하기 위해
#                             boolean값으로서 False값으로 초기화 해놓은 변수


restaurant_list = [{'상호': 'A','메뉴': '피자', '가격(원)': 20000},     # 상호, 메뉴, 가격 key마다 각 데이터별 해당하는 value값을 딕셔너리로 저장하고 
                     {'상호': 'B','메뉴': '치킨', '가격(원)': 18000},      # 각 데이터들의 key:value로 이루어진 딕셔너리를 리스트로 restaurant_list 변수에 할당
                     {'상호': 'C','메뉴': '짜장면', '가격(원)': 5000},
                     {'상호': 'D','메뉴': '초밥', '가격(원)': 15000},
                     {'상호': 'E','메뉴': '치킨', '가격(원)': 23000},
                     {'상호': 'F','메뉴': '족발', '가격(원)': 30000}]


want_to_eat = input('먹고 싶은 음식을 입력하세요: ') # 사용자에게 값을 입력받기 위해 input 함수를 사용하였으며
                                                                  # 입력할 값에 대한 정보를 위해 input 내 문구를 입력
                                                                  # 이를 want_to_eat 변수에 할당



hasMenu = False                                             # 입력받은 Menu가 있는지, 없는지를 판단하기 위해 boolean값을 갖는 hasMenu를 생성

for values in restaurant_list:                                # for문을 restaurant_list의 개수만큼 반복
    if values.get('메뉴') == want_to_eat:                  # 현재 참조중인 딕셔너리에서 '메뉴' Key에 해당하는 value값과 want_to_eat로 입력받은 값이 같을 경우, if문을 실행
          print('식당 {}, 가격 {} 원'.format(values.get('상호'),values.get('가격(원)')))   # 정해진 형식에 맞게 멘트와 정보를 주기 위해 print 함수를 사용하며
                                                                                                     # 상호명, 가격의 크기(길이)에 상관없이 올바르게 값을 호출할 수 있도록 format을 사용
          hasMenu = True                                    # 프린트가 될 경우, 입력된 메뉴가 기존 메뉴와 일치하는것이기에 프린트라인 다음줄로 hasMenu를 True로 값을 변경함.
if hasMenu == False:                                        # 현재의 코드에서 hasMenu를 사용하지 않을경우와 else를 사용하였을 경우, break를 걸지 않으면 else문이 무조건 출력되는 형태이며
    print('결과가 없습니다.')                                 # break를 할 경우, 메뉴를 2개가지고 있는 치킨 중 앞선 1개만 출력되도록 되기에
                                                                  # else문 대신 hasMenu 변수를 생성하고, 메뉴가 존재하지않아 hasMenu값이 True로 변경되지 않았기에 해당 if문 실행시 hasMenu가 가진 값이 False일 경우,
                                                                  # '결과가 없습니다.' 라는 문구를 출력해주기 위해 print 함수를 사용