var trackidDelModalEl = new bootstrap.Modal(document.getElementById('trackidDelModal'))
var trackidAddModalEl = new bootstrap.Modal(document.getElementById('trackidAddModal'))

function DeleteTrackId(trackid) {
    $('#deltrackid').html(trackid)
    $('#trackIdDelConfirmBtn'.).click(function(){
        $.ajax({
            url:'del',
            type: 'get',
            data: {
                package_id: trackid
            },
            success: function(response){
                trackidDelModalEl.hide()
                $('#track_'+response.id).fadeOut('fast');
            }
        })
    })
    trackidDelModalEl.show()
}

$(document).ready(function(){

    $('#trackidAddOpenModalBtn').click(function(){
        trackidAddModalEl.show()
    })

    $('#id_trackid').bind("change keyup input click", function() {
            if (this.value.match(/[^0-9a-zA-Z\s]/g)) {
                errorAlert('Только латинские буквы и цифры','id_trackid')
                this.value = this.value.replace(/[^0-9a-zA-Z\s]/g, '')
                }
        })

    $('#addpackage').click(function(){
        packageData = $('#addpackageform').serialize();
        $.ajax({
            url: $('#addpackageform').data('url'),
            type: 'post',
            data: packageData,
            success: function(response){
                $('#notracks').remove()
                if (response.errorMessage==1){
                    errorAlert('Трек-номер уже был добавлен ранее', 'id_trackid')
                }
                else if (response.errorMessage==2){
                    errorAlert('Введите корректный трек-номер', 'id_trackid')
                }
                else {
                    trackidAddModalEl.hide()
                    formReset('addpackageform')
                    newTrackDiv = '<div class="card mt-2" id="track_' + response.packageid + '" style="display:none">'
                    newTrackDiv += '<div class="card-body"><button type="button" class="btn-close float-end  btn-del" onclick="DeleteTrackId(\'' + response.packageid + '\')" aria-label="Удалить"></button>'
                    if (response.desc==''){
                        newTrackDiv += '<h3 class="card-title">' + response.packageid + '</h3>'
                        newTrackDiv += '<h6 class="card-subtitle mb-2 text-body-secondary">' + response.status + ' ' + response.changedate + '</h6>'
                    }
                    else {
                        newTrackDiv += '<h3 class="card-title">' + response.desc + '</h3>'
                        newTrackDiv += '<h6 class="card-subtitle mb-2 text-body-secondary">' + response.status + ' ' + response.changedate + '</h6>'
                        newTrackDiv += '<p class="card-text">Трек-номер: ' + response.packageid + '</p></div></div>'
                    }
                    $('#packageslist').append(newTrackDiv)
                    $('#track_' + response.packageid).fadeIn('slow')
                }
            }

        })
    })

});