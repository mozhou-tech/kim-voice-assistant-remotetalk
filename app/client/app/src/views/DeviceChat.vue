<template>
  <section>

    <div class="container">
      <section>
        <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  设备会话
                </p>
                 <p class="card-header-icon">
                    <span v-if="deviceStat.Status == 'ONLINE'">
                      <span class="tag is-success">在线</span>
                    </span>
                    <span v-else>
                      <span class="tag">离线</span>
                    </span>
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                   <ul style="list-style-type: none;">
                    <li v-for="item in chatItems"> {{ item.text }} &nbsp;&nbsp;&nbsp;<small>{{ item.time }}</small></li>
                    <li v-if="chatItems.length == 0">暂无对话，请发送消息给我吧</li>
                   </ul>
                </div>
              </div>
            </div>
          <div class="bottom">
            <div class="field has-addons" style="width: 100%;">
              <div class="control" style="width: 70%;">
                <input class="input" ref='chat_input' v-model="message" type="text" autofocus
                       v-on:keyup.13="sendChatMessage()"
                       :readonly="chatInputReadonly || deviceStat.Status!=='ONLINE'"
                       placeholder="你想说点啥？">
              </div>
              <div class="control" style="width: 30%;">
                <button type="button" class="button is-info" v-on:click="sendChatMessage()" :disabled="deviceStat.Status!='ONLINE'">
                  发射
                </button>
              </div>
            </div>
          </div>
      </section>
    </div>
  </section>
</template>
<script>

export default {
  name: 'DeviceChat',
  data () {
    return {
      message: '',
      chatInputReadonly: false
    }
  },
  mounted () {
    this.listenChatMessageBack()
  },
  methods: {
    sendChatMessage: function () {
      if (this.deviceStat.Status === 'ONLINE') {
        this.$store.commit('setLastConversationAt', new Date().getTime())
        this.$store.dispatch('sendChatMessage', this.message)
        console.log('send message: ' + this.message)
        this.andChatItem(this.message)
        this.message = ''
        this.$refs.chat_input.focus()
      }
    },
    andChatItem: function (text) {
      this.$store.commit('appendChatItem', '我：' + text)
      console.log(this.$store.state.chatItems)
    },
    listenChatMessageBack: function () {
      let _this = this
      if (this.$store.state.chatPollingOpen === false) {
        this.$store.commit('setChatPollingOpen', true)
        setInterval(function () {
          _this.$store.dispatch('listenChatMessageBack')
        }, 2000)
      }
    }
  },
  computed: {
    chatItems () {
      return this.$store.state.chatItems
    },
    deviceStat () {
      return this.$store.state.deviceStat
    }
  }
}
</script>

<style lang="sass" scoped>
.card .content
  height: 500px
.bottom
  position: fixed
  bottom: 20px
  width: 100%
</style>
