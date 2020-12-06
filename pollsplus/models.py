from django.db import models


class Post(models.Model):
    # id : 자동 생성
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='published date')
    writer = models.CharField(max_length=20)    # 로그인 된 정보를 가져와야 할듯
    contents_text = models.TextField()  # TextField : 다중 행 크기 조절 가능 입력, CharField : 단일 라인 입력


class Comment(models.Model):
    # id : 자동 생성
    # FK는 항상 다른 테이블의 PK로 연결되므로 클래스만 지정하면 됨
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.CharField(max_length=20)
    contents_text = models.TextField()

