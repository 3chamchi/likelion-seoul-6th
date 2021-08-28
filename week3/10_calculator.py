import time
from datetime import datetime

# https://docs.python.org/ko/3/library/functions.html#eval
# https://docs.python.org/ko/3/library/datetime.html

class Log:
    """ 계산 기록 로그 클래스 """
    count = 0
    def __init__(self, formula, reuslt):
        """ formula : 계산 내역, reuslt : 결과값, created_at : 생성 일시 """
        self.formula = formula
        self.reuslt = reuslt
        self.created_at = datetime.now()
        Log.count += 1
        print(f'[{datetime.now()}]- Log.__init__() : {self}')
    
    def __del__(self):
        Log.count -= 1
        print(f'[{datetime.now()}]- Log.__del__() : {self}')

    def __str__(self) -> str:
        return f'[{self.created_at}] {self.formula} = {self.reuslt}'


class Calculator():
    """ 계산기 클래스 """
    def __init__(self):
        """ 계산기 생성시 값 초기화 """
        self.log = list()

    def remove(self):
        """ 가장 오래된 계산 기록 삭제 """
        if len(self.log) > 0:
            del self.log[0]

    def clear(self):
        """ 계산기록 모두 삭제 """
        self.log.clear()

    def history(self):
        """ 계산기록 모두 출력 """
        for item in self.log[::-1]:
            print(item)

    def eval(self, formula):
        """ 입력 그대로 계산 """
        reuslt = eval(formula)
        log = Log(formula, reuslt)

        self.log.append(log)
        return reuslt

calculator = Calculator()
calculator.eval('1+2-3')
calculator.eval('4*2-5')
calculator.eval('10//2*5')
calculator.history()
calculator.remove()
calculator.history()
calculator.clear()
calculator.history()

