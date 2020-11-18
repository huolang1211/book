$('#login_btn').click(function () {
    $.ajax({
        url: '',
        type: 'post',
        data: {
            user: $('#username').val(),
            pwd: $('#pwd').val(),
            valid_code: $('#validCode').val(),//用户输入的随机验证码
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),//cs校验
        },
        success: function (data) {
            console.log(data);
            if (data.user) {
                location.href = '/book/';
            } else {
                $('.error').text(data.msg);//显示错误信息
            }
        }
    })
});

//随机验证码刷新
$('#validCodeImg').click(function () {
    $(this)[0].src += '?';//在其路径后加一个？代表刷新
});