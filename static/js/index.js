// function getCookie(key){
//     var arr1=document.cookie.split("; ");//由于cookie是通过一个分号+空格的形式串联起来的，所以这里需要先按分号空格截断,变成[name=Jack,pwd=123456,age=22]数组类型；
//     for(var i=0;i<arr1.length;i++){
//         var arr2=arr1[i].split("=");//通过=截断，把name=Jack截断成[name,Jack]数组；
//         if(arr2[0]==key){
//             return decodeURI(arr2[1]);
//         }
//     }
// }
// if(getCookie("ssss")){
//    console.log('111')
//     // window.open('http://skin.gouzao.tech/index ')
//
// }else{
//     console.log('222')
//     // window.open('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx05a1d3717dc54a3a&redirect_uri=http://skin.gouzao.tech/index&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect');
//
// }



$(function(){
	// $.session.set('openid', '2222')

	// if($.session.get('openid')){
   // console.log('成功')
   //  window.open('http://skin.gouzao.tech/index ')
   //
   //  }else{
   //  console.log('失败')
   //  window.open('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx05a1d3717dc54a3a&redirect_uri=http://skin.gouzao.tech/index&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect');
   //
   //   }
		$.ajax({

		     type: 'GET',

		     url: 'http://skin.gouzao.tech/protychos',

		     dataType:'json',

		    success: function(res){
		    	console.log(res)
		    	var list = res
		    	var html = ''
		    	 // <img src='${item.aimg}'>
		    	console.log(res)
		    	$.each(list,function(index,item){
		    		html += `<div class="por" href="/class" data-filter=${item.procid}>
							<div class="pbg"><img src='${item.aimg}'></div>
							<div class="des">
							  <div class="name">${index}</div>
							  <div class="des1"> ${item.content}</div>
								<div>
									<span class="jq">¥${item.min_price}-¥${item.max_price}</span>
									<div class="yy">查看</div>
									</div>
								</div>
								<img src="" class="sale">
						    </div>
					 </div>`
		    	})
		    	// console.log(html);
		    	$(".content").html(html);
		    	$.each($('.por'	), function(i,n) {
		    		$(this).click(function(){
		    			console.log($(this).data('filter'))
		    			var id = $(this).data('filter')
		    			 url = "/class?procid="+id;//此处拼接内容
           				 window.location.href = url;
		    		})
		    	})
		    },
		 
		});

});