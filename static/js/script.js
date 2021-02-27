
// Mobile initialization from Materialize
$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});


