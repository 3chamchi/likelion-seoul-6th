# Generated by Django 3.2.7 on 2021-09-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(verbose_name='작성일')),
                ('created_by', models.CharField(max_length=100, verbose_name='작성자')),
                ('is_view', models.BooleanField(default=True, verbose_name='공개 여부')),
            ],
        ),
    ]
