$(function(){
    //接受上个页面带来参数
     function getUrlParam(name) {   
             var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象  
             var r = window.location.search.substr(1).match(reg);  //匹配目标参数   
             if (r != null) return unescape(r[2]); return null; //返回参数值  
        }
     var Id=getUrlParam("actid");
     var userId=getUrlParam("userId");
     console.log(Id)
    var now = new Date();
    var time = now.getFullYear() + "-" +((now.getMonth()+1)<10?"0":"")+(now.getMonth()+1)+"-"+(now.getDate()<10?"0":"")+now.getDate();
    $('#udate').val(time)
    $('#udate').attr('min',time)

    $.ajax({
		     type: 'GET',
		     url: 'http://skin.gouzao.tech/actinfo',
		     dataType:'json',
             data: {
               actid:Id
             },
         success: function(res){
		     console.log(res,'1kkqkskqdshnqkhwjdsgqjdsgjgjjjjj')
             var time = res.ptime
             console.log(time)
             //护理类型
                 var html = ''
                 var html1= ''

          $(".ptype").html(res.protype_name);
          $(".pname").html(res.pname);
          $(".infors").html(res.pinfo);
             $("#dm").html(res.shops[0].dianpu_name);
             $(".address1").html(res.shops[0].dianpu_place);
             $(".tel").html(res.shops[0].dianpu_phone);
             //默认给姓名和电话
             console.log(res.dquser[0])
             console.log(res.dquser[1])
             $('#uname').val(res.dquser[0])
             $('#utel').val(res.dquser[1])


           //店名
          $.each(res.shops,function(index,item){
            html += `<li class="${item.dianpu_id}">${item.dianpu_name}</li>`,
              $(".two-bar").html(html);
          })



             $(".two-bar1").html(html1);
             $(".dian").click(function(){


                 console.log("ssssssssssss")
                 var dimg = $(".down").attr("src");
               console.log("bbbbbb",dimg)
                 if(dimg == "static/img/up.png"){
                   $(".down").attr("src","static/img/down.png");
                 }else {
                     $(".down").attr("src","static/img/up.png");
                 }

                 $(this).next().slideToggle();


             });



             $(".two-bar li").click(function(){
                 $(".two-bar1").html('')

                 $(".down").attr("src","static/img/down.png");

                 //清空美容师和日期
                 $("#ry").html("不指定美容师");
                 $("#udate").val(" ");



                 $("#sjj").html("请选择服务时间");




                 console.log( $(this).attr("class"))
                 var id1 = parseInt($(this).attr("class"))
                 var dian = $(this).html()
                 //相对应的地址和电话
                 $.each(res.shops,function(index,item){
                     // console.log('hhhhhhhhhh',item.dianpu_id)
                     if(item.dianpu_id == id1){
                         var adr = item.dianpu_place
                         var tel1  = item.dianpu_phone
                         $(".address1").html(adr);
                         $(".tel").html(tel1);

                     }

                 });


                 $("#dm").html(dian);
                 var soid = $("#dm").attr('class',id1);
                 $(".two-bar").slideToggle();
                 $('.address').html()
             });








          $(".fan").click(function(){
          console.log(11)
          url = "class.html?procid="+userId;//此处拼接内容
                   window.location.href = url;
          });



        $(".people").click(function(){
            html1 = ''

          $(this).next().slideToggle();
            //服务员

            var soid = $("#dm").attr('class');
            $.ajax({
                type:'GET',
                url:'http://skin.gouzao.tech/sptwt',
                dataType:'json',
                data: {
                    shopid:soid
                },
                success: function(res){
                    console.log(res,'ssjjsjefhewrhgjurhgjrgrgjrjgjr')
                    $.each(res,function(index,item){
                        console.log('cxcwc',item)
                        html1+= `<li class='${item.dianyuan_id}'>${item.dianyuan_name}</li>`
                    })
                    $('.two-bar1').html(html1)
                    var now = "<li class='0'>不指定美容师</li>"
                    $('.two-bar1').append(now)
                    $(".two-bar1 li").click(function(){


                        var pid = $(this).attr("class")
                        var people = $(this).html()
                        $("#ry").html(people);
                        $("#ry").attr("class",pid);
                        $(".two-bar1").slideToggle();

                    });

                }

            })






        });
        //选择有效时间


        $("#sj").click(function(){

            //判断是否填写日期
            var udat = $("#udate").val()
            console.log(udat,"当前日期")
            if(udat){


                var dimg = $(".down1").attr("src");
                console.log("bbbbbb",dimg)
                if(dimg == "static/img/up.png"){
                    $(".down1").attr("src","static/img/down.png");
                }else {
                    $(".down1").attr("src","static/img/up.png");
                }
                console.log('time',time)
                var wid = $('#ry').attr('class')
                console.log('wid',wid)
                var data = $('#udate').val()
                console.log('data',data)
                var yxtime = ''
                var shoid=  $("#dm").attr("class")
                console.log(shoid,'qqwwqwqwqwqwqw')
                $.ajax({
                    type: 'GET',
                    url: 'http://skin.gouzao.tech/order_send',
                    dataType:'json',
                    data: {
                        ptime:time,
                        waiter:wid,
                        order_date:data,
                        shopid:shoid,
                    },
                    success:function (res) {











                    console.log(res[0],'嘻嘻嘻嘻嘻嘻嘻')
                    $.each(res[0],function (index,item) {

                        // 判断是否存在有效时间
                        if(index == 404){
                            alert("当前日期无可预约时间段，请选择其他日期")
                        }else {
                            console.log(item,'item')


                            var ins = index
                            var ints = item[0]
                            var timewaiteid  = item[1]
                            console.log(ints,'ints')
                            console.log(ins,'ins')
                            console.log(timewaiteid,'timewaiteid')
                            //
                            yxtime += `<li class="${ins}_${timewaiteid}">${ints}</li>`
                            $(".two-bar2").html(yxtime);
                            // var intess = ints[1]
                            // console.log(intess,'data')
                            // console.log(res[0],'time')



                        }





                    })
                    console.log(res[0],'time')
                    $(".two-bar2").slideToggle();
                    console.log('qadkqdsk')
                    $(".two-bar2 li").click(function(){
                        $(".down1").attr("src","static/img/down.png");
                        var time = $(this).html()
                        var timid = $(this).attr('class')

                        $("#sjj").text(time);
                        $("#sj").attr("class",timid)

                        $(".two-bar2").slideToggle();
                    });
                    $("#udate").change(function(){
                        console.log("当日期发生改变时清空之前的有效时间")
                        $(".two-bar2").html("");
                        $("#sjj").html("请选择服务时间");
                        $(".down1").attr("src","static/img/down.png");

                    });


                    },
                    error(){
                        console.log("有效时间出错")

                    }
                })
                console.log(udat,"当前日期")
            }else {
                alert("请先选择日期")
            }



        });

        $(".s2").html(res.pprice);
         

            // 
            // var utel = 
            // var uwaiter = 
            // var uact = 
            // var uly =
           $(".yy").click(function(){
               var yanmes = $("#uname").val();
               var ytes = $("#utel").val();
               var ydats = $("#udate").val();
               var ytims = $("#sjj").html();

               console.log(2222)
                   console.log($(".ynams").html(),"wwww")
                   console.log($(".yt").val(),"dddddd")

               console.log(yanmes,"名字长度")
               console.log(ytes,"电话长度")
               console.log(ydats,"日期长度")
               console.log(ytims,"时间")


               if(yanmes && ytes && ydats && ytims !== "请选择服务时间"){

                   console.log(1111111)
                   $("#zzc").show()
                   $(".mtk").show()
                   $(".pi").html(res.protype_name);
                   $(".cp").html(res.pname);
                   $(".ddz").html($(".address1").html());
                   $(".ddh").html($(".tel").html());
                   $(".ynams").html($(".yx").val());
                   $(".yte").html($(".yt").val());
                   $(".ydat").html($("#udate").val());
                   $(".ytim").html($("#sjj").html());
               }else {
                  alert("请完善预约信息")

               }












                // var uname = $('#uname').val()
                // var utel = $('#utel').val()
                // var uwaiter = $('#ry').attr('class')
                // var uly = $('#text').val()
                // var uact = $('.pname').html()
                // var utype = res.protype_id
                //
                // var utime = $('#sj').text()
               // $.ajax({
               //     type: 'GET',
               //
               //     url: 'http://skin.gouzao.tech/orprces',
               //
               //     dataType:'json',
               //     data: {
               //      order_username:uname,
               //      order_phone:utel,
               //      order_waiter:uwaiter,
               //      order_activity:uact,
               //      order_acttype:utype,
               //      order_liuyan:uly,
               //     },
               //    success:function(res){
               //      console.log(res)
               //      // url = "/list?actid="+id+"&userId="+userId"//此处拼接内容
               //      url = "/list"//此处拼接内容
               //
               //      // url = "list.html?actid="+id+"&userId="+userId//此处拼接内容
               //     window.location.href = url;
               //
               //    }
               // })
                
           });
           $(".close").click(function () {
               $("#zzc").hide()
               $(".mtk").hide()
           });
           //点击确定
             $(".sure").click(function () {

                  var uname = $(".yx").val()
                  var utel = $(".yt").val()
                  var uwaiter = $('#ry').attr('class')
                  var uly = $('#text').val()
                  var uact = $('.pname').html()
                  var utype = res.protype_id
                 // console.log('time',time)
                 // var wid = $('#ry').attr('class')
                 // console.log('wid',wid)
                 var data = $('#udate').val()
                 // console.log('data',data)
                 var  tId = $("#sj").attr("class")

                  var utime = $('#sj').text()
                var sid=  $("#dm").attr("class")
                 var arr=new Array();
                 var claas = $("#sj").attr("class")
                 arr = claas.split('_');
                 var timeindex = arr[0]
                 var timewaite = arr[1]
                 console.log("时间的index值",timeindex)
                 console.log("时间的服务员id值",timewaite)
                 $.ajax({
                     type: 'GET',

                     url: 'http://skin.gouzao.tech/orprces',
                     // url: 'http://skin.gouzao.tech/index',

                     dataType:'json',
                     data: {
                      order_username:uname,
                      order_phone:utel,
                      order_waiter:timewaite,
                      order_activity:uact,
                      order_acttype:utype,
                      order_liuyan:uly,
                      o_date:data,
                      o_time:utime,
                      o_timenum:timeindex,
                      shopId:sid,
                     },
                    success:function(res){
                      console.log(res)
                        window.location.href = "/list";

                    },
                    error:function (){
                      alert('预约失败')
                    }

                 })


             })

		     }
		





		});



});













