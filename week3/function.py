### 함수(function) 실습

def add(num1, num2):
    result = num1 + num2
    return result

result = add(2, 5)
print(result)


### 내장 함수

# 숫자의 절댓값을 돌려줍니다.
num1 = 100
num2 = -40
print('num1 =', abs(num1))
print('num2 =', abs(num2))

# 객체의 《아이덴티티》를 돌려준다
var = 'str'
var1 = 'str'
var2 = 4
print('var = ', id(var))
print('var1 = ', id(var1))
print('var2 = ', id(var2))

user_list = [1, 2]
user_name = 'likelion'
print('id(user_list) = ', id(user_list))
print('id(user_name) = ', id(user_name))
user_list.append(5)
user_name += 'G'
print('id(user_list) = ', id(user_list))
print('id(user_name) = ', id(user_name))

item1 = ['a', 2, 9.6]
item2 = ['a', 2, 9.6]
print('id(item1) = ', id(item1), item1)
print('id(item2) = ', id(item2), item2)
item1.append(99)
item2.append('a')
print('id(item1) = ', id(item1), item1)
print('id(item2) = ', id(item2), item2)
# iterable 의 항목들로 새 정렬된 리스트를 돌려줍니다.
user_id_list = [7, 1, 2, 4, 7, 8, 4, 5, 6]
print(user_id_list)
print(sorted(user_id_list))
print(sorted(user_id_list, reverse=True))

# start 및 iterable 의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 돌려줍니다.
number_list = [10, 40, 20, 30]
print(sum(number_list))

# 범위 생성자에 대해 인자는 정수여야 합니다
print(range(10))
print(list(range(10)))
print(list(range(0, 10, 3)))
print(list(range(5, 10)))

# function 이 참을 돌려주는 iterable 의 요소들로 이터레이터를 구축합니다.
number_list = list(range(10))
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number_even_list = list(filter(is_even, number_list))
print(number_list)
print(number_even_list)

# 객체의 길이 (항목 수)를 돌려줍니다. 
text = '12345678910'
user_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(text))
print(len(user_id_list))

# object 의 형을 돌려줍니다.
text = 'abc'
number_float = 1.1
number_int = 1
list_type = [1,2,3]
tuple_type = (1, 2, 3)
dict_type = {'key': 'value'}
print('text type = ', type(text))
print('number_float type = ', type(number_float))
print('number_int type = ', type(number_int))
print('list_type type = ', type(list_type))
print('tuple_type type = ', type(tuple_type))
print('dict_type type = ', type(dict_type))

# iterable 에서 가장 큰 항목이나 두 개 이상의 인자 중 가장 큰 것을 돌려줍니다.
number_list = [4, 2, 10, 5, 9, 20]
print(max(number_list))

# iterable 에서 가장 작은 항목이나 두 개 이상의 인자 중 가장 작은 것을 돌려줍니다.
print(min(number_list))


### 외장 함수
from datetime import datetime
print(datetime.now())

import random
print(random.randrange(100))
print(random.choice(['a', 2, 'AAA', 100]))