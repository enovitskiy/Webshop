/*!Filter price*/
  $( function() {
    $( "#slider" ).slider({
      range: true,
      min: 0,
      max: 10,
      values: [ 2, 8 ],
      step: 1,
      slide: function( event, ui ) {
        $( "#id_price_0" ).val( ui.values[ 0 ]);
         $( "#id_price_1" ).val(ui.values[ 1 ] );
         $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }

                             });

     $( "#amount" ).val( "$" + $( "#slider" ).slider( "values", 0 ) +
      " - $" + $( "#slider" ).slider( "values", 1 ) );
  } );


/*Detailproduct*/
  $("a.quick-view[data-toggle='modal']").on('click', function () {
            var href = $(this).attr('title');

            console.log(href)
            $.ajax({url:href +'product/',
                    data:{'href':href},
                    success: function (data) {

                    $('#productModalPet').html(data)
                    console.log(data)

                    }});
                                                                  })