webpackJsonp([24],{269:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=i(474),l=i.n(a);for(var n in a)"default"!==n&&function(t){i.d(e,t,function(){return a[t]})}(n);var o=i(880),s=i.n(o),r=i(1),u=r(l.a,s.a,!1,null,null,null);u.options.__file="src/views/advanced-router/component/info_edit.vue",e.default=u.exports},474:function(t,e,i){"use strict";function a(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var l=i(7),n=(a(l),i(97)),o=a(n);e.default={data:function(){return{formValidate:{list1:"",list2:"",list3:null},ruleValidate:{},file:null,isfalse:!1,uploadImg:{url:this.$route.query.img},cityList:[],uploadList:[],TypeList1:[],TypeList2:[],TypeList3:[]}},computed:{upLoadData:function(){return{Id:this.$route.query.Id,mid:this.formValidate.list3}}},methods:{HangType1:function(){this.two_type()},HangType2:function(){this.three_type()},HangImg:function(){null===this.formValidate.list3?this.$Message.error("请选择车型"):null===this.file?this.$Message.error("请选择要修改的车辆图片"):(this.$refs.upload.post(this.file),this.$router.push({path:"/info/info_list"}))},HangRecall:function(){this.$router.push({path:"/info/info_list"})},handleUpload:function(t){var e=this;this.file=t;var i=new FileReader;return i.readAsDataURL(t),i.onloadend=function(){e.uploadImg={url:i.result,file:t}},!1},uploadSuccess:function(t,e,i){console.log("后端返回数据",t),console.log("当前上传文件",e),console.log("整个input file 里的文件数组",i)},one_type:function(){var t=this;this.axios({url:"https://www.mesonychid.com/taxi5/index/index/brand_table",method:"post",data:o.default.stringify({})}).then(function(e){t.TypeList1=e.data.table}).catch(function(e){t.$Message.error("请求超时,请稍后再试...")})},two_type:function(){var t=this;this.axios({url:"https://www.mesonychid.com/taxi5/index/index/series_table",method:"post",data:o.default.stringify({bid:this.formValidate.list1})}).then(function(e){t.TypeList2=e.data.table}).catch(function(e){t.$Message.error("请求超时,请稍后再试...")})},three_type:function(){var t=this;this.axios({url:"https://www.mesonychid.com/taxi5/index/index/series_table",method:"post",data:o.default.stringify({sid:this.formValidate.list1,bid:this.formValidate.list2})}).then(function(e){t.TypeList3=e.data.table}).catch(function(e){t.$Message.error("请求超时,请稍后再试...")})}},mounted:function(){this.one_type()}}},880:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("Card",{attrs:{shadow:""}},[i("Form",{ref:"formValidate",attrs:{model:t.formValidate,rules:t.ruleValidate,"label-width":80}},[i("FormItem",{attrs:{label:"车型1"}},[i("Select",{staticStyle:{width:"200px"},on:{"on-change":t.HangType1},model:{value:t.formValidate.list1,callback:function(e){t.$set(t.formValidate,"list1",e)},expression:"formValidate.list1"}},t._l(t.TypeList1,function(e){return i("Option",{key:e.Id,attrs:{value:e.Id}},[t._v(t._s(e.name))])}))],1),t._v(" "),i("FormItem",{attrs:{label:"车型2"}},[i("Select",{staticStyle:{width:"200px"},on:{"on-change":t.HangType2},model:{value:t.formValidate.list2,callback:function(e){t.$set(t.formValidate,"list2",e)},expression:"formValidate.list2"}},t._l(t.TypeList2,function(e){return i("Option",{key:e.Id,attrs:{value:e.Id}},[t._v(t._s(e.name))])}))],1),t._v(" "),i("FormItem",{attrs:{label:"车型3"}},[i("Select",{staticStyle:{width:"200px"},on:{"on-change":function(t){}},model:{value:t.formValidate.list3,callback:function(e){t.$set(t.formValidate,"list3",e)},expression:"formValidate.list3"}},t._l(t.TypeList3,function(e){return i("Option",{key:e.Id,attrs:{value:e.Id}},[t._v(t._s(e.name))])}))],1),t._v(" "),i("FormItem",{attrs:{label:"图片上传"}},[i("div",{staticStyle:{display:"flex","align-items":"end"}},[i("Upload",{ref:"upload",attrs:{multiple:t.isfalse,"show-upload-list":!1,"before-upload":t.handleUpload,"on-success":t.uploadSuccess,data:t.upLoadData,action:"https://www.mesonychid.com/taxi5/admin/Drive/update"}},[i("Button",{attrs:{type:"ghost",icon:"ios-cloud-upload-outline"}},[t._v("浏览")])],1),t._v(" "),i("img",{staticStyle:{width:"auto",height:"150px","margin-left":"10px"},attrs:{src:t.uploadImg.url,alt:""}})],1)]),t._v(" "),i("FormItem",[i("Button",{attrs:{type:"primary"},on:{click:t.HangRecall}},[t._v("返回")]),t._v(" "),i("Button",{attrs:{type:"primary"},on:{click:t.HangImg}},[t._v("确认修改")])],1)],1)],1)},l=[];a._withStripped=!0;var n={render:a,staticRenderFns:l};e.default=n}});