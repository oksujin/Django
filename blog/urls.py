from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # 정규표현식 url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/1/$', views.post_detail, name='post_detail'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 정규표현식 url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # 정규표현식 사용 [첫번째자리][두번째자리] = 0123456789 = \d
    # + : 숫자가 1번 이상 반복될 것이다.

    path('post/new/', views.post_new, name='post_new'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]