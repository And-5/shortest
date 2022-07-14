$(document).ready(function() {
    $('#log1').blur(function (){
        $.post(
        'log_2',
            {'a': $('#log1').val()},
            function (response) {
                if (response.exists == 'y' ) {
                    alert('Такой пользователь уже есть')
                }
            }
        )
    })
    $('#email1').blur(function (){
        $.post(
        'email_2',
            {'b': $('#email1').val()},
            function (response) {
                if (response.exists == 'y' ) {
                    alert('Такой email уже зарегистрирован')
                }
            }
        )
    })
})
