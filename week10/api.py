import requests

# API 요청
r = requests.get('https://dog.ceo/api/breeds/image/random')

# print(type(r))
# print(r.text)
# print(r.json())

# reqeusts 자료형 확인
print(type(r.text))
print(type(r.json()))
r_json = r.json()

# 데이터 추출
message = r_json['message']
status = r_json['status']
print(message)
print(status)
