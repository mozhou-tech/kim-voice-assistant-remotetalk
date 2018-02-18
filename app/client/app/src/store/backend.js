import axios from 'axios'


let $backend = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
});

$backend.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log(error);
  return Promise.reject(error)
});

export default {

  fetchDeviceConversationLog () {
    console.log('get device conversation logs');
    return $backend.get(`device/log`)
      .then(response => response.data)
  },
  fetchDeviceStat () {
    return $backend.get('/device/stat').then(response => response.data)
  },
  sendChatMessage (message) {
    console.log('send chat message.')
    console.log(message)
    return $backend.post(`device/chat`, {data: message})
      .then(response => response.data)
  },
  listenChatMessageBack () {
    return $backend.get('/device/chat/listen').then(response => response.data)
  }
}
