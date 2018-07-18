boolll = True

while boolll:
    try:
        i = int(input('임의의 양의 정수를 입력하세요:'))
        if type(i) == int and i > 1:
            boolll = False
            for div in range(2, i+1):
                if int(i%div) == 0:
                    if i == div:
                        print('이 숫자는 소수입니다.')
                        break
                    else:
                        print('{}x{}={}'.format(div, int(i/div), int(i)))
                        print('이 숫자는 {}로 나누어지므로 소수가 아닙니다.'.format(div))
                        break
        else:
            raise ValueError
    except ValueError:
        print('ValueError: 1보다 큰 양의 정수를 입력하세요.')