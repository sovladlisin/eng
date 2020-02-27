jQuery(window).on("load", function () {
	$(".se-pre-con").fadeOut("slow");


	"use strict";

	$("img").click(function () {
		var $src = $(this).attr("src");
		$(".show").fadeIn(3);
		$(".img-show img").attr("src", $src);
		$(".img-show").width($(".img-show img").width())
	});

	$("span, .overlay").click(function () {
		$(".show").fadeOut(3);
	});
});