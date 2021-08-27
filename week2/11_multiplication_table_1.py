# 실습2 파이썬 구구단 만들기
# 주제 : 반복문

# 프로그램 시나리오
# 1. 구구단 안내
# 2. 출력할 구구단 입력 받기, 숫자
# 3. 출력할 구구단의 곱(열수) 입력 받기, 숫자
# 4. 입력 받은 단을 반복하여 1~입력값 곱까지 출력, 예) 2x1-2 ~ 2x입력 곱
# 5. 프로그램을 종료할 것인지 확인 후 종료 또는 반복

while True:
    # 1. 구구단 안내
    title = '[멋쟁이사자처럼]구구단 출력기'
    print(title)

    # 2. 출력할 구구단 입력 받기, 숫자
    dan = input('출력하고자하는 단을 입력해주세요. 숫자만 입력 가능합니다 : ')
    dan = int(dan)

    # 3. 출력할 구구단의 곱(열수) 입력 받기, 숫자
    num = input('출력하고자하는 곱을 입력해주세요. 숫자만 입력 가능합니다 : ')
    num = int(num)

    # 4. 입력 받은 단을 반복하여 1~입력값 곱까지 출력, 예) 2x1-2 ~ 2x입력 곱
    for index in range(1, num+1):
        result = dan * index
        print(dan, 'x', index, '=', result)

    # 5. 프로그램을 종료할 것인지 확인 후 종료 또는 반복
    result = input('다른 단을 출력하려면 Y, 종료하려면 Q를 입력해주세요 :')
    if result in ['y', 'Y']:
        pass
    elif result in ['q', 'Q']:
        break
print('멋쟁이사자처럼 계산기를 이용해주셔서 감사합니다.')
    # for index in range(1,10):
    #     result = dan * index
    #     print(dan, 'x', index, '=', result)