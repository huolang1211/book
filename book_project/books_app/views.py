from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.http import JsonResponse

from books_app.utils import valid_code
from books_app.myforms import *


# Create your views here.

def login(request):
    # 基于用户认证组件实现
    if request.method == 'POST':
        # post请求
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        valid_code = request.POST.get('valid_code')  # 拿到用户输入的随机验证码
        valid_code_str = request.session.get('valid_code_str')  # 拿到保存在cookie里的验证码
        data = {'user': None, 'msg': None}
        # 拿到数据与数据库的auth_user表进行比对
        if valid_code.upper() == valid_code_str.upper():  # 判断验证码是否通过
            user = auth.authenticate(username=user, password=pwd)  # 利用用户认证组件校验
            if user:
                auth.login(request, user)  # request.user == 当前登录对象
                data['user'] = user.username
            else:
                data['msg'] = '账号或密码错误！'
        else:
            data['msg'] = '验证码错误！'
        return JsonResponse(data)

    return render(request, 'login.html')


def get_validCode_img(request):
    """
    生成随机图片验证码
    :param request:
    :return:
    """

    data = valid_code.get_valid_code_img(request)
    return HttpResponse(data)


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    auth.logout(request)  # 基于用户认证组件实现注销
    return redirect('/login/')


def register(request):
    """
    注册
        get请求：响应注册页面
        post请求：校验字段，响应字典
    :param request:
    :return:
    """

    if request.is_ajax():  # 是否是ajax请求
        form = UserForm(request.POST)
        response = {'usre': None, 'msg': None}
        if form.is_valid():
            response['user'] = form.cleaned_data.get('user')
            # 生成一条用户纪录
            user = form.cleaned_data.get('user')[0]
            pwd = form.cleaned_data.get('pwd')
            email = form.cleaned_data.get('email')
            avatar_obj = request.FILES.get('avatar')  # 获取文件对象
            extra = {}
            if avatar_obj:  # 如果有头像
                extra['avatar'] = avatar_obj
            # 创建用户对象
            UserInfo.objects.create_user(username=user, password=pwd, email=email, **extra)
        else:
            response['msg'] = form.errors  # 返回错误信息
        return JsonResponse(response)

    form = UserForm()  # 利用forms组件渲染标签
    return render(request, 'register.html', {'form': form})


# 查看书籍
def book(request):
    # ============================书籍===================================
    # 取出书籍的键值对
    book_values = Book.objects.all()
    book_form = BookForm()

    # ============================出版社===================================
    # 取出出版社的键值对
    publish_values = Publish.objects.all()
    publish_form = PublishForm()
    # ============================作者===================================
    # 取出作者的键值对
    author_values = Author.objects.all()
    author_form = AuthorForm()
    return render(request, 'book.html', locals())


def add_books(request):
    """
    添加书籍
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = BookForm(request.POST)

        # 用BookForm接收用户输入，实例化一个对象，用于后期检测，只检测BookForm中有的字段
        if form.is_valid():
            # 检测通过
            book_obj = Book.objects.create(  # 在数据库生成新数据
                title=form.cleaned_data.get('title'),
                publishDate=form.cleaned_data.get('publishDate'),
                price=form.cleaned_data.get('price'),
                publish_id=form.cleaned_data.get('publish'),  # 多对一添加出版社
            )
            book_obj.authors.add(*form.cleaned_data.get('author'))  # 多对多添加作者
            return redirect('/book/')
        else:
            errors = form.errors.get('__all__')
            return render(request, 'add_books.html', locals())

    form = BookForm()
    return render(request, 'add_books.html', locals())


def add_publish(request):
    """
    添加出版社
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = PublishForm(request.POST)
        # 用PublishForm接收用户输入，实例化一个对象，用于后期检测，只检测PublishForm中有的字段
        if form.is_valid():
            # 检测通过
            Publish.objects.create(  # 在数据库生成新数据
                name=form.cleaned_data.get('name'),
                city=form.cleaned_data.get('city'),
                email=form.cleaned_data.get('email'),
            )
            return redirect('/book/')
        else:
            print('error:', form.errors.get('__all__'))
            errors = form.errors.get('__all__')
            return render(request, 'add_publish.html', locals())
    form = PublishForm()
    return render(request, 'add_publish.html', locals())


