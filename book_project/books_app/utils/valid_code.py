from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random


def get_random_color():
    """
    生成随机颜色
    :return: 三个0-255的随机数字
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_code_img(request):
    """
    生成随机图片验证码
    :param request:
    :return:
    """
    img = Image.new('RGB', (270, 40), color=get_random_color())  # 生成一个随机颜色的矩形图片
    draw = ImageDraw.Draw(img)  # 拿到画笔对象
    dearSun_font = ImageFont.truetype('static/font/dearSun.otf', size=28)  # 生成字体对象

    """随机在图片上写六个随机颜色的文字"""
    valid_code_str = ''
    for i in range(6):
        random_num = str(random.randint(0, 9))  # 随机0-9的数字
        random_low_alpha = chr(random.randint(95, 122))  # 随机小写字母a-z
        random_upper_alpha = chr(random.randint(65, 90))  # 随机大写字母A-Z
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])  # 随机取列表里的元素

        draw.text((i * 46 + 10, 5), random_char, get_random_color(), font=dearSun_font)  # 在img的(x,y)上写一个随机颜色的文字

        valid_code_str += random_char

    request.session["valid_code_str"] = valid_code_str  # 将random_char保存在COOKIE中
    print('valid_code', valid_code_str)
    """增加噪点噪线"""
    width = 270
    height = 40
    for i in range(5):
        x1 = random.randint(0, width)  # 随机x坐标值
        x2 = random.randint(0, width)  # 随机x坐标值
        y1 = random.randint(0, height)  # 随机y坐标值
        y2 = random.randint(0, height)  # 随机y坐标值

        draw.line((x1, y1, x2, y2), fill=get_random_color())  # 画一条随机线段

    for i in range(10):
        x = random.randint(0, width)  # 随机x坐标值
        y = random.randint(0, height)  # 随机y坐标值

        draw.point([x, y], fill=get_random_color())  # 随机画一个圆点

        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())  # 随机画一段圆弧

    f = BytesIO()  # 拿到内存句柄
    img.save(f, 'png')  # 将img以.png格式保存在内存中
    return f.getvalue()  # 取出数据并返回
