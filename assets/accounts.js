var OpenOTPEl = new bootstrap.Modal(document.getElementById('OpenOTPModal'))

function errorAlert(errorMessage,inputId){
    $('#'+inputId).after('<div id="alertfor' + inputId + '" class="erroralert invalid-feedback">' + errorMessage + '</div')
    $('#alertfor' + inputId).fadeIn('slow')
    if (inputId=='') {return}
    $('#'+inputId).addClass('is-invalid')

}
function formReset(formId){
    $('#'+formId).trigger('reset')
    $(':input','#'+formId).removeClass('is-invalid')
    $('.erroralert','#'+formId).remove()
}

$(document).ready(function(){


    $('#OpenOTPBtn').click(function(){
        OpenOTPEl.show()
    })

//    $('#id_username').bind("change keyup input click", function() {
//        if (this.value.match(/[^0-9]/g)) {
//            errorAlert('Введите 10 цифр', 'id_username')
//            this.value = this.value.replace(/[^0-9]/g, '')
//            }
//    })

});