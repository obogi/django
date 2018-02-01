from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    # 3/
    # 53/
    # 53/asdf/ <- X
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('<int:pk>/', views.post_detail, name='post-detail'),

    # localhost:8000/add 에 접근할 수 있는 path구현
    path('add/', views.post_add, name='post-add'),

    # 숫자가 1개이상 반복되는 경우를 정규표현식으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
]