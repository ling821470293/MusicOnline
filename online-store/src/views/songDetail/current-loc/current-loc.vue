<template>
  <div class="current-loc">
    <div class="breadcrumbs cle z-detail-box">
      <div class="menus">
        <a href="http://127.0.0.1:8080/">首页</a>
        <code>&gt;</code>
        <a :href="'http://localhost:8080/#/app/home/list/'+ curLoc.category.id">{{curLoc.category.name}}</a>
        <code>&gt;</code>
        {{curLoc.name}}
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {
      };
    },
    props: {
      curLoc: {
        type: Object,
        default: function() {
          return {};
        }
      }
    },
}
</script>
<style  lang='scss'>
.current-loc{
  margin-left: 10px;
}
.cle:after{
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle{
    *zoom:1
}

a {
    text-decoration:none;
    color:#333;
    -webkit-transition:color .2s;
    -moz-transition:color .2s;
    -o-transition:color .2s;
    transition:color .2s
}
a:hover {
    color:#09c762
}
a:focus,area:focus {
    outline:0
}

canvas {
    -ms-touch-action:double-tap-zoom
}

.breadcrumbs {
    padding:0 5px 0 0;
    line-height:38px;
    color:#666
}
.breadcrumbs .menus {
    float:left
}
.breadcrumbs .menus a {
    margin-right:6px
}
.breadcrumbs .right {
    float:right;
    color:#bbb
}
.breadcrumbs .right i {
    font-size:20px;
    margin-right:5px;
    vertical-align:-2px
}
.breadcrumbs .right .code {
    color:#fafafa;
    margin-right:30px;
    display:inline-block
}

</style>
