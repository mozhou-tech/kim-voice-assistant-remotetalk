import Vue from 'vue'
import backend from './backend'

export default {

  fetchDeviceConversationLog: function  (context) {
    backend.fetchDeviceConversationLog().then((responseData) => {
      context.commit('setDeviceConversationLog', responseData)
    })
  },
  fetchDeviceStat: function (context) {
    backend.fetchDeviceStat().then((responseData) => {
      if (responseData.errcode === 0) {
        context.commit('setDeviceStat', responseData.data)
      }
    })
  },
  sendChatMessage: function (context, message) {
    backend.sendChatMessage(message).then((responseData) => {
      console.log(responseData)
    })
  },
  listenChatMessageBack: function (context) {
    backend.listenChatMessageBack(context.state.lastConversationAt).then((responseData) => {
      if (responseData.errcode === 0 && responseData.data.logs) {
        responseData.data.logs.forEach(function (elem, i) {
          if (elem.mic === 'server' && elem.speaker === 'device') {
            context.commit('appendChatItem', elem.content)
            context.commit('setLastConversationAt', new Date().getTime())
          }
        })
      }
    })
  }
}
