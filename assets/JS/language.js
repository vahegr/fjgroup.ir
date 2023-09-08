$(document).ready(function() {
    $(".FA").addClass("d-none");
    $(".FA").addClass("text-center");
    $(".FA").attr("dir", "rtl");

    $("#lang").click(function() {
        var currentText = $(this).text();
        var newText = (currentText === "FA") ? "EN" : "FA";
        $(this).text(newText);

        if ($(".FA").hasClass("d-none")) {
            $(".FA").removeClass("d-none");
            $(".FA").addClass("d-block");
            $(".EN").addClass("d-none");
        } else {
            $(".FA").addClass("d-none");
            $(".EN").removeClass("d-none");
            $(".EN").addClass("d-block");
        }

        if ($("#lang").text() === "FA") {
            $(".navitem").addClass("px-2");
            $(".navitem").removeClass("px-3");
        } else {
            $(".navitem").removeClass("px-2");
            $(".navitem").addClass("px-3");
        }
    });
});