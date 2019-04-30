<template>
  <div style="position: relative;">
    <current-loc :curLoc="curLoc"></current-loc>
    <Menu theme="light" :active-name="singer" @on-select="changeSinger">
      <MenuGroup title="歌手列表">
        <MenuItem :name="item.id" v-for="item in singersList">{{item.name}}</MenuItem>
      </MenuGroup>
    </Menu>
    <div class="singer_detail">
      <div class="left">
        <img :src="singerDetail.singer_images" width="220" height="250" alt="歌手封面图">
      </div>
      <div class="right">
        <h2>{{singerDetail.name}}</h2>
        <span class="tab">性别：</span><span>{{singerDetail.gender==='male'?'男':'女'}}</span><br/>
        <span class="tab">出生日期：</span><span>{{singerDetail.birthday?singerDetail.birthday:'未知'}}</span><br/>
        <span class="tab">国籍：</span><span>{{singerDetail.country?singerDetail.country:'暂无'}}</span><br/>
        <span class="tab">主要作品：</span>
        <div class="songs_box">
          <div class="songs" v-if="singerDetail.singername.length" v-for="song in singerDetail.singername">
            <router-link :to="'/app/home/songDetail/'+song.id" target = _blank>
              <span class="item">{{song.name}}</span>
            </router-link>
          </div>
        </div>
        <br />
        <span class="tab">简介：</span><span>{{singerDetail.desc?singerDetail.desc:'暂无'}}</span><br/>
      </div>
    </div>
  </div>
</template>
<script>
import cookie from '../../static/js/cookie';
import currentLoc from './current-loc/current-loc';
import { mapGetters } from 'vuex';
import { getSingers, getSingersDetail, getFav, addFav, delFav} from '../../api/api';
  export default {
    data () {
      return {
        singer: 1,
        singersList: [],
        singerId: '', //当前歌手id
        hasFav: false,
        singerDetail: {},
        curLoc:{}
      };
    },
    components: {
      'current-loc': currentLoc,
    },
    created () {
      this.singerId = this.$route.params.singerId;
      var singerId = this.singerId
      if(cookie.getCookie('token')){
        getFav(singerId).then((response)=> {
          this.hasFav = true
        }).catch(function (error) {
          console.log(error);
        });
      }
      this.getSingersList();
      this.getDetails();
    },
    methods: {
      getSingersList(){
        getSingers()
          .then((response)=> {
              console.log(response.data);
              this.singersList = response.data;
          }).catch(function (error) {
              console.log(error);
          });
      },
      getDetails () { //  请求歌手详情
        getSingersDetail(this.singerId)
          .then((response)=> {
            console.log(response.data);
            this.singerDetail = response.data;
            this.curLoc = response.data;
            this.singer = response.data.id;
          }).catch(function (error) {
            console.log(error);
          });
      },
      changeSinger(item){
        this.singerId = item
        this.singer = item
        this.getDetails()
      },
      // 增加数量
      addCollect () { //加入收藏
        addFav({
          songs: this.singerId
        }).then((response)=> {
          console.log(response.data);
          this.hasFav = true
          alert('已成功加入收藏夹');
        }).catch(function (error) {
          console.log(error);
        });
      },
      deleteCollect () {
          //删除收藏
        delFav(this.singerId).then((response)=> {
          console.log(response.data);
          this.hasFav = false
        }).catch(function (error) {
          console.log(error);
        });
      },
    }
}
</script>
<style scoped>
  a{
    color: #46bbde;
  }
  /deep/ .ivu-menu{
    display: inherit;
    margin-left: 1%;
  }
  /deep/ .ivu-menu-item-group{
    height: 350px;
    overflow-y: scroll;
    margin-bottom: 10px;
  }
  .singer_detail{
    display: inline-block;
    width: 60%;
    height: 350px;
    border: 3px solid greenyellow;
    border-radius: 5px;
    left: 22%;
    top: 40px;
    position: absolute;
  }
  .singer_detail .left{
    position: absolute;
    top: 30px;
    left: 30px;
  }
  .singer_detail .right{
    position: absolute;
    top: 50px;
    left: 300px;
  }
  .singer_detail .right span{
    line-height: 30px;
  }
  .singer_detail .right span.tab{
    color: #aaa;
    display: inline-block;
    width: 60px;
    text-align: right;
    margin-right: 10px;
  }
  .songs_box{
    display: inline-block;
    width: 300px;
    vertical-align: top;
  }
  .songs{
    display: inline-block;
  }
  .songs .item{
    display: inline-block;
    margin-right: 10px;
    height: 24px;
    line-height: 37px !important;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap
  }
</style>
