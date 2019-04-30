<template>
  <div>
    <current-loc :curLoc="curLoc"></current-loc>
    <Menu theme="light" :active-name="cd" @on-select="changeCD">
      <MenuGroup title="专辑列表">
        <MenuItem :name="item.id" v-for="item in cdsList">{{item.name}}</MenuItem>
      </MenuGroup>
    </Menu>
    <div class="cd_detail">
      <div class="left">
        <img :src="cdDetail.cds_front_image" width="220" height="250" alt="歌曲封面图">
      </div>
      <div class="right">
        <h2>{{cdDetail.name}}</h2>
        <span class="tab">收录歌曲：</span>
        <div class="songs_box">
          <div class="songs" v-if="cdDetail.cdname.length" v-for="song in cdDetail.cdname">
            <router-link :to="'/app/home/songDetail/'+song.id" target = _blank>
              <span class="item">{{song.name}}</span>
            </router-link>
          </div>
        </div>
        <br />
        <span class="tab">上传时间：</span><span>{{cdDetail.add_time?cdDetail.add_time:'未知'}}</span><br/>
        <!--<Button type="warning">收藏</Button>-->
      </div>
    </div>
  </div>
</template>
<script>
import cookie from '../../static/js/cookie';
import currentLoc from './current-loc/current-loc';
import { mapGetters } from 'vuex';
import { getCDs, getCDsDetail, getFav, addFav, delFav } from '../../api/api';
  export default {
    data () {
      return {
        cd: 1,
        cdsList: [],
        cdId: '', //当前专辑id
        hasFav: false,
        cdDetail: {},
        curLoc:{}
      };
    },
    components: {
      'current-loc': currentLoc,
    },
    created () {
      this.cdId = this.$route.params.cdId;
      var cdId = this.cdId
      if(cookie.getCookie('token')){
        getFav(cdId).then((response)=> {
          this.hasFav = true
        }).catch(function (error) {
          console.log(error);
        });
      }
      this.getCDsList();
      this.getDetails();
    },
    methods: {
      getCDsList(){
        getCDs()
          .then((response)=> {
            console.log(response.data);
            this.cdsList = response.data;
          }).catch(function (error) {
            console.log(error);
          });
      },
      getDetails () { //  请求cd详情
        getCDsDetail(this.cdId)
          .then((response)=> {
            console.log(response.data);
            this.cdDetail = response.data;
            this.curLoc = response.data;
            this.cd = response.data.id
          }).catch(function (error) {
            console.log(error);
          });
      },
      changeCD(item){
        this.cdId = item
        this.cd = item.id
        this.getDetails()
      },
      // 减少数量
      hasFaved () {

      },

      // 增加数量
      addCollect () { //加入收藏
        addFav({
          songs: this.cdId
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
        delFav(this.cdId).then((response)=> {
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
  .cd_detail{
    display: inline-block;
    width: 60%;
    height: 350px;
    border: 1px solid greenyellow;
    left: 20%;
    top: -140px;
    position: relative;
  }
  .cd_detail .left{
    position: absolute;
    top: 30px;
    left: 30px;
  }
  .cd_detail .right{
    position: absolute;
    top: 50px;
    left: 300px;
  }
  .cd_detail .right span{
    line-height: 25px;
  }
  .cd_detail .right span.tab{
    color: #aaa;
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
    height: 18px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap
  }
</style>
