$(document).ready(function () {
	 $.ajax({
		 type: "GET",
		 url: "http://localhost:5000/api/market/1",
		 contentType: "application/json; charset=utf-8",
		 dataType: "jsonp",
		 crossDomain: true,
		 success: function (response) {
			 data = response[0];
			 console.log(data);
			 $('.greeting-id').append(response.id);
			 $('.greeting-content').append(response.content);
		 },
		 failure: function (response) {
			 
		 }
	 });
 });
