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

    def __len_log(self):
        return len(self.log)

    def remove(self):
        """ 가장 오래된 계산 기록 삭제 """
        if self.__len_log() > 0:
            temp = self.log[0]
            del self.log[0]
            return temp
        else:
            return False

    def clear(self):
        """ 계산기록 모두 삭제 """
        if self.__len_log() > 0:
            self.log.clear()
            return True
        else:
            return False

    def history(self):
        """ 계산기록 모두 출력 """
        if self.__len_log() > 0:
            for item in self.log[::-1]:
                print(item)
            return True
        else:
            return False

    def eval(self, formula):
        """ 입력 그대로 계산 """
        reuslt = eval(formula)
        log = Log(formula, reuslt)

        self.log.append(log)
        return reuslt

# calculator = Calculator()
# calculator.eval('1+2-3')
# calculator.eval('4*2-5')
# calculator.eval('10//2*5')
# calculator.history()
# calculator.remove()
# calculator.history()
# calculator.clear()
# calculator.history()

if __name__ == '__main__':
    calculator = Calculator()

    while True:
        print('''[멋쟁이 사자처럼] 클래스 계산기
    사용방법
    1. 계산하기
        > 계산 가능 연산자 +, -, *, /, //, %
        > 입력 예시) 100-20 or 100*20/10
    2. 계산기 기록 확인
    3. 기록 삭제 - 가장 오래된 기록
    4. 기록 삭제 - 전체

    q 또는 Q를 입력하시면 계산기가 종료됩니다.
    ''')
        action = input('기능을 입력해주세요. : ')
        
        if action in ['q', 'Q']:
            break

        if action == '1':
            data = input('계산하고싶은 수식을 입력해주세요 : ')
            result = calculator.eval(data)
            print(result)
        elif action == '2':
            result = calculator.history()
            if not result:
                print('계산 기록이 없습니다.')
            else:
                time.sleep(3)
        elif action == '3':
            result = calculator.remove()
            if result:
                print(result)
            else:
                print('계산 기록이 없습니다.')
        elif action == '4':
            result = calculator.clear()
            if result:
                print('계산 기록을 모두 삭제하였습니다.')
            else:
                print('계산 기록이 없습니다.')
        print('\n')

    print('멋쟁이사자처럼 클래스 계산기를 이용해주세셔 감사합니다.')


