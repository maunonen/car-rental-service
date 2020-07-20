/* 
setTimeout(() => {
    $('#message').fadeOut('slow'); 
}, 3000);

$(document).ready(function() {
    $('.datepicker').datepicker();
    
    $('#contact-form').on('submit', function(event){
        console.log("AJAX")
        event.preventDefault();
        $.ajax({
            url: '/courses/',
            type: 'POST',
            headers: {'X-CSRFToken': '{{ csrf_token }}'},
            data: $('#enroll-form').serialize(),
            
            beforeSend: function () {
                $("#contactModal").modal("show");
            },
            
            success: function(data) {
                $('#contactModal .modal-body').html(data);
                console.log("SUCCESS");
            }
            error: function(data) {
                console.log("Error")
            }
        });
    });
}); */