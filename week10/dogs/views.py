import requests

from django.shortcuts import render

from .models import DogImage

def index(reqeust):
    # 강아지 이미지 랜덤으로 가져오기
    # API 요청
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    r_json = r.json()
    # 데이터 추출
    # message = 'https://images.dog.ceo/breeds/terrier-border/n02093754_7297.jpg'
    message = r_json['message']
    status = r_json['status']

    # API로 수신한 데이터 모델 저장
    dog_image, created = DogImage.objects.get_or_create(
        url=message,
        defaults={'url': message}
    )
    print(f'{dog_image} - {created}')
    print(dog_image.url)

    context = {
        'image_url': message
    }
    # 응답
    return render(reqeust, 'index.html', context)