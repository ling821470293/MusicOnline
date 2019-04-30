<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
      <div class="box">
        <div class="box_1">
          <div class="userCenterBox" style="_height:1%;">
            <h5><span>个人资料</span></h5>
              <div class="blank"></div>
              <form name="formEdit" action="" method="post">
                <table width="100%" border="0" cellpadding="20" cellspacing="0" bgcolor="#dddddd">
                  <tbody>
                    <tr>
                      <td width="28%" align="right" bgcolor="#FFFFFF">昵称： </td>
                      <td width="72%" align="left" bgcolor="#FFFFFF"><input name="name" type="text" placeholder="" size="25" class="inputBg" v-model="userInfo.name"></td>
                    </tr>
                    <tr>
                      <td width="28%" align="right" bgcolor="#FFFFFF">出生日期： </td>
                      <td align="left" bgcolor="#FFFFFF">
                        <DatePicker type="date" v-model="userInfo.birthday" format="yyyy-MM-dd" placeholder="Select date" style="width: 150px"></DatePicker>
                      </td>
                    </tr>
                    <tr>
                      <td width="28%" align="right" bgcolor="#FFFFFF">性　别： </td>
                      <td width="72%" align="left" bgcolor="#FFFFFF">
                        <input type="radio" id="male" value="male" v-model="userInfo.gender">
                        <label for="male">男</label>
                        <input type="radio" id="female" value="female" v-model="userInfo.gender">
                        <label for="female">女</label>
                      </td>
                    </tr>
                    <tr>
                      <td width="28%" align="right" bgcolor="#FFFFFF">电子邮件地址： </td>
                      <td width="72%" align="left" bgcolor="#FFFFFF"><input name="email" type="text" placeholder="xxxx@xx.com" size="25" class="inputBg" v-model="userInfo.email"></td>
                    </tr>
                    <tr>
                      <td width="28%" align="right" bgcolor="#FFFFFF" id="extend_field5i">手机：</td>
                      <td width="72%" align="left" bgcolor="#FFFFFF">
                        <input disabled name="mobile" type="text" class="inputBg" v-model="userInfo.mobile">
                      </td>
                    </tr>
                    <tr>
                      <td colspan="2" align="center" bgcolor="#FFFFFF">
                        <a class="btn_blue_1" style="border:none;" @click="confirmModify">确认修改</a>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </form>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {getUserDetail, updateUserInfo} from '../../api/api'
    export default {
      data () {
        return {
          userInfo: {
            name: '',
            birthday: '',
            sex: '',
            email: '',
            mobile: '',
          },
        };
      },
      created () {
          this.getUserInfo();
      },
      methods: {
        getUserInfo () { //请求用户信息
          getUserDetail().then((response)=> {
            console.log(response.data)
            this.userInfo = response.data;
          }).catch(function (error) {
            console.log(error);
          });
        },
        confirmModify () { // 确认修改
          let time = this.userInfo.birthday
          if(time.length !== 10){
            let year = time.getFullYear()
            let month = time.getMonth() + 1
            let day = time.getDate()
            this.userInfo.birthday = year + '-' + month + '-' + day
          }
          updateUserInfo(this.userInfo).then((response)=> {
            alert('修改成功');
            this.getUserInfo()
          }).catch(function (error) {
            console.log(error);
          });
        },
      },
    }
</script>
<style scoped>
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
.ilizi_centre {
    background:0
}
.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff;
    position: relative;
}
.btn_blue_1{
  display: inline-block;
  padding: 4px 12px;
  height: 24px;
  line-height: 18px;
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
input[type=text]{
  border: 1px solid #aaa;
  border-radius: 3px;
  padding: 2px 5px 1px;
}
tr{
  height: 35px;
}


</style>




