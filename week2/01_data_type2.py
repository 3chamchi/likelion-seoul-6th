# 주석 단축키 주석할 부분 드래그 후 컨트롤(커멘드) + /
###int
print('###int')
number = int()
number_1 = 50
number_2 = 10
number_3 = 3
print(number)
print(number_1)
print(number_2)

print('int 연산')
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_3)
print(number_1 // number_3)
print(number_1 % number_3)
print(number_2 ** number_3)

###float
print('###float')
real_number = float()
real_number1 = 30.3
real_number2 = 20.7
real_number3 = 3.1

print('float 연산')
print(real_number1 + real_number2)
print(real_number1 - real_number2)
print(real_number1 * real_number2)
print(real_number1 / real_number2)
print(real_number1 // real_number3)
print(real_number1 % real_number3)
print(real_number3 ** real_number3)

###str
print('###str')
text = str()
likelion = '멋쟁이사자처럼'
likelion2 = "멋쟁이사자처럼"
likelion3 = '''멋쟁이사자처럼
줄바꿈 자동 적용
'''
likelion4 = """멋쟁이사자처럼
줄바꿈 자동 적용
"""
print(text)
print(likelion)
print(likelion2)
print(likelion3)
print(likelion4)

print('str 연산')
print(likelion + likelion)
print(likelion * 3)

print('str 슬라이싱')
print(likelion[3])
print(likelion[1:3])
print(likelion[5:7])
print(likelion[3:])
print(likelion[:3])
print(likelion[-4])

###bool
print('###bool')
is_likelion = True
is_computer = False
print(is_likelion)
print(is_computer)

# 논리 연산자
print(not is_likelion)
print(is_likelion and is_computer)
print(is_likelion or is_computer)

###list
print('###list')
item_list = list()
item_list2 = []
item_list3 = [1, 'text', False]
item_list4 = [1, 3, 5, 4, 2]

print(item_list)
print(item_list2)
print(item_list3)

print('list 연산')
print(item_list3 + item_list4)

print('list 기능')
item_list4.append(5)
print(item_list4)
item_list4.pop()
print(item_list4)

print('list 슬라이싱')
print(item_list4[3])
print(item_list4[2:3])
print(item_list4[:3])
print(item_list4[3:])
print(item_list4[-1])


###tuple
print('###tuple')
item_tuple = tuple()
item_tuple2 = (0, )
item_tuple3 = ('name','age','phone', 'birthday')

print(item_tuple)
print(item_tuple2)
print(item_tuple3)

print('list 슬라이싱')
print(item_tuple3[2])
print(item_tuple3[:3])
print(item_tuple3[3:])
print(item_tuple3[-2])

###dict
print('###dict')
user_dict = dict()
user_dict2 = {}
user_dict3 = {
    'key' : 'value',
    'user' : {
        'name': 'likelion',
        'age' : 6
    }
}

print(user_dict)
print(user_dict2)
print(user_dict3)

user_dict2[3] = 'add 3'
user_dict2['title'] = '멋쟁이사자처럼 직장인'
print(user_dict2)

print('dict 사용')
print(user_dict3['key'])
print(user_dict3.get('key'))
print(user_dict3['user'])
print(user_dict3['user']['name'])