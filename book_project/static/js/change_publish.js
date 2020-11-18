$(function () {
    //保存数据
    $('.btn-primary').click(function () {
        var id = $('#chang_id input').val();
        var path = '/book/' + id + '/change_publish/';//拼接路径
        $.ajax({
            url: path,
            type: 'post',
            data: {
                name: $('#id_name').val(),
                city: $('#id_city').val(),
                email: $('#id_email').val(),
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"] ').val()
            },
            success: function (data) {
                if (data.user) {
                    location.href = '/book/'
                } else {
                    //清空错误信息
                    $('span.error').html('');
                    $('.form-group').removeClass('has-error');
                    //展示此次提交的错误信息
                    $.each(data.msg, function (field, error_list) {
                        $('#id_' + field).next().html(error_list[0]).parent().addClass('has-error');
                        //其它字段也加上错误信息展示效果
                    })
                }
            }
        })
    })

    //关闭窗口
    $('.close').click(function () {
        location.href = '/book/'
    })
})