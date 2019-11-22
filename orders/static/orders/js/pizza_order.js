function toppingsToggle(){
    var toppings = $("#id_product_names").val();
    if (toppings === 'Special'){
        $("#toppings__label").html('<b>Choose toppings (Up to 5): </b>');
        $("#toppings__checkboxes").css("display", "block");
    }
    else if (toppings !== "Cheese" && toppings != ''){
        $("#toppings__label").html('<b>Choose toppings:</b>');
        $("#toppings__checkboxes").css("display", "block");
    }
    else {
        $("#toppings__label").html('');
        $("#toppings__checkboxes").css("display", "none");
        $("input[type='checkbox']").prop( "checked", false );
    }
}



$('.submit_order').click(function(){
    var amount_of_chosen_toppings = $('input[type="checkbox"]:checked').length;
    var toppings = $("#id_product_names").val();
    var max_toppings=5;
    if (toppings == 'Special'){
        if (amount_of_chosen_toppings!=max_toppings && amount_of_chosen_toppings!=max_toppings-1){
            $('.extras_error').css("display", "block");
            return false
        }}

    else if (toppings == 'Cheese'){
        if (amount_of_chosen_toppings!=0){
            $('.extras_error').css("display", "block");
            return false
        }
    }
    else{
        max_toppings = parseInt(toppings[0])
        if (amount_of_chosen_toppings != max_toppings){
            $('.extras_error').css("display", "block");
            return false
        }
    }
})

$("#id_product_names").change(toppingsToggle);
$( document ).ready(toppingsToggle);