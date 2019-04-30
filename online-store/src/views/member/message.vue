<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
      <div class="box">
        <div class="box_1">
          <div class="userCenterBox boxCenterList clearfix" style="_height:1%; font-size:14px;">
            <h5><span>我的留言</span></h5>
            <div class="blank"></div>
            <div class="blank"></div>
            <div class="message-all">
              <ul>
                <li v-for="(item,index) in messageAll">
                  <div>
                    <span v-if="item.message_type===1">留言：</span>
                    <span v-if="item.message_type===2">建议：</span>
                    <span v-if="item.message_type===3">询问：</span>
                    <span>{{item.subject}}</span>
                    <span>（{{item.add_time}}）</span>
                  </div>
                  <div>
                    {{item.message}}
                  </div>
                  <div>
                    <a @click="deleteMessage(index, item.id)">删除</a>
                    <a v-if="item.file" :href="(item.file)" target="_blank">查看上传的文件</a>
                  </div>
                </li>
              </ul>
            </div>
            <form action="" method="post" enctype="multipart/form-data" name="formMsg">
              <table width="100%" border="0" cellpadding="3">
                <tbody>
                  <tr>
                    <td align="right">留言类型：</td>
                    <td>
                      <input type="radio" id="one" value="1" checked v-model="message_type">
                      <label for="one">留言</label>
                      <input type="radio" id="two" value="2" v-model="message_type">
                      <label for="two">建议</label>
                      <input type="radio" id="three" value="3" v-model="message_type">
                      <label for="three">上传</label>
                    </td>
                  </tr>
                <tr>
                  <td align="right">主题：</td>
                  <td><input name="msg_title" type="text" size="30" class="inputBg" v-model="subject"></td>
                </tr>
                <tr>
                  <td align="right" valign="top">留言内容：</td>
                  <td><textarea name="msg_content" cols="50" rows="4" wrap="virtual" class="B_blue" v-model="message"></textarea></td>
                </tr>
                <tr v-if="message_type == 3">
                  <td align="right">上传文件：</td>
                  <td><input type="file" name="message_img" size="45" class="inputBg" @change="preview"></td>
                </tr>
                <tr>
                  <td>&nbsp;</td>
                  <td><input type="hidden" name="act" value="act_add_message">
                    <a class="btn_blue_1" @click="submitMessage">提交</a>
                  </td>
                </tr>
              </tbody></table>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import {getMessages, addMessage, delMessages} from '../../api/api'
    export default {
      data () {
        return {
          message_type: 1, // 留言类型
          subject: '', // 留言主题
          message: '', // 留言内容
          file: '',
          messageAll: []
        };
      },
      created () {
        this.getMessage();
      },
      methods: {
        preview (e) {
          this.file = e.target.files[0]; //获取文件资源
          console.log(this.file);
        },
        submitMessage () { //提交留言
          const formData = new FormData();
          formData.append('file',this.file);
          formData.append('subject',this.subject);
          formData.append('message',this.message);
          formData.append('message_type',this.message_type);
          addMessage(formData).then((response)=> {
            this.getMessage();
          }).catch(function (error) {
            console.log(error);
          });
        },
        getMessage () { //获取留言
          getMessages().then((response)=> {
            console.log(response.data);
            this.messageAll = response.data;
          }).catch(function (error) {
            console.log(error);
          });
        },
        deleteMessage (index, id) { // 删除留言
          delMessages(id).then((response)=> {
            alert("删除成功")
            this.messageAll.splice(index,1);
          }).catch(function (error) {
            console.log(error);
          });
        },
      }
    }
</script>
<style scoped>
.message-all {
    border-bottom: 1px solid #ccc;
}
.message-all  li{
    border-bottom: 1px solid #ddd;
    padding: 10px;
}

.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.ilizi_centre {
    background:0
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
.ilizi_centre {
    background:0
}
.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff
}
.ilizi .face img,.iface .face img {
    width:100px;
    height:100px;
    border:1px solid #e4e4e4
}
.btn_blue_1{
  display: inline-block;
  padding: 4px 12px;
  height: 24px;
  line-height: 17px;
  border: 1px solid #1e9246;
  border-radius: 3px;
  font-size: 100%;
  color: #fff;
  background-color: #09c762;
  overflow: hidden;
  vertical-align: middle;
  cursor: pointer;
  text-decoration: none;
}
</style>
