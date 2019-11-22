function extraToggle(){
    var sub = $("#id_product_names").val();
    if (sub === 'Steak + Cheese'){
        $("#toppings__label").html('<b>Add extras: </b>');
        $("#toppings__checkboxes").css("display", "block");
    }
    else {
        $("#toppings__checkboxes").css("display", "none");
        $("input[name='extras']").prop( "checked", false );
    }
    }


$('.submit_order').click(function(){
    var sub = $("#id_product_names").val();
    var size = $("#id_product_sizes").val();
    if (sub === 'Sausage, Peppers & Onions' && size!=2) {
        return false
    }

})

$("#id_product_names, #id_product_sizes").change(function(){
    var sub = $("#id_product_names").val();
    var size = $("#id_product_sizes").val();
    if (sub === 'Sausage, Peppers & Onions' && size==1) {
        $('.size_error').css("display", "block");
    }
    else{
        $('.size_error').css("display", "none");
    }
})

$("#id_product_names").change(extraToggle);
$(document).ready(extraToggle);
