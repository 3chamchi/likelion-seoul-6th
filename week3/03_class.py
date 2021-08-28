class 클래스명:
    pass


class Person:
    pass


class Person():
    pass


class Person(object):
    pass


class Person:
    year = 2021
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name, '달린다.')

    def sleep(self):
        print(self.name, '자다.')


dongwon = Person('이동원', 16)
dongwon.name
dongwon.age
dongwon.run()
dongwon.sleep()

gildong = Person('홍길동', 99)
gildong.name
gildong.age
gildong.run()
gildong.sleep()