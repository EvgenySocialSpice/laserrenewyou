$(document).ready(function() {

    $("#contactform").submit(function() {
		$.ajax({
			type: "POST",
			url: "../mail.php",
			data: $(this).serialize()
		}).done(function() {
			//$(this).find("input").val("");
			alert("Thank you for your email we'll contact you in a minute :)!");
            $("#contactform").trigger("reset");
		});
		return false;
	});
	
});