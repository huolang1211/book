from django import forms
from django.forms import widgets
from books_app.models import *
from django.core.exceptions import ValidationError

wid_text = widgets.TextInput(attrs={'class': 'form-control'})
wid_date = widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'})
wid_pwd = widgets.PasswordInput(attrs={'class': 'form-control'})
wid_sm = widgets.SelectMultiple(attrs={'class': 'form-control'})
wid_select = widgets.Select(attrs={'class': 'form-control'})
wid_email = widgets.EmailInput(attrs={'class': 'form-control'})


def get_obj(obj_models):
    """
    从数据库取出元素对象
    :param obj_models: 表名
    :return:
    """
    obj_list = obj_models.objects.values()
    p_list = []
    for obj in obj_list:
        item = (obj.get('nid'), obj.get('name'))
        p_list.append(item)
    obj_tuple = tuple(p_list)

    return obj_tuple


#
#
class UserForm(forms.Form):
    """用户信息forms组件"""
    user = forms.CharField(
        max_length=32,
        error_messages={'required': '该字段不能为空'},  # 错误信息
        label='用户名',
        widget=wid_text
    )
    pwd = forms.CharField(
        max_length=32,
        error_messages={'required': '该字段不能为空'},  # 错误信息
        label='密码',
        widget=wid_pwd
    )
    re_pwd = forms.CharField(
        max_length=32,
        error_messages={'required': '该字段不能为空'},  # 错误信息
        label='确认密码',
        widget=wid_pwd
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={'required': '该字段不能为空', 'invalid': '格式错误'},  # 错误信息
        widget=wid_email
    )

    def clean_user(self):
        """
        用户名查重
        :return:
        """
        val = self.cleaned_data.get('user'),
        user = UserInfo.objects.filter(username=val).first()  # 在数据库中查找该用户名是否已经存在
        if not user:
            return val
        else:
            raise ValidationError('该用户已注册！')

    def clean(self):
        """
        两次输入的密码是否一致
        :return:
        """
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get(('repwd'))
        if pwd and re_pwd:  # 两次输入都不为空
            if pwd == re_pwd:  # 两次输入是否一致
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致！')
        else:
            return self.cleaned_data


#
#
class PublishForm(forms.Form):
    """出版社forms组件"""
    name = forms.CharField(
        label='社名',
        max_length=32,
        error_messages={'required': '该字段不能为空'},
        widget=wid_text
    )
    city = forms.CharField(
        label='所在城市',
        min_length=2,
        error_messages={'required': '该字段不能为空', 'min_length': '最少两个字'},
        widget=wid_text
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={'required': '该字段不能为空', 'invalid': '格式错误'},  # 错误信息
        widget=wid_email
    )


class AuthorForm(forms.Form):
    """作者forms组件"""
    name = forms.CharField(
        label='姓名',
        max_length=32,
        error_messages={'required': '该字段不能为空'},
        widget=wid_text
    )
    age = forms.IntegerField(
        label='年龄',
        error_messages={'required': '该字段不能为空'},
        widget=wid_text
    )

    def clean_age(self):
        """
        输入年龄在合理范围
        :return:
        """
        val = self.cleaned_data.get('age')
        if 0 < val < 150:
            return val
        raise ValidationError('必须在0-150之间！')


class BookForm(forms.Form):
    """书籍的forms组件"""
    title = forms.CharField(
        label='书名',
        max_length=32,
        error_messages={
            'required': '该字段不能为空',
            'max_length': '书名太长了，谁记得住啊！'
        },
        widget=wid_text
    )
    publishDate = forms.DateField(
        label='出版日期',
        error_messages={'required': '该字段不能为空'},
        widget=wid_date
    )
    price = forms.DecimalField(
        label='价格',
        max_digits=6,
        decimal_places=2,
        error_messages={
            'required': '该字段不能为空',
            'max_digits': '你标的价格太高了！',
            'decimal_places': '小字数位数太多，不好收钱，最多两位小数'},
        widget=wid_text
    )

    publish = forms.ChoiceField(
        choices=get_obj(Publish),
        label="出版社",
        widget=wid_select
    )
    author = forms.MultipleChoiceField(
        choices=get_obj(Author),
        label="作者",
        widget=wid_sm
    )

    def clean_price(self):
        """
        输入价格在合理范围
        :return:
        """
        val = self.cleaned_data.get('price')
        if 0 < val:
            return val
        raise ValidationError('不能为负数，总不至于倒贴吧！')

    def clean_title(self):
        """
        书名不能重复
        :return:
        """
        val = self.cleaned_data.get('title')  # 拿到用户输入
        ret = Book.objects.filter(title=val)  # 在数据库查询有没有和用户输入一致的书名

        if not ret:
            return val
        raise ValidationError('该书名已被注册，换一个吧！')  # 返回错误信息
