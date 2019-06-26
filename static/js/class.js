$(function(){
	var curr = 0;
	$("#jsNav a.trigger").each(function(i){
		$(this).click(function(){
			curr = i;
			$("#js img").eq(i).fadeIn("fast").siblings("img").fadeOut("fast");
			$(this).addClass("imgSelected").siblings().removeClass("imgSelected");
		});
	});
	var timer = setInterval(function(){
		var go = (curr + 1) % 5;
		$("#jsNav a.trigger").eq(go).click();
	},3000);
	$("#js,#next,#prev").hover(function(){
		clearInterval(timer);
	},function(){
		timer = setInterval(function(){
		var go = (curr + 1) % 5;
		$("#jsNav a.trigger").eq(go).click();
	},3000);
	});
	$("#next").click(function(){
		if(curr == 4){
			var go = 0;
		}else{
			var go = (curr + 1) % 5;
		}
		$("#jsNav a.trigger").eq(go).click();
	});
	$("#prev").click(function(){
		if(curr == 0){
			var go = 4;
		}else{
			var go = (curr - 1) % 5;
		}
		$("#jsNav a.trigger").eq(go).click();
	});


	$(".area").hover(function(){

	  $(this).find(".qq").show(100);}

	  ,function(){

		$(this).find(".qq").hide(100);

	});
  	
  	 function getUrlParam(name) {   
             var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象  
             var r = window.location.search.substr(1).match(reg);  //匹配目标参数   
             if (r != null) return unescape(r[2]); return null; //返回参数值  
        }
     var userId=getUrlParam("procid");
     // var userId=Server.proid("proid")
     console.log(userId)


     $.ajax({

		     type: 'GET',

		     url: 'http://skin.gouzao.tech/projechos',

		     dataType:'json',
		     data: { 
		     	proid:userId 
		     },
		    success: function(res){
		    	console.log(res)
		    	// console.log("ecwec",userId)
		    	var html = ''
		    	var html1 = ''
		    	var html2 = ''
		    	var lian =res[0].aprice
		    	var shenti = res[1].aprice
		    	var quans = res[2].aprice
		    	$('#lian').html(lian)
		    	$('#shenti').html(shenti)
		    	$('#quans').html(quans)
		    	html = `<div  class=${res[0].aid}></div>`
		    	html1 = `<div class=${res[1].aid}></div>`
		    	html2 = `<div  class=${res[2].aid}></div>`
				console.log("SDWdwawda")
				console.log("ecwec.gugyu.g.g.",res[0].aid)
		    	$("#no").html(html);
		    	$("#no1").html(html1);
		    	$("#no2").html(html2);
		    	$('.tou').click(function(){
		    		// console.log($('#no div').data('filter'))
		    		// console.log($(this).data('filter'))	
		    			var id1 = $('#no div').attr('class')
		    			 url = "/des?actid="+id1+"&userId="+userId//此处拼接内容
           				 window.location.href = url;
		    	})
		    	$('.shenti').click(function(){
		    		// console.log($('#no1 div').data('filter'))
		    		// console.log($(this).data('filter'))	
		    			var id2 = $('#no1 div').attr('class')
					// console.log(id)
		    			 url = "/des?actid="+id2+"&userId="+userId;//此处拼接内容
           				 window.location.href = url;
		    	})
		    	$('.quans').click(function(){
		    		// console.log($('#no2 div').data('filter'))
		    		// console.log($(this).data('filter'))	
		    			var id3 = $('#no2 div').attr('class')
					// console.log(id)
		    			 url = "/des?actid="+id3+"&userId="+userId;//此处拼接内容
           				 window.location.href = url;
		    	})
		    },
		 
		});




});













