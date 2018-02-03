import Vue from 'vue'
import backend from './backend'

export default {

  fetchDeviceConversationLog: function  (context) {
    backend.fetchDeviceConversationLog().then((responseData) => {
      context.commit('setDeviceConversationLog', responseData)
    })
  },

  sendChatMessage: function  (context, message) {
  	backend.sendChatMessage(message).then((responseData) => {
  	    console.log(responseData);
  	})
  }
}
