"use strict"
let data = []

$(document).ready(() => {
	// hard code the typed text
	const refText = $('#toType').text();

	$('#textBody').keydown(event => {
		const typedText = document.getElementById('textBody').value;
		const sLength = typedText.length;

		let valeur = sLength / (refText.length) * 100;

		let refFraction = refText.substring(0, sLength);
		if ( 25 < levenshteinDistance(typedText, refFraction)) {
			alert("too many error");
		}

		$('.progress-bar').css('width', valeur+'%').attr('aria-valuenow', valeur);

		saveKeypress(event, true);
	});
	$('#textBody').keyup(event => {
		saveKeypress(event, false);
	});

	$('#submit').click(() => {
		sendData();
	});
});

function saveKeypress(event, isDown) {
	if (event.keyCode >= 65 && event.keyCode <= 90 ||
				event.keyCode == 188 ||
				event.keyCode == 190) {

		const action = (isDown) ? 0 : 1;
		data.push([event.keyCode, action, $.now()]);
	}
}

function sendData() {
	const json = JSON.stringify({"id": 1, "data": data});
	console.log(json);
	alert("");
	// $.post("https://www.google.ca/",json);
}

function levenshteinDistance (a, b) {
	if(a.length == 0) return b.length;
	if(b.length == 0) return a.length;

	var matrix = [];

	// increment along the first column of each row
	var i;
	for(i = 0; i <= b.length; i++){
		matrix[i] = [i];
	}

	// increment each column in the first row
	var j;
	for(j = 0; j <= a.length; j++){
		matrix[0][j] = j;
	}

	// Fill in the rest of the matrix
	for(i = 1; i <= b.length; i++){
		for(j = 1; j <= a.length; j++){
			if(b.charAt(i-1) == a.charAt(j-1)){
				matrix[i][j] = matrix[i-1][j-1];
			} else {
				matrix[i][j] = Math.min(matrix[i-1][j-1] + 1, // substitution
				Math.min(matrix[i][j-1] + 1, // insertion
				matrix[i-1][j] + 1)); // deletion
			}
		}
	}

	return matrix[b.length][a.length];
}
