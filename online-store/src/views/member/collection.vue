<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
      <div class="box">
        <div class="userCenterBox">
          <div>
            <h5><span>我的收藏</span></h5>
            <div class="blank"></div>
            <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
              <tbody>
                <tr align="center">
                  <th width="25%" bgcolor="#ffffff">歌曲名称</th>
                  <th width="25%" bgcolor="#ffffff">演唱者</th>
                  <th width="25%" bgcolor="#ffffff">所属专辑</th>
                  <th width="25%" bgcolor="#ffffff">操作</th>
                </tr>
                <tr v-for="(item,index) in collections">
                  <td align="center" bgcolor="#ffffff">
                    <router-link :to="'/app/home/songDetail/'+item.songs.id" class="f6" target="_blank">{{item.songs.name}}</router-link>
                  </td>
                  <td align="center" bgcolor="#ffffff">
                    <router-link v-if="item.songs.singer_id" :to="'/app/home/singerDetail/'+item.songs.singer_id.id" class="f6" target="_blank">{{item.songs.singer_id.name}}</router-link>
                  </td>
                  <td align="center" bgcolor="#ffffff">
                    <router-link v-if="item.songs.cd_id" :to="'/app/home/cdDetail/'+item.songs.cd_id.id" class="f6" target="_blank">{{item.songs.cd_id.name}}</router-link>
                  </td>
                  <td align="center" bgcolor="#ffffff">
                    <!--<a class="f6" @click="deletePro(index, item.songs.id)">删除</a>-->
                    <Button type="error" @click="model(index, item.songs.id)">删除</Button>
                  </td>
                </tr>
              </tbody>
            </table>
            <form name="selectPageForm" action="" method="get">
              <div class="pagenav" id="pagenav">
                <ul>
                  <li></li>
                </ul>
                <div class="clear"></div>
              </div>
            </form>
          </div>
          <div v-if="show" class="model">
            <div class="content">
              <span>确定删除吗？</span>
            </div>
            <div class="foot">
              <Button type="" size="small" @click="cancel">取消</Button>
              <Button type="error" size="small" @click="deletePro(num, item)">删除</Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import {getAllFavs, delFav} from '../../api/api'
    export default {
      data () {
        return {
          collections: [],
          show: false,
          num: -1,
          item: -1
        };
      },
      created () {
        this.getCollection();
      },
      methods: {
        model(index, songs){
          this.show = true
          this.num = index
          this.item = songs
        },
        getCollection () { //获取收藏列表
          getAllFavs().then((response)=> {
            console.log(response.data)
            this.collections = response.data;
          }).catch(function (error) {
            console.log(error);
          });
        },
        cancel(){
          this.show = false
        },
        deletePro (index, id) { //删除收藏歌曲
          delFav(id).then((response)=> {
            this.show = false
            this.collections.splice(index,1);
            alert('已删除歌曲');
            this.num = -1
            this.item = -1
          }).catch(function (error) {
            console.log(error);
          });
        }
      }
    }
</script>
<style scoped>
.my_nala_main h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
.my_nala_main h3.my_nala a:hover {
    text-decoration:none
}

.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.my_nala_centre .something_interesting ul {
    margin-left:20px
}
.my_nala_centre .something_interesting li {
    width:130px;
    text-align:center;
    float:left
}
.my_nala_centre .something_interesting b {
    font-weight:normal
}
.my_nala_centre .something_interesting em {
    font-size:12px;
    font-weight:bold;
    color:#09c762
}
.my_nala_centre .pagenav {
    padding:15px 10px;
    border-top:1px solid #e4e4e4
}


.ilizi_centre {
    background:0
}

.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff;
    min-height: 200px;
}
.ilizi .face img,.iface .face img {
    width:100px;
    height:100px;
    border:1px solid #e4e4e4
}
.userCenterBox{
  position: relative;
}
.model{
  width: 200px;
  height: 80px;
  position: absolute;
  top: 0;
  left: 20%;
  background-color: #e1f0fe;
  border: 1px solid #58a7cb;
  border-radius: 8px;
}
.model .content{
  height: 50px;
  line-height: 60px;
  text-align: center;
  font-size: 20px;
}
.model .foot{
  text-align: right;
  margin-right: 10px;
}
tr{
  height: 35px;
}
a:hover{
  color: #09c762;
}

</style>
