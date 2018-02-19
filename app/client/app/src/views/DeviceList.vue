<template>

  <section>

    <div class="container">
        <section>

            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  设备状态
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
                  <table class="table">
                    <tr><td>设备名称</td><td>{{ deviceStat.DeviceName }}</td></tr>
                    <tr><td>设备编码</td><td>{{ deviceStat.DeviceId || 'empty'}}</td></tr>
                    <tr><td>最近在线</td><td>{{ deviceStat.LastOnlineTime }}</td></tr>
                  </table>
                </div>
              </div>
              <footer class="card-footer">
                <router-link :to="{ path: '/device/log'}" class="card-footer-item">查看日志</router-link>
                <router-link :to="{ path: '/device/chat'}" class="card-footer-item">设备会话</router-link>
              </footer>
            </div>
        </section>
    </div>

  </section>
</template>
<script>

export default {
  name: 'Property',
  mounted () {

  },
  components: {
  },
  data () {
    return {

    }
  },
  computed: {
    deviceStat () {
      return this.$store.state.deviceStat
    }
  },
  methods: {

  }
}
</script>

<style lang="sass" scoped>

</style>
