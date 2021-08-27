# 실습4 파이썬 자판기 만들기
# 주제 : 반복문, 제어문

# • 돈을넣은후커피를구매할수있는자판기개발
# • 입력값:돈
# • 출력 값 : 커피 출력 문구, 거스름돈, 예) 커피입니다! 거스름돈 0000원

# # 프로그램 시나리오
# # 1. 프로그램 및 사용방법 설명
# # 2. 사용자 현금 입력받기
# # 3. 상품, 반환 현금 출력

# # 1. 프로그램 및 사용방법 설명
# print('[멋쟁이사자처럼] 커피 자판기')
# print('''=======사용법=======
# 순서 : 현금 투입 -> 상품, 거스름돈 출력
# ''')

# item = {
#     'name' : '믹스커피',
#     'price' : 600
# }

# # 2. 사용자 현금 입력받기
# num = int(input('커피 구매를 위해 현금을 투입해주세요 : '))

# # 3. 상품, 반환 현금 출력
# name = item['name']
# result_num = num - item['price']
# print(name, result_num)

# 프로그램 시나리오
# 1. 프로그램 및 사용방법 설명
# 2. 사용자 현금 입력받기
# 3. 상품, 반환 현금 출력

# 1. 프로그램 및 사용방법 설명
print('[멋쟁이사자처럼] 커피 자판기')
print('''=======사용법=======
순서 : 현금 투입 -> 상품 선택 -> 상품, 거스름돈 출력

[번호 - 이름 - 금액]
1. 믹스커피 600
2. 차가운 아메리카노 1500
3. 따뜻한 아메리카노 1000
 ''')

items_dict = {
    '1' : {
        'name' : '믹스커피',
        'price' : 600,
        'stock' : 10
    },
    '2' : {
        'name' : '차가운 아메리카노',
        'price' : 1500,
        'stock' : 10
    },
    '3' : {
        'name' : '따뜻한 아메리카노',
        'price' : 1000,
        'stock' : 10
    }
}
while True:
    # 2. 사용자 현금 입력받기
    num = int(input('커피 구매를 위해 현금을 투입해주세요 : '))
    item, su = input('구매하고자 하는 상품과 수량을 입력해주세요 : ').split(' ')
    su = int(su)

    # 3. 상품, 반환 현금 출력
    stock = items_dict[item]['stock']
    if stock >= su:
        name = items_dict[item]['name']
        result_num = num - (items_dict[item]['price'] * su)
        print(name, su, '개', result_num)

        items_dict[item]['stock'] -= su
    else:
        print('해당 상품의 재고가 부족합니다.')