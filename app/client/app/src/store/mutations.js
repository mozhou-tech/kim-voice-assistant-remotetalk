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
  }
}

