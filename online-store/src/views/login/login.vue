<template>
  <div>
    <div class="c-box bg-box" >
      <div class="login-box clearfix"style="margin-top:10px">
        <div class="fr form-box">
          <h2>帐号登录</h2>
          <form id="jsLoginForm" autocomplete="off">
            <input type="hidden" name="csrfmiddlewaretoken" value="ywSlOHdiGsK6VFB6iyhnB1B30khmz8SU">
            <div class="form-group marb20">
              <label>用&nbsp;户&nbsp;名</label>
              <input name="account_l" id="account_l" type="text" v-model="userName" @focus="errorUnshow" placeholder="手机号/账号">
            </div>
             <p class="error-text" v-show="userNameError">{{userNameError}}</p>
            <div class="form-group marb8">
              <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
              <input name="password_l" id="password_l" type="password" v-model="parseWord" @keyup.enter="login" @focus="errorUnshow" placeholder="请输入您的密码">
            </div>
            <p class="error-text" v-show="parseWordError">{{parseWordError}}</p>
            <div class="auto-box marb38">
            </div>
            <p class="error-text" v-show="error">{{error}}</p>
            <input class="btn btn-green" id="jsLoginBtn" type="button" @click = "login" value="立即登录 &gt; ">
          </form>
          <ul class="form other-form">
            <li>
              <h5>使用第三方帐号登录</h5>
            </li>
            <li class="other-login">
              <a class="qq" href="http://shop.projectsedu.com:8001/login/qq/"></a>
              <a class="sina" href="http://shop.projectsedu.com:8001/login/weibo/"></a>
              <a class="weixin" href="http://shop.projectsedu.com:8001/login/weixin/"></a>
            </li>
          </ul>
          <p class="form-p">
            没有帐号？
            <router-link :to="'/app/register/'" target = _blank>[立即注册]</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import cookie from '../../static/js/cookie';
  import { login } from '../../api/api'
  export default {
    data(){
      return {
        userName:'',
        parseWord:'',
        autoLogin:false,
        error:false,
        userNameError:'',
        parseWordError:''
      }
    },
    methods:{
      login(){
        // if(this.userName==''||this.parseWord==''){
        //   this.error = true;
        //   return
        // }
        var that = this;
      login({
          username:this.userName, //当前页码
          password:this.parseWord
      }).then((response)=> {
            console.log(response);
            //本地存储用户信息
            cookie.setCookie('name',this.userName,7);
            cookie.setCookie('token',response.data.token,7)
            //存储在store
            // 更新store数据
            that.$store.dispatch('setInfo');
            //跳转到首页页面
            this.$router.push({ name: 'index'})
          })
          .catch(function (error) {
            if("non_field_errors" in error){
              that.error = error.non_field_errors[0];
            }
            if("username" in error){
              that.userNameError = error.username[0];
            }
            if("password" in error){
              that.parseWordError = error.password[0];
            }
          });

        //      this.$http.post('/login', {
        //   params: {
        //     userName:this.userName,
        //     parseWord:this.parseWord,
        //   }
        // })
        //   .then((response)=> {
        //     console.log(response);
        //     //本地存储用户信息
        //     cookie.setCookie('name',response.data.info.name,7);
        //     cookie.setCookie('id',response.data.info.id,7)
        //     //存储在store
        //     // 更新store数据
        //     this.$store.dispatch('setInfo');

        //     //跳转到首页页面
        //     this.$router.push({ name: 'index'})

        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //   });
      },
      errorUnshow(){
        this.error = false;
      }
    },
    created(){
      //清除缓存
      cookie.delCookie('token');
      cookie.delCookie('name');
      //重新触发store
      //更新store数据
      this.$store.dispatch('setInfo');
    }
  }
</script>
<style  scoped>
  .error-text{
    color:#fa8341;
  }
  .other-form li {
    padding-bottom: 8px;
    margin-bottom: 10px;
  }
  .other-form li h5 {
    font-size:12px;
  }

  .other-login a {
    margin-top: 0;
    vertical-align: top;
    margin-right: 10px;
    background: url(../../static/images/login/other-login-bg.png) center no-repeat;
    display: inline-block;
    width: 30px;
    height: 30px;
    overflow: hidden;
  }
  .other-login a.qq {
    background-position: -40px 0;
  }
  .other-login a.sina {
    background-position: 0 0;
  }
  .other-login a.weixin {
    background-position: -200px 0;
  }
  .c-box{
    width:100%;
    min-width: 1190px;
    overflow:hidden;
  }
  .bg-box{
    background:url(../../static/images/login/back.jpg) no-repeat center center;
    background-size: 100%;
  }
  .login-box{
    width:853px;
    margin:0px auto;
  }
  .clearfix::after {
    clear: both;
    content: " ";
    display: block;
    font-size: 0;
    height: 0;
    visibility: hidden;
  }
  .imgslide li {
    float:left;
  }
  .imgslide .dots li{
    float:left;
    margin:5px;
    background:#fff;
    width:12px;
    height:12px;
    border-radius:50%;
    color:#fff;
    text-align:center;
    cursor:pointer;
    overflow: hidden;
  }
  .hd-login > h1{
    float:left;
    color:#fff;
    font-size:30px;
    font-weight: normal;
  }
  .form-box .valcode.errorput input {
    border-color: #f00;
    box-shadow: 0 0 5px #aa0b0b;
  }
  .form-box a{
    color:#666;
  }
  .form-box a:hover{
    color:#6ec559;
  }
  .form-box{
    position:relative;
    width:330px;
    height: 472px;
    padding:0 40px;
    background:#fff;
    color:#666;
  }
  .form-box > h2,
  .form-box > .tab{
    height:54px;
    line-height:54px;
    margin-bottom:34px;
    font-size:18px;
    font-weight:normal;
    color:#333;
    border-bottom:1px solid #eaeaea;
  }
  .form-box > .tab > h2{
    float:left;
    width:90px;
    height:53px;
    line-height:53px;
    cursor: pointer;
    font-weight:normal;
    text-align:center;
  }
  .form-box > .tab > h2.active{
    border-bottom:3px solid #6ec55a;
    color:#333;
  }
  .form-group{
    position:relative;
    width:270px;
    height:38px;
    border:1px solid #dedede;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    overflow:hidden;
  }
  .form-group > label{
    float:left;
    width:72px;
    height:20px;
    line-height:20px;
    margin-top:9px;
    border-right:1px solid #eaeaea;
    text-align:center;
  }
  .form-group > input{
    float:left;
    width:195px;
    line-height:24px;
    padding:7px 10px;
    border:0;
    line-height:normal\9;
    padding:12px 10px 9px\9;
  }
  .marb20{
    margin-bottom:8px;
  }
  .marb8{
    margin-bottom:8px;
    margin-top: 20px;
  }
  .marb38{
    margin-bottom:38px;
  }
  .auto-box{
    height:18px;
    line-height:18px;
  }
  .auto-box > label > input{
    vertical-align: sub;
  }
  .auto-box > label > a{
    color:#6ec559;
  }
  .btn{
    width:100%;
    height:42px;
    line-height:42px;
    font-size:14px;
    color:#fff;
    border:0;
    cursor:pointer;
  }
  .btn-green{
    background:#6ec55a;
  }
  .btn-green:hover{
    background:#5dbf45;
  }
  .form-p{
    position:absolute;
    left:40px;
    bottom:25px;
  }
  .form-p > a{
    color:#fa8341;
  }
  .form-p > a:hover{
    color:#666;
  }


</style>
