import Vue from 'vue'
import backend from './backend'

export default {

  fetchDeviceConversationLog: function  (context) {
    backend.fetchDeviceConversationLog().then((responseData) => {
      context.commit('setDeviceConversationLog', responseData)
    })
  },

  fetchResourceTwo: function  (context, resourceId) {
  	backend.fetchResourceTwo(resourceId).then((responseData) => {
  		context.commit('setResource', responseData)
  	})
  }
}
