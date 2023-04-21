function recalculateCart()
{
  var subtotal = 0;
  var quantity = 0;  // initialize quantity variable
  
  /* Sum up row totals */
  $('.product').each(function () {
    var productQuantity = parseInt($(this).find('.product-quantity input').val());
    var productPrice = parseFloat($(this).find('.product-price').text());
    var productTotal = productQuantity * productPrice;
    subtotal += productTotal;
    quantity += productQuantity;  // update quantity variable
  });

  /* Calculate totals */
  var tax = subtotal * taxRate;
  var shipping = (subtotal > 0 ? shippingRate : 0);
  var total = subtotal + tax + shipping;
  
  /* Update totals display */
  $('.totals-value').fadeOut(fadeTime, function() {
    $('#cart-subtotal').html(subtotal.toFixed(2));
    $('#cart-tax').html(tax.toFixed(2));
    $('#cart-shipping').html(shipping.toFixed(2));
    $('#cart-total').html(total.toFixed(2));
    if(total == 0){
      $('.checkout').fadeOut(fadeTime);
    }else{
      $('.checkout').fadeIn(fadeTime);
    }
    $('.totals-value').fadeIn(fadeTime);
  });

  /* Send HTTP POST request to update_quantity endpoint */
  $.post('http://127.0.0.1:8000/addtocart/', {'quantity': quantity}, function(data){
    console.log(data);
  });
}
