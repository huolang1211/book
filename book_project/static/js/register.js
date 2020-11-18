//头像预览
$('#avatar').change(function () {
    //获取用户选中的文件对象
    var file_obj = $(this)[0].files[0];
    //获取文件对象的路径
    var reader = new FileReader();//实例化一个读取功能 的对象
    reader.readAsDataURL(file_obj);//读取文件路径
    reader.onload = function () {
        $('#avatar_img').attr('src', reader.result);
        //修改图片路径，就是换上用户选中的图片
    }
});

//基于Ajax提交数据
$('.reg_btn').click(function () {
    var formdata = new FormData();
    var request_data = $('#form').serializeArray();
    //拿到form的全部字段数据
    $.each(request_data, function (index, data) {
        formdata.append(data.name, data.value);
    });
    formdata.append('avatar', $('#avatar')[0].files[0]);// 放入头像字段

    $.ajax({
        url: '',
        type: 'post',
        contentType: false,//不能默认方式传输数据
        processData: false,
        data: formdata,
        success: function (data) {
            if (data.user) {
                //注册成功
                location.href = '/login/';
            } else {//注册失败
                //清空错误信息
                $('span.error').html('');
                $('.form-group').removeClass('has-error');
                //展示此次提交的错误信息
                $.each(data.msg, function (field, error_list) {

                    if (field == '__all__') {
                        $('#id_re_pwd').next().html(error_list[0]).parent().addClass('has-error');
                        //全局钩子的错误信息，放在re_pwd中展示，并为其添加边框变红的样式
                    }
                    $('#id_' + field).next().html(error_list[0]).parent().addClass('has-error');
                    //其它字段也加上错误信息展示效果
                })
            }
        }
    })
});