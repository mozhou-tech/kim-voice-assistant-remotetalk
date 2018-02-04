import Vue from 'vue'

export default {

  setLoading: function (state, bool) {
    state.isLoading = bool
  },
  setResource: function (state, value) {
    state.resource = value
  },
  setDeviceConversationLog: function (state, value) {
    state.device_conversation_logs = value
  },
  appendChatItem: function (state, value) {
    let  date = new Date()
    if(state.chatItems.length > 10){
      state.chatItems.shift()
    }
    state.chatItems.push({text : value, time: date.getHours() + ':' + date.getMinutes()})
  }
}

