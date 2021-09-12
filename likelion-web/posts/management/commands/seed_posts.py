from django.core.management.base import BaseCommand
from django_seed import Seed

from posts.models import Post


class Command(BaseCommand):
    help = '이 커맨드를 통해 랜덤한 테스트 게시글 데이터를 만듭니다.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=10,
            type=int,
            help='만들고자하는 게시글의 수를 입력하세요.'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder(locale='ko-kr')
        seeder.add_entity(Post, number,)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number}개의 게시글이 작성되었습니다.'))
