theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
document.documentElement.setAttribute('data-bs-theme', theme)

function errorAlert(errorMessage,inputId){
    if ($('#alertfor' + inputId).length) {
        if($('#alertfor' + inputId).html()==errorMessage){return}
        $('#alertfor' + inputId).fadeOut('fast')
        $('#alertfor' + inputId).html(errorMessage)
    }
    else {
        $('#'+inputId).after('<div id="alertfor' + inputId + '" class="erroralert invalid-feedback">' + errorMessage + '</div')
    }
    $('#alertfor' + inputId).fadeIn('slow')
    if (inputId=='') {return}
    $('#'+inputId).addClass('is-invalid')
}

function formReset(formId){
    $('#'+formId).trigger('reset')
    $(':input','#'+formId).removeClass('is-invalid')
    $('.erroralert','#'+formId).remove()
}

function PhoneMask(){
    $('input[type="tel"]').mask('(999)999-99-99');
    $('form').submit(function(){
        $('input[type="tel"]').val($('input[type="tel"]').val().replaceAll(/[^0-9]/g,''));
    });
}

function NavBar(){
    $.ajax({

    })
}