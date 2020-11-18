
# book_project

---

## Introduction

后端使用 `django`

前端使用 `jquery` & `bootstrap` 

## 开发环境

- Python 3.6.8  
- Django 3.1.3
- Jquery 3.4.1 
- Bootstrap 3.3.7

## Quick Tutorial


### 生成表结构

> 使用 `mysql` 数据库

```
python manage.py makemigrations

python manage.py migrate
```

### 启动项目

```
python manage.py runserver 8000

后台地址：

127.0.0.1:8000/admin/

账号密码 odin 123
```

### 登录用户信息
```
python manage.py runserver 8000

超级用户：

账号密码 odin 123

普通用户：

账号密码 alex 123
账号密码 wusir 123
```

### 程序的实现的功能
```

1. 实现用户登录、注册
2. 列出图书列表、出版社列表、作者列表
3. 点击作者，会在新的页面列出该作者出版的图书列表
4. 点击出版社，会列出该出版社旗下图书列表
5. 可以创建、修改、删除 图书、作者、出版社
6. 点击修改按钮，弹出模块框，模态框中展示该书、出版社、作者的信息且信息可以修改
7. 书名不可重复，不可修改
8. 修改信息时，使用ajax请求发送信息

```
### 代码结构
```
/book_project
├── README 程序说明文件
├── 流程图.jpg 流程图文件
├── img 效果图
│   ├── book_project #选课系统 执行文件 目录
│   │   ├── __init__.py
│   │   ├── asgi.py # ASGI配置
│   │   ├── setting.py # 项目配置
│   │   ├── urls.py # 负责把URL模式映射到应用程序
│   │   ├── wsgi.py # WSGI配置
│   ├── books_app # app应用
│   │   ├── migrations # 数据库相关
│   │   ├── utils # 工具
│   │   │   ├── valid_code.py # 创建随机验证码
│   │   ├── admin.py # 后台管理
│   │   ├── apps.py # 应用程序配置
│   │   ├── models.py # 模型
│   │   ├── myforms.py # 数据校验
│   │   ├── tests.py # 测试
│   │   └── viems.py # 视图 主逻辑
│   ├── media #存放用户上传文件
│   │   ├── avatars #存放头像文件
│   │   └── __init__.py
│   ├── static  # 静态文件
│   │   ├── __init__.py
│   │   ├── bootstrap # bootstrap文件
│   │   ├── css # 样式文件
│   │   ├── font # 字体文件
│   │   ├── js # javascript文件
│   │   └── jquery-3.4.1.js # jquery文件
│   ├── templates  # 模板文件
│   │   ├── __init__.py
│   │   ├── bootstrap # bootstrap文件
│   │   ├── css # 样式文件
│   │   ├── font # 字体文件
│   │   ├── js # javascript文件
│   │   └── jquery-3.4.1.js # jquery文件
│   └── venv # 虚拟环境
├── __init__.py
└── manage.py # django工具
```
### 效果图

![image](https://github.com/huolang1211/book/blob/master/book_project/img/1.png)
![image](https://github.com/huolang1211/book/blob/master/book_project/img/2.png)
![image](https://github.com/huolang1211/book/blob/master/book_project/img/3.png)
![image](https://github.com/huolang1211/book/blob/master/book_project/img/4.png)

## 常见问题

### mysql 数据库使用 

* 配置

```
# 在 settings.py 文件下找到 DATABASES 配置，修改为 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名称',
        'USER': '用户名',
        'PASSWORD': '密码',
        'HOST': '',  # 默认 127.0.0.1
        'PORT': '',  # 默认 3306
    }
}
```

然后连接至您的数据库终端

```
$ mysql -u 用户名 -p 密码
创建数据库，记得指定编码
>>> create database 数据库名称 default charset utf8;

```

### 第一次执行这条语句报No changes detected

* 问题

```
python manage.py makemigrations
```

* 解决

在`APP`创建目录 migrations 并在里面创建__init__.py
```
mkdir APP_NAME/migrations
touch APP_NAME/migrations/__init__.py
```


### 头像文件存放在配置

* 默认

```
 /media/avatars
```

* 配置

```
# 在 settings.py 文件下找到 MEDIA_ROOT 配置，
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
  将其中的media修改成你要想的文件夹
```



```
2020 By Odin.
```
