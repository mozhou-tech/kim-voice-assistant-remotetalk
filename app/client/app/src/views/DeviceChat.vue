<template>
  <section>

    <div class="container">
      <section>
        <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  设备会话
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                   asdf
                </div>
              </div>

            </div>
          <div class="bottom">
            <div class="field has-addons" style="width: 100%;">
              <div class="control" style="width: 70%;">
                <input class="input" v-model="message" type="text" placeholder="你想说点啥？">
              </div>
              <div class="control" style="width: 30%;">
                <button type="submit" class="button is-info" v-on:click="sendChatMessage()">
                  发送消息
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
      message: ''
    }
  },
  methods: {
    sendChatMessage: function () {
      this.$store.dispatch('sendChatMessage', {data: this.message})
      console.log('send message: ' + this.message)
    }
  },
  computed: {
    isLoading () {
      return this.$store.state.isLoading
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
