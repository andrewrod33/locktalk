function login() {
	    	
	    	
}








$(document).ready(function(){
	$('#logout').on('click',function(){
		FB.logout(function(response) {
  // user is now logged out
  			console.log(response)
		});
	});
});