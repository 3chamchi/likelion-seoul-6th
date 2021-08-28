add_count = 0  # 전역 변수

def add(num1, num2):  # num1, num2 지역 변수
    global add_count  # 전역 변수
    add_count += 1
    result = num1 + num2
    return result  # result 지역 변수

add(1,3)
print(add_count)

# def add(num1, num2):  # num1, num2 지역 변수
#     global add_count
#     add_count += 1

#     result = num1 + num2
#     return result  # result 지역 변수

class Add():
    def __init__(self) -> None:
        pass

    def add(self, num1, num2):
        result = num1 + num2
        return result

add_class = Add()
add_class.add(3, 5)
print(add_count)


print('add_count' in locals())  # 전역 변수 확인
print('add_count' in globals())  # 지역 변수 확인