const message = document.getElementById("message");
function filter() {
	let text = message.value;
	let pattern = /(ha+)|(HA+)|(hA+)|(Ha+)|(he+)|(HE+)|(hE+)|(He+)/gi;
	let result = text.replace(pattern, "$1 $2 $3 $4 $5 $6 $7 $8");
	document.getElementById("demo").innerHTML = result;
}