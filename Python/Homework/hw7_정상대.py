### File & Writer Info
# Assignment Number.. : 07
# Student ID......... : 14
# Student Name....... : 정상대
# File Name.......... : hw7_정상대
# Program Description : 제어문(if-else, while)을 활용하는 방법을 익힌다.
# Submit Date........ : 2018-07-09
### Variable Description
# switchcontrol...... : while에서 True/False 조건을 위해 bool값을 갖는 변수
# gold............... : 용사가 소지한 금액을 갖는 변수
# satiety............ : 포만감을 나타내는 변수
# healthpoint........ : 용사의 체력지수를 나타내는 변수
# level.............. : 용사의 레벨을 나타내는 변수
# select............. : 사용자가 입력한 값을 받는 변수
# stage.............. : 행동에 따른 스테이지를 위한 변수


print('[전략게임 : 용사의 마왕 공략]\n  게임 규칙:\n    (1) 포만감, 체력이 0이 되면 용사는 모험을 포기한다.\n    (2) Lv 15를 달성하면, 마왕 공략에 성공하여 용사의 모험이 성공적으로 막을 내린다.\n    (3) 50단계를 넘길 경우, 마왕이 세계 정복에 성공하여 용사의 모험이 끝난다.')

name = input('용사의 이름을 입력하세요: ')

switchcontrol = True
gold = 1000
satiety = 10
healthpoint = 10
level = 1
select = 0
stage = 1

while switchcontrol:
    print('### 용사 {}의 스테이터스 ###\n포만감 : {}\n체력 : {}\nLevel : {}\n골드 : {}\n스테이지 : {}\n용사에게 어떤 명령을 내릴까요?\n1 - 음식 섭취\n2 - 놀기\n3 - 잠자기\n4 - 아르바이트\n5 - 던전'.format(name, satiety, healthpoint, level, gold, stage))
    select = input('번호를 입력하세요 => ')
    if select == '1':
        if gold >= 200:
            print('맛있는 음식을 먹은 용사는 포만감이 1 증가했습니다. 200골드를 음식값으로 소비했습니다.\n')
            satiety += 1
            gold -= 200
            stage += 1
        else:
            print('200골드 이상을 소지하고 있지 않아, 음식을 살 수 없습니다.\n')
            stage += 1
    elif select == '2':
        print('강아지와 뛰어 놀며 재미있게 놀았습니다. 운동으로 인해 포만감과 체력이 1 감소합니다.\n')
        satiety -= 1
        healthpoint -= 1
        stage += 1
    elif select == '3':
        print('용사는 잠을 청합니다. 충분한 휴식으로 인해 체력이 1 증가하였습니다.\n')
        healthpoint += 1
        stage += 1
    elif select == '4':
        print('용사는 음식점에서 아르바이트를 했습니다. 일당 600골드를 획득하였으나, 피로로 인해 체력이 1 감소합니다.\n')
        gold += 600
        healthpoint -= 1
        stage += 1
    elif select == '5':
        print('용사는 던전에서 몬스터들을 물리쳤습니다. 레벨이 1 증가하며, 포만감과 체력이 1 감소합니다.\n')
        level += 1
        healthpoint -= 1
        satiety -= 1
        stage += 1
    else:
        print('번호가 잘못 입력되었습니다. 올바른 번호를 입력해 주세요.\n')
    
    if stage >= 50:
        print('### 용사 {}의 스테이터스 ###\n포만감 : {}\n체력 : {}\nLevel : {}\n골드 : {}\n스테이지 : {}\n용사에게 어떤 명령을 내릴까요?\n1 - 음식 섭취\n2 - 놀기\n3 - 잠자기\n4 - 아르바이트\n5 - 던전'.format(name, satiety, healthpoint, level, gold, stage))
        print('50단계 동안 마왕을 공략하지 못해, 세계는 마왕의 손에 정복되었습니다.\n')
        switchcontrol = False
        
    elif level >= 15:
        print('### 용사 {}의 스테이터스 ###\n포만감 : {}\n체력 : {}\nLevel : {}\n골드 : {}\n스테이지 : {}\n용사에게 어떤 명령을 내릴까요?\n1 - 음식 섭취\n2 - 놀기\n3 - 잠자기\n4 - 아르바이트\n5 - 던전'.format(name, satiety, healthpoint, level, gold, stage))
        print('레벨 15 달성. 마왕 공략에 성공하여 세계를 구하였습니다.\n')
        switchcontrol = False
        
    elif satiety == 0:
        print('### 용사 {}의 스테이터스 ###\n포만감 : {}\n체력 : {}\nLevel : {}\n골드 : {}\n스테이지 : {}\n용사에게 어떤 명령을 내릴까요?\n1 - 음식 섭취\n2 - 놀기\n3 - 잠자기\n4 - 아르바이트\n5 - 던전'.format(name, satiety, healthpoint, level, gold, stage))
        print('용사가 배고픔을 견디지 못해 모험을 포기했습니다.\n')
        switchcontrol = False
        
    elif healthpoint == 0:
        print('### 용사 {}의 스테이터스 ###\n포만감 : {}\n체력 : {}\nLevel : {}\n골드 : {}\n스테이지 : {}\n용사에게 어떤 명령을 내릴까요?\n1 - 음식 섭취\n2 - 놀기\n3 - 잠자기\n4 - 아르바이트\n5 - 던전'.format(name, satiety, healthpoint, level, gold, stage))
        print('체력을 다한 용사는 나무에 기대어 조용히 숨을 거두었습니다.\n')
        switchcontrol = False
        