import axios from 'axios';


let host = 'http://shop.projectsedu.com';
let localhost = 'http://127.0.0.1:8000';

//获取歌曲类别信息
// export const queryCategorysongs = params => { return axios.get(`${localhost}/indexsongs/`) }

//获取歌曲类别信息
export const getCategory = params => {
  if('id' in params){
    return axios.get(`${localhost}/categorys/`+params.id+'/');
  }
  else {
    return axios.get(`${localhost}/categorys/`, params);
  }
};


//获取热门搜索关键词
export const getHotSearch = params => { return axios.get(`${localhost}/hotsearchs/`) }

//获取歌曲列表
export const getSongs = params => { return axios.get(`${localhost}/songs/`, { params: params }) }

//获取歌手列表
export const getSingers = params => { return axios.get(`${localhost}/singers/`, { params: params }) }

//获取歌手列表
export const getCDs = params => { return axios.get(`${localhost}/cds/`, { params: params }) }

//歌曲详情
export const getSongsDetail = songId => { return axios.get(`${localhost}/songs/${songId}`+'/') }

//歌手详情
export const getSingersDetail = singerId => { return axios.get(`${localhost}/singers/${singerId}`+'/') }

//专辑详情
export const getCDsDetail = cdId => { return axios.get(`${localhost}/cds/${cdId}`+'/') }

//收藏
export const addFav = params => { return axios.post(`${localhost}/userfavs/`, params) }

//取消收藏
export const delFav = songsId => { return axios.delete(`${localhost}/userfavs/`+songsId+'/') }

export const getAllFavs = () => { return axios.get(`${localhost}/userfavs/`) }

//判断是否收藏
export const getFav = songsId => { return axios.get(`${localhost}/userfavs/`+songsId+'/') }

//登录
export const login = params => {
  return axios.post(`${localhost}/login/`, params)
}

//注册

export const register = parmas => { return axios.post(`${localhost}/users/`, parmas) }

//短信
export const getMessage = parmas => { return axios.post(`${localhost}/codes/`, parmas) }


//获取用户信息
export const getUserDetail = () => { return axios.get(`${localhost}/users/1/`) }

//修改用户信息
export const updateUserInfo = params => { return axios.put(`${localhost}/users/1/`, params) }

//获取留言
export const getMessages = () => {return axios.get(`${localhost}/messages/`)}

//添加留言
export const addMessage = params => {return axios.post(`${localhost}/messages/`, params, {headers:{ 'Content-Type': 'multipart/form-data' }})}

//删除留言
export const delMessages = messageId => {return axios.delete(`${localhost}/messages/`+messageId+'/')}
