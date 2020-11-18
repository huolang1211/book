$(function () {
    //保存数据
    $('.btn-primary').click(function () {
        var id = $('#chang_id input').val();
        var path = '/book/' + id + '/change_book/';//拼接路径
        var formdata = new FormData();
        var request_data = $('#form').serializeArray();
        $.each(request_data, function (index, data) {
            console.log('data', data);
            formdata.append(data.name, data.value);
        });
        $.ajax({
            url: path,
            type: 'post',
            contentType: false,
            processData: false,
            data: formdata,
            success: function (data) {
                if (data.adopt) {
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
    });

    //关闭窗口
    $('.close').click(function () {
        location.href = '/book/'
    })
});