<template>
  <div class="songs_list">
    <div class="title">
      <i class="iconfont icon-remen"></i>
      <span>热门推荐</span>
    </div>
    <div class="list_box">
      <div class="list" v-for="(item ,index) in list">
        <div class="list_item">
          <div>
            <span>{{index + 1}}.&nbsp;</span>
            <router-link :to="'/app/home/songDetail/'+item.id" target = _blank>
              <span>{{item.name}}</span>
            </router-link>
            <span> ------</span>
            <router-link :to="'/app/home/singerDetail/'+item.singer_id.id" target = _blank>
              <span>{{item.singer_id.name}}</span>
            </router-link>
            <!--<div class="operation">-->
              <!--<span class="play" @click="play(item)">-->
                <!--<audio id='test' src=''></audio>-->
                <!--<i v-if="item.state" class="iconfont icon-suspend_icon"></i>-->
                <!--<i v-else class="iconfont icon-bofang"></i>-->
              <!--</span>-->
              <!--<span class="download" @click="down(item)"><i class="iconfont icon-xiazai"></i></span>-->
              <!--<span class="fav"><i class="iconfont icon-shoucang1"></i></span>-->
            <!--</div>-->
          </div>
        </div>
      </div>
    </div>
    <div class="link_more">
      <span class="more">
        <router-link to="/app/home/list/1" target = _blank>
          <span>更多 ></span>
        </router-link>
      </span>
    </div>
  </div>
</template>
<script>
  import { getSongs } from '../../api/api';
  import saveAs from 'file-saver';
  var FileSaver = require('file-saver');
  export default {
    data(){
      return {
        list:[],
        isPlaying:false
      }
    },
    methods:{
      getList(){
        getSongs({
          is_hot: true
        })
        .then((response)=> {
           //跳转到首页页response.body面
          console.log(response)
            this.list = response.data.results
        })
        .catch(function (error) {
          console.log(error);
        });
      },
      play(item){
        let player = document.getElementById('test');
        if (this.isPlaying) {
          // 如果正在播放, 停止播放并停止读取此音乐文件
          player.pause();
          player.src = '';
          item.state = false
          this.isPlaying = false;
        } else {
          player.src = item.file;
          player.play();
          item.state = true
          this.isPlaying = true;
        }
        console.log(item)
        console.log(this.list)
      },
      down(data){
        FileSaver.saveAs(data.file, data.name)
      }
    },
    created(){
      this.getList();
    }
}
</script>
<style  lang='scss' scoped>
  a{
    color: #46bbde;
  }
  a:hover{
    color: #09c762!important;
  }
 .songs_list{
   display: inline-block;
   position: relative;
   width: 55%;
   height: 400px;
   margin-top: 10px;
   border: 3px solid greenyellow;
 }
 .icon-remen{
   padding-left: 10px;
   font-size: 28px;
 }
  .title{
    font-size: 30px;
    color: orangered;
  }
  .link_more{
    position: absolute;
    bottom: 5px;
    right: 5px;
  }
  .more{
    float: right;
    font-size: 18px;
    margin-right: 20px;
    margin-top: 10px;
  }
  .more a span{
    color: grey!important;
    padding: 2px 3px;
    border-radius: 3px;
  }
  .more a span:hover{
    background-color: #97df82;
  }
  .list_box{
    height: 300px;
    overflow-y: hidden;
  }
  .list{
    display: block;
    padding-left: 10px;
    height: 30px;
    width: 100%;
    line-height: 30px;
    border-bottom: 1px solid #cccccc;
  }
  .list_item{
    position: relative;
  }
  .operation{
    display: inline-block;
    position: absolute;
    right: 15px;
  }
  .operation span{
    margin-left: 15px;
  }
  .operation span:hover{
    cursor: pointer;
  }
  .operation span i{
    font-size: 20px;
  }
  .operation .play{
    color: #7acce4;
  }
</style>
