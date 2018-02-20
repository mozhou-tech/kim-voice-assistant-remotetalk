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
          <div class="card-content" style="">
            <div class="content" ref="chatbox" v-bind:style="{height: + (pageHeight - 250)+'px'}">
               <ul style="list-style-type: none;" id="chat-wrap">
                <li v-for="item in chatItems" :class="'chat-item '+item.speaker">
                    <div class="chat-avatar flex-item">
                        <span v-if="item.speaker === 'device'">Kim</span>
                    </div>
                    <div class="chat-device-arrow flex-item"></div>
                    <div class="chat-text flex-item">
                      <span>{{ item.text }} &nbsp;&nbsp;&nbsp;<small style="color: darkgrey">{{ item.time }}</small></span>
                    </div>
                    <div class="chat-user-arrow flex-item"></div>
                    <div class="chat-avatar flex-item">
                        <span v-if="item.speaker === 'user'">You</span>
                    </div>
                </li>
                <li v-if="chatItems.length === 0">暂无对话，请发送消息给我吧</li>
               </ul>
            </div>
          </div>
          <footer class="card-footer">
            <div class="field has-addons" style="width: 100%;">
              <div class="control is-expanded">
                <input class="input" ref='chatinput' v-model="message" type="text" autofocus
                       v-on:keyup.13="sendChatMessage()"
                       :readonly="deviceStat.Status!=='ONLINE'"
                       placeholder="你想说点啥？">
              </div>
              <div class="control">
                <button type="button" class="button is-info" v-on:click="sendChatMessage()" :disabled="deviceStat.Status!='ONLINE'">
                  &nbsp;发射 🚀&nbsp;
                </button>
              </div>
            </div>
        </footer>
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
      pageHeight: 0
    }
  },
  mounted () {
    this.listenChatMessageBack()
    this.setChatboxHeight(0)
    this.chatBoxScrollToBottom(20)
  },
  methods: {
    setChatboxHeight: function (delay) {
      let _this = this
      setTimeout(function () {
        _this.pageHeight = window.innerHeight
        console.log(_this.pageHeight)
      }, delay)
    },
    chatBoxScrollToBottom: function (delay) { // 两天窗口滚动到底部
      let _this = this
      setTimeout(function () {
        _this.$refs.chatbox.scrollTop = _this.$refs.chatbox.scrollHeight + 600
      }, delay)
    },
    sendChatMessage: function () { // 发送聊天消息
      if (this.message === '') {
        return false
      }
      if (this.deviceStat.Status === 'ONLINE') {
        this.$store.commit('setLastConversationAt', new Date().getTime())
        this.$store.dispatch('sendChatMessage', this.message)
        this.andChatItem(this.message)
        this.message = ''
        this.$refs.chatinput.focus()
      }
    },
    andChatItem: function (text) { // 想本地存储添加一个聊天内容条目
      this.$store.commit('appendChatItem', {content: text, speaker: 'user', timestamp: new Date().getTime()})
      this.chatBoxScrollToBottom(20)
    },
    listenChatMessageBack: function () { // 定时监听聊天消息
      let _this = this
      if (this.$store.state.chatPollingOpen === false) {
        this.$store.commit('setChatPollingOpen', true)
        setInterval(function () {
          _this.$store.dispatch('listenChatMessageBack')
        }, 2000)
      }
    }
  },
  watch: {
    '$store.state.chatItems': function () {
      this.chatBoxScrollToBottom(20)
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

<style lang="css" scoped>
.card-content{padding: 8px;margin: 0;padding-bottom: 18px;}
.card .content{
   overflow: scroll;
}
.card .content ul{
   margin: 0;padding: 0;margin-top: 13px;
}
#chat-wrap li.chat-item{display: flex;flex-direction: row;}
#chat-wrap li.chat-item>.flex-item{ flex: auto }
#chat-wrap li.user{align-items: right;text-align: right}
#chat-wrap li.chat-item .chat-avatar{width:6%;}
#chat-wrap li .chat-text{
   font-size: 14px;
   display: block;
   color: #3d3d3d;
   background: #EEEEEE;
   border-radius: 3px;
   padding: 4px;
   width: 80%;
}
#chat-wrap li.user .chat-text{ background: #eee;align-content: flex-end;}
#chat-wrap li.device .chat-text{background: #b5e5f4;align-content: flex-start;}
#chat-wrap li .user .arrow{
  width: 0;
  height: 0;
  border-top: 60px solid transparent;
  border-bottom: 60px solid transparent;
  border-left: 60px solid green;
}
</style>
