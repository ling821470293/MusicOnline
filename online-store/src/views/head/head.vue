<template>
  <div id="header" class="new_header">
    <div class="hd_bar">
      <div class="bd_bar_bd cle">
        <ul class="welcome">
          <li id="ECS_MEMBERZONE" v-if="userInfo.name">
            <router-link :to="'/app/home/member/userinfo'">{{userInfo.name}}</router-link>
          &nbsp;[<a @click="loginOut">退出</a>]
          </li>
          <li id="ECS_MEMBERZONE" v-else>
            <router-link :to="'/app/login'">请登录</router-link>
            <s>|</s>
            <router-link :to="'/app/register'">免费注册</router-link>
          </li>
        </ul>
        <ul id="userinfo-bar">
          <li class="more-menu"><i class="iconfont arrow"> </i>
            <router-link :to="'/app/home/member/userinfo'">会员中心</router-link>
          </li>
        </ul>
      </div>
    </div>
    <div class="hd_main cle">
      <div class="logo">
        <router-link to="/app/home/index" class="lizi_logo">
          <img src="../../static/images/head/music_logo.png" class="logo_img" alt="在线音乐网站">
        </router-link>
      </div>
      <div class="search_box">
        <input class="sea_input" type="text" name="keywords" id="keyword" v-model="searchWord" @keyup.enter="searchSubmit">
        <button  class="sea_submit" @click="searchSubmit">搜索</button>
      </div>
      <div class="head_search_hot">
       <span>热搜词：</span>
        <router-link v-for="item in hotSearch" :to="'/app/home/search/'+item.keywords" :key="item.keywords">
          {{item.keywords}}
        </router-link>
      </div>
    </div>
    <div class="hd_nav">
      <div class="hd_nav_bd cle">
        <div class="main_nav main_nav_hover" id="main_nav">
          <div class="main_nav_link" @mouseover="overAllmenu" @mouseout="outAllmenu">
            <a class="meunAll">全部歌曲分类
              <i class="iconfont icon-tubiao-"></i>
            </a>
            <div class="main_cata" id="J_mainCata" v-show="showAllmenu">
              <ul>
                <li class="first" v-for="(item,index) in allMenuLabel">
                  <h3>
                    <router-link :to="'/app/home/list/'+item.id">{{item.name}}</router-link>
                  </h3>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <ul class="sub_nav cle" id="sub_nav">
          <li>
            <router-link to="/app/home/index">首页</router-link>
          </li>
          <template v-for="(item,index) in allMenuLabel">
            <li>
              <div v-if="item.is_tab">
                <router-link :to="'/app/home/list/'+item.id" >{{item.name}}</router-link>
              </div>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import cookie from '../../static/js/cookie';
