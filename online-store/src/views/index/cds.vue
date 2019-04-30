<template>
  <div class="cd-list">
    <div class="title">
      <i class="iconfont icon-tuijian"></i>
      <span>推荐专辑</span>
      <span class="more">
        <router-link to="/app/home/cdDetail/1" target = _blank>
          <span>更多 ></span>
        </router-link>
      </span>
    </div>
    <div class="list" v-for="item in cds">
      <router-link :to="'/app/home/cdDetail/'+item.id" target = _blank>
        <div style="text-align: center"><img :src="item.cds_front_image" width="150" height="150" alt="专辑封面图"></div>
        <p class="name">{{item.name}}</p>
      </router-link>
    </div>
  </div>
</template>
<style scoped>
  a{
    color: #46bbde;
  }
  p.name:hover{
    color: #09c762!important;
  }
  .cd-list{
    display: inline-block;
    width: 22%;
    height: 400px;
    float: right;
    margin-right: 3%;
    margin-top: 10px;
    border: 3px solid greenyellow;
    overflow-y: scroll;
  }
  .title{
    display: inline-block;
    width: 100%;
    font-size: 25px;
    color: #58a7cb;
  }
  .more{
    float: right;
    font-size: 16px;
    line-height: 42px;
    margin-right: 20px;
  }
  .more a span{
    color: grey!important;
    padding: 2px 3px;
    border-radius: 3px;
  }
  .more a span:hover{
    background-color: #97df82;
  }
  .icon-tuijian{
    font-size: 28px;
    margin-left: 10px;
  }
  .list .name{
    text-align: center;
    font-size: 18px;
  }
</style>

<script>
  import {getCDs} from '../../api/api'

  export default {
    data() {
      return {
        cds:[]
      }
    },
    methods:{
      getCDsList(){
        getCDs({
          is_recommend: true
        })
        .then((response)=> {
          console.log(response)
          //跳转到首页页response.body面
          this.cds = response.data
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    created(){
      this.getCDsList();
    }
  }
</script>


