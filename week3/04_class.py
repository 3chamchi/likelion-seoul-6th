class Person(object):
    def __init__(self, name, age, money):
        # print('Person.__init__()')
        self.name = name
        self.age = age
        self.money = money

    def hello(self):
        """ 인사 """
        pass

    def how_much(self):
        """ 금액 출력 """
        pass


class Korean(Person):
    def hello(self):
        print('안녕하세요')


class American(Person):
    def hello(self):
        print('Hello')


korean = Korean('민국이', 3, 3000)
korean.hello()

american = American('마이클', 23, 200000)
american.hello()


class Country():
    country = None
    language = None
    currency = None
    population = 0

    def __init__(self) -> None:
        Country.population += 1

    @staticmethod
    def current_population():
        return Country.population


class Korean(Person, Country):
    country = '한국'
    language = '한국어'
    currency = '₩'

    def __init__(self, name, age, money):
        Person.__init__(self, name, age, money)
        Country.__init__(self)

    def how_much(self):
        return self.currency, self.money


class American(Person, Country):
    country = '미국'
    language = '영어'
    currency = '$'

    def __init__(self, name, age, money):
        Person.__init__(self, name, age, money)
        Country.__init__(self)

    def how_much(self):
        return self.currency, self.money


korean = Korean('민국이', 3, 3000)
print(korean.name)
print(korean.age)
print(korean.money)
print(korean.country)
print(korean.language)
print(korean.currency)
print(korean.how_much())
print(korean.current_population())

american = American('마이클', 23, 200000)
print(american.name)
print(american.age)
print(american.money)
print(american.country)
print(american.language)
print(american.currency)
print(american.how_much())
print(american.current_population())

korean_list = list()
for index in range(10):
    korean = Korean(f'민국이-{index}', 3 + index, 3000 * index)
    korean_list.append(korean)

print(Country.current_population())
