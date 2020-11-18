alert("Hello");
console.log("here");
function ListDrop(category_id) {
    $('.list_' + category_id).toggle();
    $('#ldrop_' + category_id).toggleClass(' fa fa-angle-down fa fa-angle-up');
}

$(".overlay").click(function() {
    $(".overlay").css("display", "none");
});

$(".item-detail-picture").click(function() {
    $(".overlay").css("display", "block");
});

$('#upload_form').submit(function(){
    console.log('Checking file size');
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var file = $('#id_{{ form.upload_field_name }}')[0].files[0];
        var max_upload_limit = {{ form.max_upload_limit }};
        if (file && file.size > max_upload_limit) {
            alert('File'+file.name+ 'of type' +file.type+) 'must be < {{ form.max_upload_limit_text}}');
            return false;
        }
    }
});
