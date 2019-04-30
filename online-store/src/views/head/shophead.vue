<template>
  <div>
    <div id="header">
      <div class="hd_bar" id="userinfo-bar">
        <div class="bd">
          <div class="hd_lbar" style="display: block;" id="ECS_MEMBERZONE">
            <template v-if="userInfo.name">
              <router-link :to="'/app/home/index'"> 网站首页</router-link>
              <router-link v-if="userInfo.name" :to="'/app/home/member/userinfo'">{{userInfo.name}}</router-link>
              &nbsp;[<a @click="loginOut">退出</a>]
            </template>
            <template v-else>
              <router-link :to="'/app/login'"> 登录</router-link>
              <router-link :to="'/app/register'"> 注册</router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex';
  export default {
    computed: {
      ...mapGetters({
        userInfo:'userInfo'
      })
    },
    methods: {
      loginOut(){
        cookie.delCookie('token');
        cookie.delCookie('name');
        //重新触发store
        //更新store数据
        this.$store.dispatch('setInfo');
        //跳转到登录
        this.$router.push({name: 'login'})
      },
    }
  }
</script>

<style scoped>
#header {
    width:100%
}
#header .hd_bar {
    background-color:#222;
    height:57px
}
.hd_bar .bd {
    width:826px;
    height:57px;
    margin:0 auto;
    position:relative;
    z-index:100
}
.hd_bar .hd_lbar {
    float:left;
    width:310px;
    overflow:hidden;
    padding-left:6px;
    display:none
}
.hd_bar .hd_lbar a {
    display:inline-block;
    height:17px;
    line-height:17px;
    color:#eee;
    padding:20px 12px;
    background-color:#222;
    vertical-align:top
}
.hd_bar .hd_lbar a:hover {
    background-color:#666;
    color:#fff;
    text-decoration:none
}
.hd_bar .hd_lbar .iconfont {
    margin-right:5px;
    color:#999;
    vertical-align:top
}
</style>
