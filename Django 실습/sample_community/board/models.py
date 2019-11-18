from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('sampleuser.Sampleuser', on_delete=models.CASCADE,
                               verbose_name='작성자')

    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    # verbose_name을 지정함으로써 패스명 다른글자가 뜨지않고 사용자명,비밀번호,등록시간이 뜬다
    # 데이터베이스에 테이블명을 지정하고싶을때 아래와 같이 테이블 생성

    # 파이썬의 클래스는 호출시 문자열을 반환하는데 이떄 유저네임을 반환함으로서 보기쉽게한다
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sample_board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