import { getHotSearch, getCategory} from  '../../api/api'
  export default {
    data(){
      return {
        hotSearch:[],//热词
        searchWord:'',//搜索词
        showAllmenu:false,//菜单显示控制
        allMenuLabel:[],//菜单
      }
    },
    computed: {
      ...mapGetters({
        songs_list: 'songs_list',
        userInfo:'userInfo'
      })
    },
    methods:{
      loginOut(){
        cookie.delCookie('token');
        cookie.delCookie('name');
        //跳转到登录
        this.$router.push({name: 'login'})
      },
      overAllmenu(){
        this.showAllmenu = true;
      },
      outAllmenu(){
        this.showAllmenu = false;
      },
      searchSubmit(){
        if(this.searchWord){
          //跳转到登录
          this.$router.push({ name: 'search', params: { keyword: this.searchWord }});
        }
      },
      clickHotWord(word){
        this.searchWord = word;
        //跳转搜索结果页
      },
      getMenu(){//获取菜单
        getCategory({
          params:{}
        }).then((response)=> {
          console.log(response)
          this.allMenuLabel = response.data
        })
        .catch(function (error) {
          console.log(error);
        });
      },
      getHotSearch(){//获取热搜
        getHotSearch()
        .then((response)=> {
            this.hotSearch = response.data
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    created(){
      this.getMenu()//获取菜单
      this.getHotSearch()//获取热词
    },
  }
</script>
<style scoped  lang='scss'>
  html {
    background:#fafafa;
    color:#333;
    _background-attachment:fixed
  }
html.isPhone {
    min-width:1196px
}
body,h1,h2,h3,h4,h5,h6,hr,p,blockquote,dl,dt,dd,ul,ol,li,pre,form,fieldset,legend,button,input,select,textarea,th,td {
    margin:0;
    padding:0
}
body,button,input,select,textarea {
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
ul,ol {
    list-style:none
}
a {
    text-decoration:none;
    color:#333;
    -webkit-transition:color .2s;
    -moz-transition:color .2s;
    -o-transition:color .2s;
    -ms-transition:color .2s;
    transition:color .2s
}
a:hover {
    color:#09c762
}
a:focus,area:focus {
    outline:0
}
fieldset,img {
    border:0
}

#header {
    background:#fff;
    zoom:1
}
#header .hd_main {
    width:1196px;
    margin:15px auto 0;
    position:relative;
    z-index:2001
}
#header .hd_main .logo_img{
    width: 68%;
    margin-top: 6px;
}
.new_header .search_result {
    margin:27px 0 0 -9px;
    width:380px
}
#header.new_header .hd_main {
    margin-top:20px;
    height:90px;
    padding-bottom:5px
}
#header.new_header .search_box {
    right:394px;
    top:14px;
    width:460px;
    height:32px;
    border-color:#09c762;
    z-index: 10;
}
#header.new_header .search_box .sea_input {
    margin:7px 8px 0;
    width:360px
}
#header.new_header .search_box .sea_submit {
    background-color:#09c762;
    width:80px;
}

/*----------*/
.hd_bar {
    height:34px;
    border-bottom:1px solid #e5e5e5;
    background-color:#f5f5f5;
    position:relative;
    z-index:2002
}


/*hd_bar ul*/

.hd_bar ul {
    padding-top:4px;
    float:left
}
.hd_bar ul.welcome {
    margin-left:-10px
}
.hd_bar ul.welcome li .iconfont {
    color:#999;
    margin-right:4px
}

