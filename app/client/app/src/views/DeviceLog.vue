<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">设备运行日志</p>
        <div class="card-header-icon">
         <button class="button is-link is-small is-outlined" v-on:click="refreshConversations()">刷新数据</button>
        </div>
      </header>
      <div class="card-content">
        <div class="content">
          <table class="table">
              <thead>
                <tr>
                  <th width="120px"><abbr title="Position">设备</abbr></th>
                  <th width="120px"><abbr title="Won">时间</abbr></th>
                  <th><abbr title="Played">对话信息</abbr></th>
                </tr>
              </thead>
              <tbody>
                <tr v-on:click="openModal(item)" v-for="item in device_conversation_logs">
                  <td>{{ item.device }}</td>
                  <td>{{ item.timestamp | formatDate }}</td>
                  <td>{{ item.content | shortContent }}</td>
                </tr>
              </tbody>
            </table>
        </div>
      </div>
    </div>
    <div class="modal" v-bind:class="{'is-active':isModalActive}">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">交互设备： {{ chosenItem.device }}</p>
          <button class="delete" aria-label="close" v-on:click="closeModal"></button>
        </header>
        <section class="modal-card-body">
          <table class="table">
            <tr><td>mic</td><td>{{ chosenItem.mic }}</td></tr>
            <tr><td>speaker</td><td>{{ chosenItem.speaker }}</td></tr>
            <tr><td>内容</td><td>{{ chosenItem.content }}</td></tr>
            <tr><td>时间</td><td>{{ chosenItem.timestamp | formatDate }}</td></tr>
          </table>
        </section>
        <footer class="modal-card-foot">
          <button class="button" v-on:click="closeModal">关闭</button>
        </footer>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  name: 'DeviceLog',
  mounted () {
    this.refreshConversations()
  },
  data () {
    return {
      isModalActive: false,
      chosenItem: ''
    }
  },
  computed: {
    device_conversation_logs () {
      return this.$store.state.device_conversation_logs
    }
  },
  methods: {
    refreshConversations () {
      this.$store.dispatch('fetchDeviceConversationLog')
    },
    closeModal () {
      this.isModalActive = false
    },
    openModal (item) {
      this.chosenItem = item
      this.isModalActive = true
    }
  }
}
</script>

<style lang="sass" scoped>

</style>
