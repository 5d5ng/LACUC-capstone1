from django.db import models

# Create your models here.


class Sampleuser(models.Model):
    username = models.CharField(max_length=60, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    Preferred_Place = models.CharField(max_length=60, verbose_name='선호장소')
    Preferred_group = models.CharField(max_length=60, verbose_name='동행')

    Preferred_Style = models.CharField(max_length=60, verbose_name='여행스타일')
    Preferred_Accomodation = models.CharField(
        max_length=60, verbose_name='선호숙박시설')
    Preferred_term = models.CharField(max_length=60, verbose_name='여행기간')
    Best_Place = models.CharField(max_length=60, verbose_name='가장 좋았던 곳')

    # verbose_name을 지정함으로써 패스명 다른글자가 뜨지않고 사용자명,비밀번호,등록시간이 뜬다
    # 데이터베이스에 테이블명을 지정하고싶을때 아래와 같이 테이블 생성

    # 파이썬의 클래스는 호출시 문자열을 반환하는데 이떄 유저네임을 반환함으로서 보기쉽게한다

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'sample_sampleuser'
        verbose_name = '테스트 사용자'
        verbose_name_plural = '테스트 사용자'
