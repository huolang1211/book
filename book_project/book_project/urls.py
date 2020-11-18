"""book_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from books_app import views
from book_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),  # 登录
    path('get_img/', views.get_validCode_img),  # 获取随机验证图片
    path('logout/', views.logout),  # 退出
    path('register/', views.register),  # 注册
    path('book/', views.book),  # 书籍
    re_path('^$', views.book),  # 主页也是书籍
    path('add_books/', views.add_books),  # 添加书籍
    path('add_publish/', views.add_publish),  # 添加出版社
    path('add_author/', views.add_author),  # 添加作者
    re_path(r'book/(\d+)/delete_book/$', views.delete_book),  # 删除书籍
    re_path(r'book/(\d+)/change_book/$', views.change_book),  # 编辑书籍
    re_path(r'book/(\d+)/delete_publish/$', views.delete_publish),  # 删除出版社
    re_path(r'book/(\d+)/change_publish/$', views.change_publish),  # 编辑出版社
    re_path(r'book/(\d+)/delete_author/$', views.delete_author),  # 删除作者
    re_path(r'book/(\d+)/change_author/$', views.change_author),  # 编辑作者
    re_path(r'book/(.+)/author_list/$', views.author_list),  # 查看作者所写书籍列表
    re_path(r'book/(\d+)/publish_list/$', views.publish_list),  # 查看出版社出版书籍列表
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),  # media配置:存放用户头像
]
