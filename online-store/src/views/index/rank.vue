<template>
  <div class="rank">
    <span class="title">排行榜</span>
    <Tabs value="dot" @on-click="rank">
      <TabPane label="点击榜" name="dot">
        <div class="list" v-for="item in dotList">
          <div class="list_item">
            <router-link :to="'/app/home/songDetail/'+item.id" target = _blank>
              <span>{{item.name}}</span>
            </router-link>
            <span class="num">点击量：{{item.click_num}}</span>
          </div>
        </div>
      </TabPane>
      <TabPane label="收藏榜" name="fav">
        <div class="list" v-for="item in favList">
          <div class="list_item">
            <router-link :to="'/app/home/songDetail/'+item.id" target = _blank>
              <span>{{item.name}}</span>
            </router-link>
            <span class="num">收藏数：{{item.fav_num}}</span>
          </div>
        </div>
      </TabPane>
    </Tabs>
  </div>
</template>
<script>
  import { getSongs } from '../../api/api';
export default{
    data(){
        return {
          songList:{},
          dotList:{},
          favList:{},
          downList:{},
        }
    },
    methods:{
      getOpro(){
        getSongs()
          .then((response)=> {
            console.log(response)
            this.songList = response.data.results
            this.rank('dot')
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      rank(name){
        if(name === 'dot'){
          this.dotList = this.songList.sort(this.compare('click_num'))
        }else if(name === 'fav'){
          this.favList = this.songList.sort(this.compare('fav_num'))
        }else if(name === 'down'){
          this.downList = this.songList.sort(this.compare('download_num'))
        }
      },
      compare(property){
        return function(obj1,obj2){
          var value1 = obj1[property];
          var value2 = obj2[property];
          return value2 - value1;     // 降序
        }
      }
    },
    created(){
      this.getOpro();
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
  .rank{
    display: inline-block;
    margin: 10px;
    float: left;
    width: 18%;
    height: 400px;
    border: 3px solid greenyellow;
    overflow-y: hidden;
  }
  .title{
    display: inline-block;
    width: 100%;
    text-align: center;
    font-size: 25px;
    color: darkgoldenrod;
  }
  .list{
    display: block;
    padding-left: 10px;
    height: 30px;
    width: 100%;
    line-height: 30px;
    border-bottom: 1px solid #cccccc;
  }
  .num{
    float: right;
    margin-right: 20px;
  }

</style>
<style>
  .ivu-tabs > .ivu-tabs-bar .ivu-tabs-nav{
    left: 32px!important;
  }
</style>

