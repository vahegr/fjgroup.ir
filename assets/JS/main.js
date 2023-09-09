$(document).ready(function() {
    $(".projectType1").click(function() {
        $(".xicon1").toggleClass("hidden");
        $(".office").toggleClass("nothidden");
    });

    $(".projectType2").click(function() {
        $(".xicon2").toggleClass("hidden");
    });

    $(".projectType3").click(function() {
        $(".xicon3").toggleClass("hidden");
    });

    $(".projectType4").click(function() {
        $(".xicon4").toggleClass("hidden");
    });

    $(".projectType5").click(function() {
        $(".xicon5").toggleClass("hidden");
    });

    $(".projectType6").click(function() {
        $(".xicon6").toggleClass("hidden");
    });

    $(".projectType7").click(function() {
        $(".xicon7").toggleClass("hidden");
    });

    $(".projectType8").click(function() {
        $(".xicon8").toggleClass("hidden");
    });

    $(".projectType9").click(function() {
        $(".xicon9").toggleClass("hidden");
    });

    $(".projectType10").click(function() {
        $(".xicon10").toggleClass("hidden");
    });

    $(".projectType11").click(function() {
        $(".xicon11").toggleClass("hidden");
    });

    $(".projectType12").click(function() {
        $(".xicon12").toggleClass("hidden");
    });

    $(document).on('click', function() {
        $('.collapse').collapse('hide');
    });

    $('.projectType').click(function() {
        var category = $(this).data('filter'); // Get the category from the data-filter attribute

        // Remove the active class from all buttons
        $('.projectType').removeClass('active');

        // Add the active class to the clicked button
        $(this).addClass('active');

        // Show or hide the boxes based on the category
        $('.container .row .col-md-4').each(function() {
            if ($(this).hasClass(category)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});