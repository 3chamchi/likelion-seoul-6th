### 제어문
### if
#if - 1
print('if - 1')
animal = '사자'
if animal == '사자':
    print('사자입니다.')

#if - 2
print('if - 2')
age = 21
if age < 20:
    print('청소년입니다.')
else:
    print('성인입니다.')

#if - 3
print('if - 3')
score = 99
if score < 60:
    print('E 학점')
elif score < 70:
    print('D 학점')
elif score < 80:
    print('C 학점')
elif score < 90:
    print('B 학점')
elif score < 100:
    print('A 학점')
else:
    print('ERROR')


### for

#for - 1
print('for - 1')
number_list = [1, 2, 3, 4, 5]
for number in number_list:
    print(number)

#for - 2
print('for - 2')
for index in range(10):
    print(number)


### while

#while - 1
print('while - 1')
index = 0
while index < 10:
    index = index + 1
    print(index)

#while - 2
print('while - 2')
count = 0
while True:
    if count > 10:
        break
    count = count + 1
    print(count)