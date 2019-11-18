from django.shortcuts import render
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_write(request):
    form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    boards = Board.objects.all().order_by('-id')   # 시간 역순으로 모든 게시글을 가져옴
    return render(request, 'board_list.html', {'boards': boards})  # 템플릿으로 전달
