from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs' : blogs})

def create(request):
    # 새로운 글(데이터)저장하는 역할 == POST
    
    if request.method == 'POST':
        form = NewBlog(request.POST) # 입력받았어
        if form.is_valid:
            #입력된 글들을 저장
            post = form.save(commit=False) #commit=flase 아직은 저장하지 말고, 정보 덜 입력했으니까
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    # 글쓰기 페이지를 띄워주는 역할 == GET (!= POST)
    
    else:
        #단순히 입력받을 수 있는 form을 띄우기
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form' : form})

def update(request, pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    # 해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog) # pk에 해당하는 blog를 저장하는 instance.(는 객체같은거)
    if form.is_valid():
        form.save()
        return redirect('home')
    #입력이 잘못되었거나 request방식이 다르면
    return render(request, 'viewcrud/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')