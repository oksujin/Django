from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post  
from .forms import PostForm

def post_list(request) :
    qs = Post.objects.all() # 전체 글 목록을 가져오겠다.
    # qs(쿼리 셋) 데이터를 가져오는 조건
    qs = qs.filter(published_date__lte=timezone.now()) # 발행날짜가 현재 날짜보다 작거나 같은 데이터들
    qs = qs.order_by('published_date') # 발행 날짜 기준으로 오름차순 정렬

    
    #render : 장고가 지원하는 템플릿 시스템
    return render(request, 'blog/post_list.html', {
        'post_list' : qs, # 받아온 데이터를 post_list라는 이름으로 쓰겠다.
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 원래 페이지 볼 수 없을 때 처리하는 코드
    # try :
    #     post = Post.objects.get(pk=pk) #(field명 = 입력받은 pk)
    # except Post.DoesNotExist:
    #     raise Http404 #Page Not Found : from django.http import Http404
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

# @로그인을 꼭 해야함
def post_new(request):
    # request.POST, request.FILES

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # 받아온 값을 넣어서 form 생성
        if form.is_valid() : # 입력받아온 값 유효성 
            post = form.save(commit=False)
            post.author = request.user # admin이 꺼져있으면 로그인 확인 못해서 error
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else :
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form' : form,
    } )

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
 
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 받아온 값을 넣어서 form 생성
        if form.is_valid() : # 입력받아온 값 유효성 
            post = form.save(commit=False)
            post.author = request.user # admin이 꺼져있으면 로그인 확인 못해서 error
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {
        'form' : form
    })