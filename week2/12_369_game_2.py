# 실습3 파이썬 369게임 만들기
# 주제 : 반복문, 제어문

# 프로그램 시나리오
# 1. 프로그램 및 사용방법 설명
# 2. 사용자에게 1부터 x까지 출력할 x값 입력받기
# 3. 1부터 x까지 출력, 단 [3, 6, 9] 중 하나의 값이 있다면 별표(*) 출력

print('369 게임 원하는 숫자를 입력하세요.')

# result = [] # 위 코드와 동일
result = list()  # 빈 list 자료형 변수 생성 방법

number = int(input('숫자 입력 : '))
'3' in '33'
start_count = 0
for index in range(1, number + 1):
    if '3' in str(index):
        start_count = start_count + 1
        result.append('*')
    elif '6' in str(index):
        start_count = start_count + 1
        result.append('*')
    elif '9' in str(index):
        start_count = start_count + 1
        result.append('*')
    else:
        result.append(index)

# [1,2,3,4,5,6,7,8,9]
# print_count = 1
print_count = 0
for num in result:
    if print_count % 9 == 0:
        print(num)
        # print(num, end='\n')
    else:
        print(num, end=', ')
    print_count = print_count + 1

print('별이 찍힌 횟수 : ', start_count)

    # if '3' in str(index) or '6' in str(index) or '9' in str(index):
    #     result.append('*')  # list 자료형의 append()는 값을 추가하는 방법
    # else:
    #     result.append(index)
# print(result)  # 변수값 확인 부분

# 출력 부분
# for index in range(len(result)):
#     if index == len(result) - 1:
#         print(result[index], end='')  # print 기능의 end 속성은 출력 후 붙일 문자열 입력 기본값 '\n'
#     elif index % 9 == 0 and index != 0:
#         print(result[index], end='\n')
#     else:
#         print(result[index], end=', ')