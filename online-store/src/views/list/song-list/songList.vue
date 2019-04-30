<template>
  <div class="songlist">
    <ul class="list_item">
      <li v-for="item in listData" >
        <router-link :to="'/app/home/songDetail/'+item.id" target="_blank" class="productitem">
          <span class="name">{{item.name}}</span>
        </router-link>
        <div class="detail">
          <div class="author">
            <span class="title">演唱者：</span>
            <router-link :to="'/app/home/singerDetail/'+item.singer_id.id" target = _blank>
              <span class="name">{{item.singer_id.name}}</span>
            </router-link>
          </div>
          <div class="calc">
            <span class="title">点击量：</span><span>{{item.click_num}}</span>
            <span class="title">收藏数：</span><span>{{item.fav_num}}</span>
          </div>
        </div>
      </li>
    </ul>
</div>
</template>
<script>
    export default {
      data () {
        return {};
      },
      props: {
        listData: {
          type: Array,
          default: function() {
            return [];
          }
        }
      },
    }
</script>
<style scoped>
  .songlist{
    display: block;
    padding-left: 10px;

    width: 100%;
    line-height: 25px;
    border-bottom: 1px solid #cccccc;
  }
  .songlist .title{
    margin-left: 20px;
  }
  .songlist .name{
    color: darkturquoise;
  }
  .songlist .name:hover{
    color: orchid;
  }
  .detail{
    float: right;
    margin-right: 50px;
  }
  .author{
    display: inline-block;
    width: 200px;
    text-align: center;
  }
  .calc{
    display: inline-block;
  }
</style>
