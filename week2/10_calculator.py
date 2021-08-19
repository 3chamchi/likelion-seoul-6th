# 실습1 파이썬 계산기 만들기

# 프로그램 시나리오
# 1. 사용자에게 프로그램 설명을 한다. 사용방법 등
# 2. 기능을 입력 받는다. 더하기, 빼기, 곱하기, 나누기
# 3. 계산할 숫자 두개를 입력 받는다.
# 4. 계산 한 결과값을 출력한다.

print('[멋쟁이 사자처럼 계산기]')
print('\n원하는 기능을 입력 후 계산할 두 숫자를 입력해주세요.')
print('''
기능 목록
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
''')

action = int(input('기능을 입력하세요: '))

num1 = int(input('첫 번째 숫자를 입력하세요: '))
num2 = int(input('두 번째 숫자를 입력하세요: '))

if action == 1:
    pass

if action == 1:
    result = num1 + num2
    print(num1, ' + ', num2, ' = ', result)
elif action == 2:
    result = num1 - num2
    print(num1, ' - ', num2, ' = ', result)
elif action == 3:
    result = num1 * num2
    print(num1, ' x ', num2, ' = ', result)
elif action == 4:
    result = num1 / num2
    print(num1, ' / ', num2, ' = ', result)
else:
    print('잘못된 기능입니다.')
