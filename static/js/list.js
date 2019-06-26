$(function(){
	// $.session.set('openid', '2222')

	// if($.session.get('openid')){
   // console.log('成功')
   //  window.open('http://skin.gouzao.tech/list ')
   //
   //  }else{
   //  console.log('失败')
   //  window.open('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx05a1d3717dc54a3a&redirect_uri=http://skin.gouzao.tech/list&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect');
   //
   //   }
     $.ajax({
		     type: 'GET',
		     url: 'http://skin.gouzao.tech/allorders',
		     // url: 'http://www.baidu.com',
		     dataType:'json',
		     success: function(res){
		    	console.log(res)
		    	var list = res
		    	var html = ''
		    	console.log(res)
		    	$.each(list,function(index,item){
		    		console.log(item.order_shopid[0][2],'dddd')
					console.log(item.order_shopid[0][3],'wwwwwwwww')

					html += `
					    <div class="list">
						<div class="title"><span>${item.order_project}</span>－<span>${item.order_activity}</span></div>
						<div class="con">
							<div class="left">
								<img src="${item.order_img}" alt="未加载">
							</div>
							<div class="right">
								<div class="sj">预约时间：<span>${item.order_date}</span>  <span>${item.order_time} </span> </div>
								<div class="dz">
									<span class="s1"> 店铺地址：</span>
									<span class="s2"> ${item.order_shopid[0][2]}</span></div>
								<div class="bh">联系电话：<span>${item.order_shopid[0][3]}</span> </div>
								<div class="bh">订单编号：<span>${item.order_id}</span> </div>
								<div class="jq"> <span>价钱:¥</span> <span class="qian">${item.order_price}</span></div>

							</div>
						</div>
					    </div>
					    <div class="deites">
					       <div class="typ">预约人：<span>${item.order_username}</span> </div>
						   <div class="typ">联系电话：<span>${item.order_phone}</span> </div>
						   <div class="typ1">留言备注：<span>${item.order_liuyan}</span> </div> 
                        </div>
					   `
		    	})
		    	console.log(html);  
		    	$(".content").html(html);


		    	//点击出现详情
				 $(".list").click(function () {

				 	$(this).next(".deites").slideToggle();

				 })
				 $(".deites").click(function () {

					 $(this).slideToggle();

				 })










		    	// $.each($('.por'	), function(i,n) {
		    	// 	$(this).click(function(){
		    	// 		console.log($(this).data('filter'))	
		    	// 		var id = $(this).data('filter')
		    	// 		 url = "class.html?procid="+id;//此处拼接内容
       //     				 window.location.href = url;
		    	// 	})
		    	// })

		     }
		    
		 
		});
		
});