def add_author(request):
    """
    添加作者信息
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        # 用AuthorForm接收用户输入，实例化一个对象，用于后期检测，只检测AuthorForm中有的字段
        if form.is_valid():
            # 检测通过
            Author.objects.create(  # 在数据库生成新数据
                name=form.cleaned_data.get('name'),
                age=form.cleaned_data.get('age'),
            )
            return redirect('/book/')
        else:
            print('error:', form.errors.get('__all__'))
            errors = form.errors.get('__all__')
            return render(request, 'add_author.html', locals())
    form = AuthorForm()
    return render(request, 'add_author.html', locals())


def publish_list(request, id):
    """
    查看该出版社出版的书籍
    :param request:
    :return:
    """
    # 根据出版社的id，一对多取书籍信息
    book_list = Book.objects.filter(publish__nid=id).all()
    print('book_list', book_list)
    return render(request, 'publish_list.html', {'book_list': book_list})


def author_list(request, id):
    """
    查看该作者写的书籍
    :param request:
    :return:
    """

    """
    查看该出版社出版的书籍
    :param request:
    :return:
    """
    # 根据出版社的id，一对多取书籍信息
    book_list = Book.objects.filter(authors__nid=id).all()
    print('book_list', book_list)
    return render(request, 'author_list.html', {'book_list': book_list})


def change_author(request, id):
    """
    修改作者信息
    :param request:
    :param id: 作者的id
    :return:
    """

    if request.method == 'POST':
        res = {'user': None, 'msg': None, 'field': None}
        print('post', request.POST)
        form = AuthorForm(request.POST)
        # 用AuthorForm接收用户输入，实例化一个对象，用于后期检测，只检测AuthorForm中有的字段
        if form.is_valid():
            # 检测通过
            Author.objects.filter(pk=id).update(  # 在数据库生成新数据
                name=form.cleaned_data.get('name'),
                age=form.cleaned_data.get('age'),
            )
            res['user'] = form.cleaned_data.get('name')
        else:
            res['msg'] = form.errors  # 返回错误信息
        return JsonResponse(res)  # 序列化

    # =========get请求=========
    author_obj = Author.objects.filter(nid=id).first()  # 根据id,查出作者信息
    form = AuthorForm()
    return render(request, 'change_author.html', locals())


def change_publish(request, id):
    """
    修改出版社信息
    :param request:
    :param id: 出版社的id
    :return:
    """

    if request.method == 'POST':
        res = {'user': None, 'msg': None, 'field': None}
        form = PublishForm(request.POST)
        # 用AuthorForm接收用户输入，实例化一个对象，用于后期检测，只检测AuthorForm中有的字段
        if form.is_valid():
            # 检测通过
            Publish.objects.filter(pk=id).update(  # 在数据库生成新数据
                name=form.cleaned_data.get('name'),
                city=form.cleaned_data.get('city'),
                email=form.cleaned_data.get('email'),
            )
            res['user'] = form.cleaned_data.get('name')
        else:
            res['msg'] = form.errors  # 返回错误信息
        print('form', form.errors)
        return JsonResponse(res)  # 序列化

    # =========get请求=========
    publish_obj = Publish.objects.filter(nid=id).first()  # 根据id,查出出版社信息
    form = PublishForm()
    return render(request, 'change_publish.html', locals())


def change_book(request, id):
    """
    修改书籍信息
    :param request:
    :param id: 书籍的id
    :return:
    """
    book_obj = Book.objects.filter(nid=id).first()  # 根据id,查出书籍信息
    if request.method == 'POST':
        print('fkdslf', request.POST)
        res = {'adopt': None, 'msg': None}
        form = BookForm(request.POST)
        # 用BookForm接收用户输入，实例化一个对象，用于后期检测，只检测BookForm中有的字段
        form.is_valid()  # 将数据进行检测
        del form.errors['title']  # 因title不可变，故title的错误可以忽略，所以将其错误信息删除
        if not form.errors:  # 删除title错误后无错误信息则通过检测
            # 检测通过
            Book.objects.filter(pk=id).update(  # 在数据库生成新数据
                publishDate=form.cleaned_data.get('publishDate'),
                price=form.cleaned_data.get('price'),
                publish_id=form.cleaned_data.get('publish'),
            )
            book_obj.authors.set(form.cleaned_data.get('author'))  # 修改书籍作者
            res['adopt'] = 'OK'
        else:
            res['msg'] = form.errors  # 返回错误信息

        return JsonResponse(res)  # 序列化

    # =========get请求=========
    book_obj = Book.objects.filter(nid=id).first()  # 根据id,查出书籍信息
    publish_list = Publish.objects.all()  # 根据id,查出出版社信息
    author_list = Author.objects.all()  # 根据id,查出出版社信息
    form = BookForm()
    return render(request, 'change_book.html', locals())


def delete_book(request, book_id):
    """
    删除书籍数据
    :param request:
    :param id:
    :return:
    """

    book_obj = Book.objects.filter(nid=book_id).first()  # 取出book对象
    book_obj.authors.clear()  # 解除和Author表的所有绑定关系
    book_obj.delete()  # 删除book对象
    # redirect 重定向，跳转页面
    return redirect('/book/')


def delete_publish(request, publish_id):
    """
    删除出版社数据
    :param request:
    :return:
    """
    Publish.objects.get(nid=publish_id).delete()
    Book.objects.filter(publish_id=publish_id).delete()
    return redirect('/book/')


def delete_author(request, author_id):
    """
    删除作者数据
    :param request:
    :return:
    """

    author_obj = Author.objects.filter(nid=author_id).first()  # 拿到要删除的作者对象
    author_obj.book_set.clear()  # 解除和Book表的所有绑定关系
    author_obj.delete()  # 删除作者对象
    return redirect('/book/')
