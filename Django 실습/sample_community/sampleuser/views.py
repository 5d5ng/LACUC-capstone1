
from .models import Sampleuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import LoginForm
# make_password,check_password함수사용을위해 선언
# Create your views here.


def login(request):
 # form 에 만들어놓은 로그인 폼을 가져와서 사용
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # session
            request.session['user'] = form.user_id
            return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    user_id = request.session.get('user')  # session에서 아이디를 뺴옴
    #  로그인 할때 session에 넣었던 키가 id값이므로user

    if user_id:
        sampleuser = Sampleuser.objects.get(pk=user_id)  # pk는 기본키
        return HttpResponse(sampleuser.username)
    return HttpResponse('Home!')


def logout(request):  # 로그아웃 기능
    if request.session.get('user'):  # 값이 있다면 이프문 통과
        del(request.session['user'])  # 세션에서 삭제

    return redirect('/')  # 홈으로 이동


def register(request):
    if request.method == 'GET':  # 주소를 치고 들어갔을때의 경우
        return render(request, 'register.html')
    elif request.method == 'POST':  # 등록을 눌렀을때의 액션
        username = request.POST.get('username', None)  # 초기값 None으로 설정
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        Preferred_Place = request.POST.get('Preferred_Place', None)
        Preferred_group = request.POST.get('Preferred_group', None)
        Preferred_Style = request.POST.get('Preferred_Style', None)
        Preferred_Accomodation = request.POST.get(
            'Preferred_Accomodation', None)
        Preferred_term = request.POST.get('Preferred_term', None)
        Best_Place = request.POST.get('Best_Place', None)

        res_data = {}  # 에러를 받을 딕셔너리 만들어줌
        if not(username and useremail and password and re_password and Preferred_Place
               and Preferred_group and Preferred_Style and Preferred_term and Best_Place and Preferred_Accomodation):  # 값이 다들어있지않는경우
            res_data['error'] = '모든 값을 가지지않았습니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:

            sampleuser = Sampleuser(
                username=username,
                useremail=useremail,
                password=make_password(password),  # 암호화 후 저장
                Preferred_Place=Preferred_Place,
                Preferred_group=Preferred_group,
                Preferred_Style=Preferred_Style,
                Preferred_Accomodation=Preferred_Accomodation,
                Preferred_term=Preferred_term,
                Best_Place=Best_Place
            )
            sampleuser.save()
        # 데이터 포스트를 하고 다시 html페이지를반환

        return render(request, 'register.html', res_data)
        # res_data를 줘야 에러메시지 출력됨
    # 리퀘스트와 반환하고싶은 html파일 리턴
