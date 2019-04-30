<template>
  <div>
    <rank></rank>
    <songList></songList>
    <cdList></cdList>
  </div>
</template>
<script>
//排行榜
import rank from './rank';
//歌曲列表
import songList from './song-list';
//专辑列表
import cdList from './cds';

export default {
  components:{
    rank, songList, cdList
  }
}
</script>
<style  lang='scss'>

</style>
