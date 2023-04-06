$(document).ready(function(){

    $('.btn-del').click(function(){
        $.ajax({
            url:'del',
            type: 'get',
            data: {
                package_id: $(this).parent().parent().attr('id').slice(6) // отправляем ID на удаление
            },
            success: function(response){
                $('#track_'+response.id).fadeOut('fast');
                //$('#track_'+response.id).remove();
                // если ответ пришел, удаляем блок с кодом
            }

        })
    })

    $('.btn-del').click(function(){
        $.ajax({
            url:'del',
            type: 'get',
            data: {
                package_id: $(this).parent().parent().attr('id').slice(6) // отправляем ID на удаление
            },
            success: function(response){
                $('#track_'+response.id).fadeOut('fast');
                //$('#track_'+response.id).remove();
                // если ответ пришел, удаляем блок с кодом
            }

        })
    })

    $('#addpackage').click(function(){

        packageData = $('#addpackageform').serialize();
        $.ajax({
            url: $('#addpackageform').data('url'),
            type: 'post',
            data: packageData,
            success: function(response){
                if (response.errorMessage==1){
                    $('#errorallert').fadeIn('slow')
                }
                else {
                    newTrackDiv = '<div class="card mt-1" id="track_' + response.package_id + '" style="display:none">'
                    newTrackDiv += '<div class="card-body"><button type="button" class="btn-close float-end  btn-del" aria-label="Удалить"></button>'
                    newTrackDiv += '<h3 class="card-title text-uppercase">' + response.package_id + '</h3>'
                    newTrackDiv += '<h6 class="card-subtitle mb-2 text-body-secondary">' + response.status + '</h6>'
                    newTrackDiv += '<p class="card-text">' + response.desc + '</p></div></div>'
                    $('#packageslist').append(newTrackDiv)
                    $('track_' + response.package_id).fadeIn('fast')
                }
            }

        })
    })

});