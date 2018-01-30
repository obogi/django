from blog.urls import path
from . import views
# from . <- 점이 가리키는 점은 현재 위치

urlpatterns = [
    path('', views.post_list),
]