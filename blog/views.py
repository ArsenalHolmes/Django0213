

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    '''
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页',
                      'welcome': '欢迎访问我的博客首页'
                  })
    '''

    post_list = Post.objects.all().order_by('-created_time')#order_by 排序  依据是created_time 默认从远到近 加“-” 倒置
    return render(request, 'blog/index.html', context={'post_list': post_list})