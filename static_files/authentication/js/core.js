var i = 0; 			// Start Point
var images = [];	// Images Array
var time = 3000;	// Time Between Switch
	 
// Image List
images[0] = "/static/authentication/img/reel1.png";
images[1] = "/static/authentication/img/reel2.png";
images[2] = "/static/authentication/img/reel3.png";
images[3] = "/static/authentication/img/reel4.png";
images[4] = "/static/authentication/img/reel5.png";
images[5] = "/static/authentication/img/reel6.png";

// Change Image
function changeImg(){
	document.slide.src = images[i];

	// Check If Index Is Under Max
	if(i < images.length - 1){
	  // Add 1 to Index
	  i++; 
	} else { 
		// Reset Back To O
		i = 0;
	}

	// Run function every x seconds
	setTimeout("changeImg()", time);
}

// Run function when page loads
window.onload=changeImg;