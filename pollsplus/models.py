import string
from random import choice
from django.db import models

def user_path(instance, filename):
  pid = ''.join([choice(string.ascii_letters) for _ in range(8)])
  extension = filename.split('.')[-1]
  return f'{pid}.{extension}'
  
class Post(models.Model):
    # id : 자동 생성
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='published date', auto_now_add=True)   # 자동으로 현재 시간 입력
    writer = models.CharField(max_length=20)    # 로그인 된 정보를 가져와야 할듯
    contents_text = models.TextField()  # TextField : 다중 행 크기 조절 가능 입력, CharField : 단일 라인 입력
    file = models.ImageField(upload_to=user_path)

    def __str__(self):
        return self.title_text


class Comment(models.Model):
    # id : 자동 생성
    # FK는 항상 다른 테이블의 PK로 연결되므로 클래스만 지정하면 됨
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name='published date', auto_now_add=True)
    writer = models.CharField(max_length=20)
    contents_text = models.TextField()

    def __str__(self):
        return self.contents_text
