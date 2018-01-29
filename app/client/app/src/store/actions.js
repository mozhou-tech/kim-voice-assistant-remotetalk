import Vue from 'vue'
import backend from './backend'

export default {

  getDeviceLog: function  (context) {
    backend.getDeviceLog().then((responseData) => {
      context.commit('setResource', responseData)
    })
  },

  fetchResourceTwo: function  (context, resourceId) {
  	backend.fetchResourceTwo(resourceId).then((responseData) => {
  		context.commit('setResource', responseData)
  	})
  }
}
