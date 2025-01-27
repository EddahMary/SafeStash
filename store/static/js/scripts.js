$(document).ready( function() {
    $('#bookslot').click(function subst(){
        alert("Your slot has been booked successfully see it on slots info!");
        var slots = parseInt($("#slots").val());
        slots--;
        $("#slots").text(slots);
    });
    $('#delivery').click(function(){
        alert("Your delivery details have been submitted successfully keep your phone on in case of any communication intended!");
    });
    $('#pickup').click(function(){
        alert("Your pick up details have been submitted successfully we will be expecting you at the time you have sent!");
    });
    $('#pickup1').click(function () {
        $('#delivery1').remove();
    });
});
