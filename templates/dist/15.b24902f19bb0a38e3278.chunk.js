webpackJsonp([15],{275:function(n,t,e){"use strict";function a(n){c||(e(943),e(945))}Object.defineProperty(t,"__esModule",{value:!0});var i=e(495),o=e.n(i);for(var s in i)"default"!==s&&function(n){e.d(t,n,function(){return i[n]})}(s);var d=e(947),r=e.n(d),c=!1,l=e(1),m=a,h=l(o.a,r.a,!1,m,null,null);h.options.__file="src/views/visit/directly.vue",t.default=h.exports},495:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=e(97),i=function(n){return n&&n.__esModule?n:{default:n}}(a);t.default={name:"text-editor",data:function(){var n=this;return{loadings:!0,model123:"",cityList123:[{value:"123",label:"New York"}],modal6:!1,loading:!1,data6:[],modal7:!1,formItem:{},formAdd:{},cityList:[],select:[],pageList:[],ajaxHistoryData:[],dataCount:0,pageSize:10,historyColumns:[{type:"selection",width:60,align:"center"},{title:"时间",key:"createTime"},{title:"负责人",key:"Leader"},{title:"负责人手机号",key:"phone"},{title:"公司名称",key:"name"},{title:"固定电话",key:"company_phone"},{title:"公司地址",key:"address"},{title:"地区",key:"column"},{title:"Action",key:"action",width:150,align:"center",render:function(t,e){return t("div",[t("Button",{props:{type:"primary",size:"small"},style:{marginRight:"5px"},on:{click:function(){n.hangEdit(e.row)}}},"修改"),t("Button",{props:{type:"error",size:"small"},on:{click:function(){n.hangRemove(e.row)}}},"删除")])}}],historyData:[],cityList_shi:[],cityList_city:[],cityList_dist:[],cityList_shi_edit:[],cityList_city_edit:[],cityList_dist_edit:[]}},created:function(){this.init(),this.handleListApproveHistory(),this.Get_shi(),this.Get_shi_edit(),this.category()},computed:{},methods:{category:function(){var n=this;this.axios({url:"Reference/show",method:"post"}).then(function(t){n.cityList=t.data.table,console.log(t,"1234")}).catch(function(n){})},hangsheng_edit:function(){this.Get_city_edit()},hangshi_edit:function(){this.Get_district_edit()},Get_shi_edit:function(){var n=this;this.axios({url:"Reference/get_shi",method:"post"}).then(function(t){n.cityList_shi_edit=t.data.table,200===t.data.code?n.$Message.success(t.data.msg):400===t.data.code&&n.$Message.error(t.data.msg)}).catch(function(n){})},Get_city_edit:function(){var n=this;this.axios({url:"Reference/get_citys",method:"post",data:i.default.stringify({shi_id:this.formItem.shi_name})}).then(function(t){n.cityList_city_edit=t.data.table}).catch(function(n){})},Get_district_edit:function(){var n=this;this.axios({url:"Reference/get_district",method:"post",data:i.default.stringify({city_id:this.formItem.city_name})}).then(function(t){n.cityList_dist_edit=t.data.table}).catch(function(n){})},hangsheng:function(){this.Get_city()},hangshi:function(){this.Get_district()},Get_shi:function(){var n=this;this.axios({url:"Reference/get_shi",method:"post"}).then(function(t){n.cityList_shi=t.data.table,200===t.data.code?n.$Message.success(t.data.msg):400===t.data.code&&n.$Message.error(t.data.msg)}).catch(function(n){})},Get_city:function(){var n=this;this.axios({url:"Reference/get_citys",method:"post",data:i.default.stringify({shi_id:this.formAdd.shi_name})}).then(function(t){n.cityList_city=t.data.table}).catch(function(n){})},Get_district:function(){var n=this;this.axios({url:"Reference/get_district",method:"post",data:i.default.stringify({city_id:this.formAdd.city_name})}).then(function(t){n.cityList_dist=t.data.table}).catch(function(n){})},handleSelectAll:function(){var n=this,t=this.select.map(function(n){return n.Id});console.log(t),this.axios({url:"Reference/directly_delete",method:"post",data:i.default.stringify({Id:t})}).then(function(t){200===t.data.code?(n.init(),n.handleListApproveHistory(),n.$Message.success(t.data.msg)):400===t.data.code&&n.$Message.error(t.data.msg)}).catch(function(t){n.$Message.error("请选择要删除的数据")})},handleRowChange:function(n,t){this.select=n},hangNew:function(){var n=this;this.axios({url:"Reference/directly_Add",method:"post",data:i.default.stringify({name:this.formAdd.name,cid:this.formAdd.type,phone:this.formAdd.phone,company_phone:this.formAdd.company_phone,shi_id:this.formAdd.shi_name,city_id:this.formAdd.city_name,dist_id:this.formAdd.dist_name,Leader:this.formAdd.Leader,address:this.formAdd.address})}).then(function(t){200===t.data.code?(n.init(),n.handleListApproveHistory(),n.$Message.success(t.data.msg),n.formAdd.name="",n.formAdd.type="",n.formAdd.phone="",n.formAdd.company_phone="",n.formAdd.shi_name="",n.formAdd.Leader="",n.formAdd.address=""):400===t.data.code&&(n.formAdd.input="",n.$Message.error(t.data.msg))}).catch(function(t){n.$Message.error("请求超时,请稍后再试...")})},cancel:function(){this.formAdd.name="",this.formAdd.type="",this.formAdd.phone="",this.formAdd.company_phone="",this.formAdd.shi_name="",this.formAdd.Leader="",this.formAdd.address=""},asyncOK:function(){var n=this;this.axios({url:"Reference/directly_update",method:"post",data:i.default.stringify({Id:this.$route.query.id,name:this.formItem.name,cid:this.formItem.type,phone:this.formItem.phone,company_phone:this.formItem.company_phone,shi_id:this.formItem.shi_name,city_id:this.formItem.city_name,dist_id:this.formItem.dist_name,Leader:this.formItem.Leader,address:this.formItem.address})}).then(function(t){200===t.data.code?(n.init(),n.handleListApproveHistory(),n.$Message.success(t.data.msg)):400===t.data.code&&n.$Message.error(t.data.msg)}).catch(function(t){n.$Message.error("请求超时,请稍后再试...")})},hangEdit:function(n){var t=this;this.modal6=!0,this.$router.push({query:{id:n.Id}}),this.axios({url:"Reference/directly_detail",method:"post",data:i.default.stringify({Id:n.Id})}).then(function(n){t.formItem.Leader=n.data.table.Leader,t.formItem.type=n.data.table.cid,t.formItem.name=n.data.table.name,t.formItem.phone=n.data.table.phone,t.formItem.company_phone=n.data.table.company_phone,t.formItem.shi_name=n.data.table.shi,t.formItem.city_name=n.data.table.city,t.formItem.dist_name=n.data.table.dist,t.formItem.address=n.data.table.address}).catch(function(n){t.$Message.error("请求超时,请稍后再试...")})},hangRemove:function(n){var t=this;this.axios({url:"Reference/directly_delete",method:"post",data:i.default.stringify({Id:n.Id})}).then(function(n){200===n.data.code?(t.init(),t.handleListApproveHistory(),t.$Message.success(n.data.msg)):400===n.data.code&&t.$Message.error(n.data.msg)}).catch(function(n){t.$Message.error("请求超时,请稍后再试...")})},init:function(){var n=this;this.axios({url:"Reference/directly_show",method:"post",data:i.default.stringify({})}).then(function(t){n.loadings=!1,n.data6=t.data.table}).catch(function(t){n.$Message.error("请求超时,请稍后再试...")})},handleListApproveHistory:function(){var n=this;this.axios({url:"Reference/directly_show",method:"post"}).then(function(t){n.loadings=!1,n.ajaxHistoryData=t.data.table,n.dataCount=t.data.table.length,t.data.table.length<n.pageSize?n.historyData=n.ajaxHistoryData:n.historyData=n.ajaxHistoryData.slice(0,n.pageSize)}).catch(function(t){n.$Message.error("请求超时,请稍后再试...")})},changepage:function(n){var t=(n-1)*this.pageSize,e=n*this.pageSize;this.historyData=this.ajaxHistoryData.slice(t,e)}}}},943:function(n,t,e){var a=e(944);"string"==typeof a&&(a=[[n.i,a,""]]),a.locals&&(n.exports=a.locals);e(16)("e3854b72",a,!1)},944:function(n,t,e){t=n.exports=e(15)(void 0),t.push([n.i,"/*@import '../../../styles/loading.less';*/\n",""])},945:function(n,t,e){var a=e(946);"string"==typeof a&&(a=[[n.i,a,""]]),a.locals&&(n.exports=a.locals);e(16)("2922a53d",a,!1)},946:function(n,t,e){t=n.exports=e(15)(void 0),t.push([n.i,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",""])},947:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=function(){var n=this,t=n.$createElement,e=n._self._c||t;return e("div",[e("div",[n._v("直属分公司")]),n._v(" "),e("Card",{attrs:{shadow:""}},[e("div",{staticStyle:{"margin-bottom":"10px"}},[e("Button",{attrs:{type:"info"},on:{click:function(t){n.modal7=!0}}},[n._v("新增")]),n._v(" "),e("Button",{attrs:{disabled:0===this.select.length},on:{click:n.handleSelectAll}},[n._v("全选删除")])],1),n._v(" "),e("Table",{attrs:{loading:n.loadings,"highlight-row":"",border:"",columns:n.historyColumns,data:n.historyData},on:{"on-selection-change":n.handleRowChange}}),n._v(" "),e("div",{staticStyle:{"text-align":"right"}},[e("Page",{staticClass:"paging",attrs:{total:n.dataCount,"page-size":n.pageSize,"show-total":""},on:{"on-change":n.changepage}})],1)],1),n._v(" "),e("Modal",{attrs:{title:"修改",loading:n.loading},on:{"on-ok":n.asyncOK},model:{value:n.modal6,callback:function(t){n.modal6=t},expression:"modal6"}},[e("Form",{attrs:{model:n.formItem,"label-width":90}},[e("FormItem",{attrs:{label:"负责人"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formItem.Leader,callback:function(t){n.$set(n.formItem,"Leader",t)},expression:"formItem.Leader"}})],1),n._v(" "),e("FormItem",{attrs:{label:"负责人手机号"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formItem.phone,callback:function(t){n.$set(n.formItem,"phone",t)},expression:"formItem.phone"}})],1),n._v(" "),e("FormItem",{attrs:{label:"公司名称"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formItem.name,callback:function(t){n.$set(n.formItem,"name",t)},expression:"formItem.name"}})],1),n._v(" "),e("FormItem",{attrs:{label:"固定电话"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formItem.company_phone,callback:function(t){n.$set(n.formItem,"company_phone",t)},expression:"formItem.company_phone"}})],1),n._v(" "),e("FormItem",{attrs:{label:"公司地址"}},[e("Select",{attrs:{filterable:"",placeholder:"省"},on:{"on-change":n.hangsheng_edit},model:{value:n.formItem.shi_name,callback:function(t){n.$set(n.formItem,"shi_name",t)},expression:"formItem.shi_name"}},n._l(n.cityList_shi_edit,function(t){return e("Option",{key:t.shi_id,attrs:{value:t.shi_id}},[n._v(n._s(t.shi_name))])})),n._v(" "),e("div",{staticStyle:{"margin-top":"10px"}},[e("Select",{attrs:{filterable:"",placeholder:"市"},on:{"on-change":n.hangshi_edit},model:{value:n.formItem.city_name,callback:function(t){n.$set(n.formItem,"city_name",t)},expression:"formItem.city_name"}},n._l(n.cityList_city_edit,function(t){return e("Option",{key:t.city_id,attrs:{value:t.city_id}},[n._v(n._s(t.city_name))])}))],1),n._v(" "),e("div",{staticStyle:{"margin-top":"10px"}},[e("Select",{attrs:{filterable:"",placeholder:"区"},model:{value:n.formItem.dist_name,callback:function(t){n.$set(n.formItem,"dist_name",t)},expression:"formItem.dist_name"}},n._l(n.cityList_dist_edit,function(t){return e("Option",{key:t.dist_id,attrs:{value:t.dist_id}},[n._v(n._s(t.dist_name))])}))],1)],1),n._v(" "),e("FormItem",{attrs:{label:"详细地址"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formItem.address,callback:function(t){n.$set(n.formItem,"address",t)},expression:"formItem.address"}})],1),n._v(" "),e("FormItem",{attrs:{label:"地区"}},[e("Select",{model:{value:n.formItem.type,callback:function(t){n.$set(n.formItem,"type",t)},expression:"formItem.type"}},n._l(n.cityList,function(t){return e("Option",{key:t.Id,attrs:{value:t.Id}},[n._v(n._s(t.name))])}))],1)],1)],1),n._v(" "),e("Modal",{attrs:{title:"新增"},on:{"on-cancel":n.cancel,"on-ok":n.hangNew},model:{value:n.modal7,callback:function(t){n.modal7=t},expression:"modal7"}},[e("Form",{attrs:{model:n.formAdd,"label-width":90}},[e("FormItem",{attrs:{label:"负责人"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formAdd.Leader,callback:function(t){n.$set(n.formAdd,"Leader",t)},expression:"formAdd.Leader"}})],1),n._v(" "),e("FormItem",{attrs:{label:"负责人手机号"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formAdd.phone,callback:function(t){n.$set(n.formAdd,"phone",t)},expression:"formAdd.phone"}})],1),n._v(" "),e("FormItem",{attrs:{label:"公司名称"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formAdd.name,callback:function(t){n.$set(n.formAdd,"name",t)},expression:"formAdd.name"}})],1),n._v(" "),e("FormItem",{attrs:{label:"固定电话"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formAdd.company_phone,callback:function(t){n.$set(n.formAdd,"company_phone",t)},expression:"formAdd.company_phone"}})],1),n._v(" "),e("FormItem",{attrs:{label:"公司地址"}},[e("Select",{attrs:{filterable:"",placeholder:"省"},on:{"on-change":n.hangsheng},model:{value:n.formAdd.shi_name,callback:function(t){n.$set(n.formAdd,"shi_name",t)},expression:"formAdd.shi_name"}},n._l(n.cityList_shi,function(t){return e("Option",{key:t.shi_id,attrs:{value:t.shi_id}},[n._v(n._s(t.shi_name))])})),n._v(" "),e("div",{staticStyle:{"margin-top":"10px"}},[e("Select",{attrs:{filterable:"",placeholder:"市"},on:{"on-change":n.hangshi},model:{value:n.formAdd.city_name,callback:function(t){n.$set(n.formAdd,"city_name",t)},expression:"formAdd.city_name"}},n._l(n.cityList_city,function(t){return e("Option",{key:t.city_id,attrs:{value:t.city_id}},[n._v(n._s(t.city_name))])}))],1),n._v(" "),e("div",{staticStyle:{"margin-top":"10px"}},[e("Select",{attrs:{filterable:"",placeholder:"区"},model:{value:n.formAdd.dist_name,callback:function(t){n.$set(n.formAdd,"dist_name",t)},expression:"formAdd.dist_name"}},n._l(n.cityList_dist,function(t){return e("Option",{key:t.dist_id,attrs:{value:t.dist_id}},[n._v(n._s(t.dist_name))])}))],1)],1),n._v(" "),e("FormItem",{attrs:{label:"详细地址"}},[e("Input",{attrs:{placeholder:""},model:{value:n.formAdd.address,callback:function(t){n.$set(n.formAdd,"address",t)},expression:"formAdd.address"}})],1),n._v(" "),e("FormItem",{attrs:{label:"地区"}},[e("Select",{model:{value:n.formAdd.type,callback:function(t){n.$set(n.formAdd,"type",t)},expression:"formAdd.type"}},n._l(n.cityList,function(t){return e("Option",{key:t.Id,attrs:{value:t.Id}},[n._v(n._s(t.name))])}))],1)],1)],1)],1)},i=[];a._withStripped=!0;var o={render:a,staticRenderFns:i};t.default=o}});