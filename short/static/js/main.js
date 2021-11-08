$(document).ready(function() {
    $('#log1').blur(function (){
        $.post(
        'log_2',
            {'aaa': $('#log1').val()},
            function (response) {
                if (response.exists == 'y' ) {
                    alert('Такой пользователь уже есть')
                }
            }
        )
    });
    $('#short').click(function (){
        $.post(
        'short',
            {'aaa': $('#log1').val()},
            function (response) {
                if (response.exists == 'y' ) {
                    alert('Такая запись уде есть')
                }
            }
        )
    })
});