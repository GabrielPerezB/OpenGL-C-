var data = [

];

$(document).ready(function(){
	start();
	$("#Options li").click(function(e){
		var value = this.value;
		$("#info").text(data);
		changeStyle(this);
	});
});

function changeStyle(element){
	$("#Options li").removeClass("selected");
	$(element).addClass("selected");
}

function start(){
	$("#First").addClass("selected");
	$("#info").text(data);
}