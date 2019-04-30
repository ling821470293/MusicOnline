<template>
  <div id="wrapper">
    <current-loc :curLoc="curLoc"></current-loc>
    <div class="main cle">
      <list-nav :currentCategoryName="currentCategoryName" :songNum="songNum" :isObject="isObject"></list-nav>
      <div class="maincon">
        <list-sort @on-sort="changeSort" :songNum="songNum"></list-sort>
        <div class="list-detail">
          <song-list  :listData="listData"></song-list>
          <Page pre-text="上一页" next-text="下一页" end-show="false" :page="curPage" :total-page='totalPage' @pagefn="pagefn"></Page>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  // 歌曲列表
  import songList from './song-list/songList';
  // 左侧列表导航
  import listNav from './list-nav/listNav';
  // 列表排序
  import listSort from './list-sort/listSort';
  // 翻页
  import page from './page/page';
  // 当前位置
  import currentLoc from './current-loc/current-loc';

    import { getCategory, getSongs } from '../../api/api'
    export default {
      data () {
        return {
          curPage: 1, // 页码
          category: '', // 歌曲类型
          listData: [],
          isObject:true,
          ordering: '-add_time',
          songNum: 0, //歌曲数量
          curLoc: {}, //当前位置
          pageType:'list',
          searchWord:'',
          currentCategoryName:''
        };
      },
      components: {
        'song-list': songList,
        'list-nav': listNav,
        'list-sort': listSort,
        'Page': page,
        'current-loc': currentLoc,
      },
      created () {
        this.getAllData ();
      },
      watch: {
        "$route": "getAllData"
      },
      computed: {
        totalPage(){
          return  Math.ceil(this.songNum/10)
        }
      },
      methods: {
        getAllData () {
          if(this.$route.params.id){
            this.category = this.$route.params.id;
            this.pageType = ''
            this.getMenu(this.category); // 获取左侧菜单列表
          }else{
            this.getMenu(null); // 获取左侧菜单列表
            this.pageType = 'search'
            this.searchWord = this.$route.params.keyword;
          }
          this.getListData(); //获取歌曲列表
        },
        getListData() {
          if(this.pageType==='search'){
            getSongs({
              search: this.searchWord, //搜索关键词
            }).then((response)=> {
              this.listData = response.data.results;
              this.songNum = response.data.count;
            }).catch(function (error) {
              console.log(error);
            });
          }else {
            getSongs({
              page: this.curPage, //当前页码
              category: this.category, //歌曲类型
              ordering: this.ordering, //排序类型
            }).then((response)=> {
              console.log(response)
              this.listData = response.data.results;
              this.songNum = response.data.count;
            }).catch(function (error) {
              console.log(error);
            });
          }
        },
        getMenu(id) {
          if(id != null){
            getCategory({
              id:this.$route.params.id
            }).then((response)=> {
              this.currentCategoryName = response.data.name
              this.isObject = true
              this.curLoc = response.data
            }).catch(function (error) {
              console.log(error);
            });
          }else {
            getCategory({}).then((response)=> {
              this.isObject = false
              this.curLoc = {}
            }).catch(function (error) {
              console.log(error);
            });
          }
        },
        changeSort (type) {
          this.ordering = type;
          this.getListData();
        },
        pagefn(value){//点击分页
          this.curPage = value.page;
          this.getListData()
        }
      }
}
</script>
<style  lang='scss'>
.maincon {
    width: 970px;
    float: right;
}
</style>
