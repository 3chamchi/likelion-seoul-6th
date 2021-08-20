# 실습1 파이썬 계산기 만들기

# 프로그램 시나리오
# 1. 사용자에게 프로그램 설명을 한다. 사용방법 등
# 2. 기능을 입력 받는다. 더하기, 빼기, 곱하기, 나누기
# 3. 계산할 숫자 두개를 입력 받는다.
# 4. 계산 한 결과값을 출력한다.

print('[멋쟁이 사자처럼 계산기]')  # 계산기 이름 출력
print('\n원하는 기능을 입력 후 계산할 두 숫자를 입력해주세요.')  # 사용자에게 사용법 출력
print('''
기능 목록
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 종료
''')

action = int(input('기능을 입력하세요: '))  # 사용자가 원하는 기능 입력 받기, int()은 추후 기능 조건 확인을 위해 사용 >> input 입력값은 str 형태이므로 int형태로 변경

num1 = int(input('첫 번째 숫자를 입력하세요: '))  # 사용자가 입력한 첫 번째 숫자 입력 받기
num2 = int(input('두 번째 숫자를 입력하세요: '))  # 사용자가 입력한 두 번째 숫자 입력 받기

if action == 5:  # 종료 조건 확인 
    exit()  # exit() 프로그램을 종료 시키는 함수

if action == 1:  # 더하기 조건 확인
    result = num1 + num2  # 더하기
    print(num1, ' + ', num2, ' = ', result)
elif action == 2:  # 빼기 조건 확인
    result = num1 - num2  # 빼기
    print(num1, ' - ', num2, ' = ', result)
elif action == 3:  # 곱하기 조건 확인
    result = num1 * num2  # 곱하기
    print(num1, ' x ', num2, ' = ', result)
elif action == 4:  # 나누기 조건 확인
    result = num1 / num2  # 나누기
    print(num1, ' / ', num2, ' = ', result)
else:  # 1, 2, 3, 4, 5 기능 외 예외처리
    print('잘못된 기능입니다.')