.hd_bar ul#userinfo-bar {
    float:right
}
.hd_bar ul#userinfo-bar li .vipico {
    width:12px;
    height:17px;
   /*background:url(../../static/images/head/wap.png) no-repeat;*/
    float:left;
    margin-right:4px;
    font-size:18px
}
.hd_bar li {
    float:left;
    position:relative;
    z-index:2000;
    height:17px;
    line-height:17px;
    padding:5px 10px
}
.hd_bar li s {
    color:#ccc;
    margin:0 8px;
    text-decoration:none
}
.hd_bar li a:hover {
    text-decoration:none
}
.hd_bar ul.welcome li .iconfont {
    color:#999;
    margin-right:4px
}
.bd_bar_bd {
    width:1196px;
    margin:0 auto
}
.hd_bar li.more-menu {
    padding-right:20px
}
.hd_bar li.more-menu i.arrow {
    position:absolute;
    top:5px;
    right:5px;
    font-size:16px;
    line-height:16px;
    z-index:2002;
    -webkit-transition:all .5s;
    -moz-transition:all .5s;
    -ms-transition:all .5s;
    transition:all .5s;
    color:#bbb;
    -webkit-backface-visibility:hidden
}
.show{
    opacity:1 !important;
    visibility:visible !important;
}
.hd_bar li.hover a.menu-link {
    color:#09c762
}
.hd_bar li.hover i.arrow {
    -moz-transform:rotate(180deg);
    -webkit-transform:rotate(180deg);
    -ms-transform:rotate(180deg);
    transform:rotate(180deg)
}
.cle:after {
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle{
    *zoom:1
}
.logo {
    position:absolute;
    left:10px;
    top:5px;
    z-index:2
}
.search_box {
    position:absolute;
    right:0;
    top:0;
    width:300px;
    height:29px;
    border:2px solid #1e9246;
    border-right:0;
    background-color:#fff;
    overflow:hidden;
    box-shadow:2px 1px 1px rgba(200,200,200,0.5) inset
}
.sea_input {
    float:left;
    width:228px;
    margin:5px;
    color:#bbb;
    outline:0;
    border:0;
    background:0
}
.sea_submit {
    font-size:15px;
    color:#fff;
    float:right;
    height:29px;
    width:62px;
    padding-left:6px;
    border:0;
    background-color:#1e9246;
    cursor:pointer;
    letter-spacing:5px;
    overflow:hidden
}
.sea_submit:hover {
    color:#ffd736
}
/*热搜榜*/
.head_search_hot {
    position:absolute;
    top:58px;
    right:404px;
    width:450px;
    height:16px;
    overflow:hidden
}
.head_search_hot span {
    color:#999
}
.head_search_hot a {
    margin:0 8px 0 5px;
    color:#666
}
.head_search_hot a.red,.head_search_hot a:hover {
    color:#09c762
}

.hd_nav {
    background-color:#09c762;
    height:35px
}
.hd_nav_bd {
    padding-left:214px;
    position:relative;
    z-index:1990;
    width:982px;
    margin:0 auto
}

.main_nav {
    position:absolute;
    top:0;
    left:0;
    z-index:1991
}
.hd_nav .main_nav .main_nav_link {
    width:214px;
    height:35px;
    color:#fff;
    background-color:#1a4ec3;
    overflow:hidden
}
.hd_nav .main_nav .main_nav_link a.meunAll {
    display:block;
    padding:7px 10px 0 0;
    height:25px;
    font-size:14px;
    text-align:center;
    font-weight:bold;
    color:#fff;
    overflow:hidden
}
.hd_nav .main_nav .main_nav_link a:hover {
    color:#fff;
    text-decoration:none
}
.hd_nav .main_nav .main_nav_link i {
    position:absolute;
    top:10px;
    right:50px;
    -webkit-transition:all .5s;
    -moz-transition:all .5s;
    -ms-transition:all .5s;
    transition:all .5s;
    font-size:12px;
    line-height:16px;
    -webkit-backface-visibility:hidden
}
.hd_nav .main_nav_hover .main_nav_link i {
    -moz-transform:rotate(180deg);
    -webkit-transform:rotate(180deg);
    -ms-transform:rotate(180deg);
    transform:rotate(180deg);
}

.main_cata {
    width:214px;
    height:auto;
    opacity:1;
    position:absolute;
    left:0;
    top:35px;
    z-index:1999;
    padding-bottom:10px;
}
.main_cata ul {
    width:214px;
    padding:10px 0;
    overflow:hidden;
    background-color:#57a3f3db;
    border-bottom:1px solid #ccc;
    box-shadow:-2px 4px 4px rgba(200,200,200,0.3)
}
.main_cata li {
    width:100%;
    height:35px;
    line-height:35px;
    border:none;
    overflow:hidden;
    font-size:0;
}
.main_cata li a {
    font-size:12px;
}
.main_cata li h3 {
    text-indent:58px;
}
.main_cata li h3 a {
    font-size:13px;
    font-family:Arial;
    color:#fff;
}
.main_cata li h3 a:hover{
    color: #09c762!important;
}
.main_cata li .bd {
    padding:0 0 6px 14px;
    margin-right:-10px;
    height:43px;
    overflow:hidden
}
.main_cata li .bd a {
    color:#999;
    display:inline-block;
    margin-right:14px;
    line-height:22px
}
.main_cata li.last {
    padding:0;
    box-shadow:0 4px 3px rgba(200,200,200,0.3)
}

.hd_nav .sub_nav {
    float:left
}
.hd_nav .sub_nav li {
    float:left;
    height:35px;
    overflow:hidden;
    font-size:14px;
}
.hd_nav .sub_nav li a {
    display:inline-block;
    overflow:hidden;
    padding:7px 28px;
    color:#fff;
}
.hd_nav .sub_nav li.current a,.hd_nav .sub_nav li a:hover {
    color:#fff;
    background-color:#1e9246;
    text-decoration:none
}
.icon-tubiao-{
  transform:rotate(0deg) !important;
}
</style>
