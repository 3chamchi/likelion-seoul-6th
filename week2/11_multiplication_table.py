# 실습2 파이썬 구구단 만들기
# 주제 : 반복문

# 프로그램 시나리오
# 1. 구구단 안내
# 2. 출력할 구구단 입력 받기, 숫자
# 3. 입력 받은 단을 반복하여 1~9까지 출력, 예) 2x1-2 ~ 2x9=18

title = '[멋쟁이사자처럼]구구단 출력기'
print(title)
dan = input('출력하고자하는 단을 입력해주세요. 숫자만 입력 가능합니다 : ')
dan = int(dan)

for index in [1,2,3,4,5,6,7,8,9]:
    result = dan * index
    print(dan, 'x', index, '=', result)

# for index in range(1,10):
#     result = dan * index
#     print(dan, 'x', index, '=', result)