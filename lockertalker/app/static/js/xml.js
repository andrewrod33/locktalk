$(document).ready(function(){

	$.ajax(
		{
			url: 'http://proxy-rocketu.rhcloud.com/rocketu-api/',	
			type: 'GET',
			dataType: 'xml',
			data:{
				url: 'http://fulltextrssfeed.com/feeds.sbnation.com/rss/current',
			},
			success: function(json) {
				console.log(json);
		
				}
			}
	);
});