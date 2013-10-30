$(document).ready(function(){
	var teamId= JSON.parse(localStorage.getItem('getTeams'));
	console.log(teamId);
	
		
	function doAJAX(url){
		$.ajax(
			{
				url: 'http://api.espn.com/v1/sports/football/nfl/teams/'+ url +'/news/?apikey=6pz3x9tcb269689jvg23swm8',	
				type: 'GET',
				dataType: 'json',
				data:{
				},
				success: function(json) {
					console.log(json);
				$('ul#news').append(Mustache.render($("#new-news").html(), json  )
					)
					}
				}
		);
	

	/* $.ajax(
		{
			url: 'http://proxy-rocketu.rhcloud.com/rocketu-api/',	
			type: 'GET',
			dataType: 'json',
			data:{
				url: 'http://bleacherreport.com/api/front/lead_articles.json?tags="oakland-raiders"&devicetype=ipad&appversion=1.4&page=1&perpage=10'
			},
			success: function(json) {
				console.log(json);
			$('ul#news2').html(Mustache.render($("#all-news-template").html(), json  )
				)
				}
			}
	); */
	}
		for ( i=0; i<teamId.length; i++){
			console.log(i);
			doAJAX(teamId[i]);
		}

	   
	 

});
	
//url: 'http://api.espn.com/v1/sports/football/nfl/teams/13/news/?apikey=6pz3x9tcb269689jvg23swm8',
//url: 'http://api.espn.com/v1/now/?apikey=6pz3x9tcb269689jvg23swm8',
//url:'http://api.espn.com/v1/sports/news/headlines/top/?apikey=6pz3x9tcb269689jvg23swm8',
//url: 'http://api.espn.com/v1/sports/football/nfl?apikey=6pz3x9tcb269689jvg23swm8',
//url: 'http://api.espn.com/v1/sports//news/headlines/top/football/nfl?apikey=6pz3x9tcb269689jvg23swm8',
//url: 'http://api.espn.com/v1/sports/football/nfl/teams/13/news/?apikey=6pz3x9tcb269689jvg23swm8',
//http://bleacherreport.com/api/front/lead_articles.json?limit=10
//http://feeds.feedburner.com/sportsblogs/sbnation.xml
//url: 'http://feeds.feedburner.com/sportsblogs/sbnation.xml'
//http://bleacherreport.com/api/front/lead_articles.json?tags=oakland-raiders&devicetype=ipad&appversion=1.4&page=1&perpage=15
//http://bleacherreport.com/articles;feed?tag_id=16
//http://api.espn.com/v1/sports/football/nfl/athletes?apikey=6pz3x9tcb269689jvg23swm8