# 공식문서 : https://docs.python.org/ko/3/tutorial/inputoutput.html#fancier-output-formatting
title = '멋쟁이사자처럼 직장인 서울 6기'
desciption = '12주 나의 아이디어를 만들어보세요!'
teacher = '이동원'

print('산술 연산자 사용')
print(title + ' ' + teacher)
print()

print('콤마(,) 사용')
print(title, teacher)
print()

print('format() 사용')
print('{} {}'.format(title, teacher))
print('{1} {0}'.format(title, teacher))
print()

print('f-string 사용 - 권장')
print(f'{title} {teacher}')
print()