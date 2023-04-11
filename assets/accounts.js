var OpenOTPEl = new bootstrap.Modal(document.getElementById('OpenOTPModal'))

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