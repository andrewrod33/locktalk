$(document).ready(function(){
	function car(make,color,speed){
		this.make = make
		this.color = color
		this.speed = speed

		this.setSpeed = setSpeed;
		function setSpeed(speed){
			this.speed = speed;

		}
	}	

		var myCar =  new car('Scion', 'red', '60');
		console.log(myCar);

		$('h1').html('Virtual car('myCar.color + ' ' + myCar.make+ ')' );

		myCar.setSpeed(100);

});