$(document).ready(function(){
	//выбор долота
	$("#doloto").on('change ready',function(){
		var dlt = $("#doloto option:selected").attr('id');

		//$("#doloto").each(function (index, elem) {
		//	if($(this).val()==$("#doloto").val()){
		//		dlt = $(elem).attr('id');
		//	}
		//});
		$.ajax({
		type:'GET',
		url:'change',
		data: { 'dolotoDim': dlt },
		success:function(data){
			$("#ybt").html('');
			var dan = data;
			$(dan).each( function(index,value){
				var pynkt ="<option id="+value.id+">"+value.ybtDim+"</option>";
				$("#ybt").append(pynkt);
			});
			
		},
		error:function(){
			alert('loll');
		},
		});
		return false;
	});

	//выбор утяжеленной бурильной колоны
	$("#ybt").change(function(){
		ybt = $("#ybt option:selected").attr('id');
		//$("#ybtList>option").each(function (index, elem) {
		//	if($(this).val()==$("#ybt").val()){
		//		ybt = $(elem).attr('id');
		//	}
		//});
		$.ajax({
			type:'GET',
			url:'selectYbt',
			data: { 'ybtDim': ybt },
			success:function(data){
				$("#casing").html('');
				var dan = data;
				$(dan).each( function(index,value){
				var pynkt ="<option id="+value.id+">"+value.casingDim+"</option>";
				$("#casing").append(pynkt);
				});
			},
			error:function(){
				alert('Не работает');
			},
		});
		return false;
	});
	//выбор обсадной колонны
	$("#casing").change(function(){
		cas = $("#casing option:selected").attr('id');
		//$("#casingList>option").each(function (index, elem) {
		//	if($(this).val()==$("#casing").val()){
		//		cas = $(elem).attr('id');
		//	}
		//});
		$.ajax({
			type:'GET',
			url:'selectCasing',
			data: { 'casingDim': cas },
			success:function(data){
				$("#boring").html('');
				var dan = data;
				$(dan).each( function(index,value){
				var pynkt ="<option id="+value.id+">"+value.casingDim+"</option>";
				$("#boring").append(pynkt);
				});
			},
			error:function(){
				alert('Не работает');
			},
		});
		return false;
	});
	var list_Engine = "";
	$('#haveEngine').change(function(){
		if($("#haveEngine").prop("checked")==true){
			$('#engine').html(list_Engine);
		}else{
			list_Engine = $('#engine').html();
			$('#engine').html('');
		}
	});
});