$(document).ready(function(){

    $('.btn-del').click(function(){
        $.ajax({
            url:'del',
            type: 'get',
            data: {
                package_id: $(this).parent().attr('id').slice(6) // отправляем ID на удаление
            },
            success: function(response){
                $('#track_'+response.id).remove(); // если ответ пришел, удаляем блок с кодом
            }

        })
    })

});