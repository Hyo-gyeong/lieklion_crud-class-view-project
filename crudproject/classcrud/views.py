from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# Create your views here.
# 클래스를 수행하게 해주는 html필요
#html의 이름이 default로 지어져있음
#다른 이름 사용하고싶으면 명시해주어야 함.
class BlogView(ListView):     #블로그 리스트를 담은 html필요, 이름 : (소문자모델)_list.html
    #template_name = 'classcrud/list.html' // classcrud폴더 안에 list라는 이름으로 파일이름을 만들꺼야~~
    #object_list가 default지만 여러 object_list를 만드는 경우
    #context_object_name = 'blog.list'이렇게 바꿀 수 있음
    model = ClassBlog

class BlogCreate(CreateView):       #입력 공간을 갖고있는 html필요, 이름 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):       # 상세 페이지를 담은 html필요, 이름 : (소문자모델)_detail.html
    #object가 default지만 여러 object를 만드는 경우
    #context_object_name = 'blogpost'이렇게 바꿀 수 있음
    model = ClassBlog

class BlogUpdate(UpdateView):       #입력 공간을 갖고있는 html필요, 이름 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):       #"진짜 지울건지?"확인하는 html필요, 이름 : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')