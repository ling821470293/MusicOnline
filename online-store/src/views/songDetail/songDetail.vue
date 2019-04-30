<template>
  <div>
    <current-loc :curLoc="curLoc"></current-loc>
    <div class="song_detail">
      <div class="left">
        <img :src="songDetail.songs_front_image" width="220" height="250" alt="歌曲封面图">
      </div>
      <div class="right">
        <h2>{{songDetail.name}}</h2>
        <span class="tab">演唱者：</span>
        <router-link v-if="songDetail.singer_id" :to="'/app/home/singerDetail/'+songDetail.singer_id.id" target = _blank>
          <span>{{songDetail.singer_id?songDetail.singer_id.name:'未知'}}</span>
        </router-link>
        <br/>
        <span class="tab">歌曲分类：</span><span>{{songDetail.category?songDetail.category.name:''}}</span><br/>
        <span class="tab">所属专辑：</span>
        <router-link v-if="songDetail.cd_id" :to="'/app/home/cdDetail/'+songDetail.cd_id.id" target = _blank>
          <span>{{songDetail.cd_id?songDetail.cd_id.name:'暂无'}}</span>
        </router-link>
        <br/>
        <span class="tab">歌曲简介：</span><span>{{songDetail.songs_brief?songDetail.songs_brief:'暂无'}}</span><br/>
        <span class="tab">发行时间：</span><span>{{songDetail.publish_date?songDetail.publish_date:'未知'}}</span><br/>
        <span class="tab">播放：</span><audio :src="songDetail.file" id="myAudio" controls autoplay="autoplay">Audio player not available.</audio><br/>
        <Button v-if="!hasFav" type="warning" @click.native="addCollect">收藏</Button>
        <Button v-else type="error" @click.native="deleteCollect">取消收藏</Button>
      </div>
    </div>
    <div class="my_fav">
      <h2>我的收藏</h2>
      <div class="song_list">
        <div class="item" v-for="item in collections">
          <router-link :to="'/app/home/songDetail/'+item.songs.id" target = _blank>
            <span>{{item.songs.name}}</span>
          </router-link>
          <span class="btn_class">
            <Button type="error" size="small" @click.native="deleteItemCollect(item.songs.id)">取消收藏</Button>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import cookie from '../../static/js/cookie';
import currentLoc from './current-loc/current-loc';
import { mapGetters } from 'vuex';
import { getSongsDetail, getAllFavs, getFav, addFav, delFav} from '../../api/api';
  export default {
    data () {
      return {
        songId: '', //当前歌曲id
        hasFav: false,
        songDetail: {},
        curLoc:{},
        collections:[],
      };
    },
    components: {
      'current-loc': currentLoc,
    },
    created () {
      this.songId = this.$route.params.songId;
      var songId = this.songId
      if(cookie.getCookie('token')){
        getFav(songId).then((response)=> {
          this.hasFav = true
        }).catch(function (error) {
          console.log(error);
        });
      }
      this.getDetails();
      this.getCollection();
    },
    methods: {
      getDetails () { //  请求歌曲详情
        getSongsDetail(this.songId)
          .then((response)=> {
              console.log(response.data);
              this.songDetail = response.data;
              this.curLoc = response.data;
          }).catch(function (error) {
              console.log(error);
          });
      },
      getCollection () { //获取收藏列表
        getAllFavs().then((response)=> {
              this.collections = response.data;
              console.log(this.collections)
          }).catch(function (error) {
              console.log(error);
          });
      },
      // 增加数量
      addCollect () { //加入收藏
        addFav({
          songs: this.songId
        }).then((response)=> {
          console.log(response.data);
          this.hasFav = true
          alert('已成功加入收藏夹');
          this.getCollection()
        }).catch(function (error) {
          console.log(error);
          if(error.detail === "身份认证信息未提供。"){
            alert('请登录后再收藏');
          }
        });
      },
      deleteCollect () {
          //删除收藏
        delFav(this.songId).then((response)=> {
          console.log(response.data);
          this.hasFav = false
          this.getCollection()
        }).catch(function (error) {
          console.log(error);
        });
      },
      deleteItemCollect(item){
        //删除收藏
        delFav(item).then((response)=> {
          console.log(response.data);
          this.getCollection()
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
}
</script>
<style scoped>
  a{
    color: #46bbde;
  }
  .song_detail{
    display: inline-block;
    width: 60%;
    height: 350px;
    border: 3px solid greenyellow;
    margin-left: 8%;
    position: relative;
    border-radius: 5px;
  }
  .song_detail .left{
    position: absolute;
    top: 30px;
    left: 30px;
  }
  .song_detail .right{
    position: absolute;
    top: 50px;
    left: 300px;
  }
  .song_detail .right span{
    line-height: 25px;
  }
  .song_detail .right span.tab{
    color: #aaa;
  }
  .my_fav{
    float: right;
    margin-right: 15px;
    width: 30%;
    height: 350px;
    border: 3px solid greenyellow;
    border-radius: 5px;
  }
  .my_fav h2{
    font-size: 20px;
    padding-left: 5px;
    border-bottom: 2px solid #aaa;
  }
  .my_fav .item{
    height: 30px;
    line-height: 30px;
    border-bottom: 1px solid #ccc;
  }
  .my_fav .item span{
    margin-left: 10px;
  }
  .btn_class{
    float: right;
    margin-right: 20px;
    line-height: 27px;
  }
</style>
