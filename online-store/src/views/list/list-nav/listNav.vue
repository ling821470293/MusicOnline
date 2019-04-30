<template>
  <div class="sidebar">
    <div class="cate-menu">
      <h3 v-if="isObject"><strong>{{currentCategoryName}}</strong><i id="total_count">歌曲共{{songNum}}首</i></h3>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        cateType: '', //类别
      };
    },
    components: {

    },
    props: {
      songNum: { //歌曲数量
        type: Number,
        default: 0
      },
      isArray:{
        default: function () {
          return false
        }
      },
      isObject: false,
      currentCategoryName: ""
    },
    methods: {
    }
}
</script>
<style scoped>
  .sidebar{
    display: inline-block;
    width: 15%;
    height: 100%;
  }
  .sidebar strong{
    display: inline-block;
    font-size: 30px;
  }
  #total_count{
    float: right;
    line-height: 46px;
    color: #aaaaaa;
  }
</style>
