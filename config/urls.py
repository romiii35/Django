"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render, redirect

movie_list = [
    {'title' : '명탐정 코난', 'director' : '시게하라 카츠야'},
    {'title' : '귀멸의 칼날', 'director' : '소토자키 하루오'},
    {'title' : '케이팝 데몬 헌터스', 'director' : '매기 강'},
    {'title' : '괴수 9호', 'director' : '미야 시게유키'},
]
def index(request):
    return HttpResponse("<h1>hello</h1>")

def book_list(request):
    # book_text = ''
    #
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'

    return render(request, 'book_list.html', {'range' : range(0, 10)})
def book(request, num):
    return render(request, 'book_detail.html', {'num' : num})

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지 입니다.</h1>')
def python(request):
    return HttpResponse('python 페이지 입니다.')

def movies(request):
    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie['title']}</a><br>'
    #     for index, movie in enumerate(movie_list)]
    #
    # movie_titles =[]
    # for movie in movie_list:
    #     movie_titles.append(movie['title'])
    #
    # response_text = ''
    #
    # for index, title in enumerate(movie_titles):
    #     response_text += f'<a href="/movie/{index}/">{title}</a><br>'
    #
    # return HttpResponse(response_text)

    return render(request, template_name= 'movies.html', context={'movie_list': movie_list})
def movie_detail(request, index):
    if index > len(movie_list) -1:
        raise Http404
    # from django.http import Http404
    # raise Htto404 표시를 안해줬을때, 그 페이지에서 나오는거는 500번대 error = 서버측 에러
    # 위 표시를 해줘서 (400번대 에러) 유저측 에러를 발생하자

    # response_text = f'<h1>{movie["title"]}</h1> <p>감독 : {movie["director"]}</p>'
    movie = movie_list[index]
    context = {'movie' : movie}
    return render(request, 'movie.html', context)

def gugu(request, num):
    if num < 2:
        return redirect('/gugu/2/')
    context = {
        'num' : num,
        # 'results' : [(i, num * i) for i in range(1, 10)]
        'results' : [num * i for i in range(1, 10)]
        # 'range' : range(1, 10)
    }

    return render(request, 'gugu.html', context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index), #''는 기본 경로, 아무것도 안넣었을떄에는 기본인 "8000"포트에 들어간다.

    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>', language),

    path('language/python/', python),

    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugu/<int:num>/', gugu),

]
