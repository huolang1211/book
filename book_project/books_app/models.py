from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserInfo(AbstractUser):
    """用户信息"""
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)  # 手机号，可以为空，且唯一
    avatar = models.FileField(upload_to='avatars/', default='/avatars/default.png')
    # 头像，存放地址的相对路径，初始图片路径
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 创建时间，生成该字段时不用赋值，当前时间就是该值

    def __str__(self):
        """
        打印时显示的信息
        :return: 用户名
        """
        return self.username


class Publish(models.Model):
    """出版社信息表"""
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # 名字
    city = models.CharField(max_length=32)  # 所在城市
    email = models.EmailField()  # 邮箱

    def __str__(self):
        """
        打印时显示的信息
        :return: 出版社的名字
        """
        return self.name


class Author(models.Model):
    """作者信息表"""
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()  # 年龄

    def __str__(self):
        """
        打印时显示的信息
        :return: 作者的名字
        """
        return self.name


class Book(models.Model):
    """书籍信息表"""
    nid = models.AutoField(primary_key=True)  # 主键，自增
    title = models.CharField(max_length=32)
    publishDate = models.DateField(default='2020-01-01')  # 出版日期
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)  # 价格,最多五位数，小数点后两位

    publish = models.ForeignKey(to='Publish', to_field='nid', on_delete=models.CASCADE)  # 与出版社表建立多对一关系
    authors = models.ManyToManyField(to='Author')  # 与Author建立多对多关系

    def __str__(self):
        """
        打印时显示的信息
        :return: 书名
        """
        return self.title
