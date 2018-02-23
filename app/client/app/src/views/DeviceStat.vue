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
                    <span v-if="deviceStat.Status === 'ONLINE'">
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
                    <tr><td>设备名称</td><td>{{ deviceStat.DeviceName+' ( ' + deviceStat.cfg_myname + ' )' || 'empty' }}</td></tr>
                    <tr><td>设备编码</td><td>{{ deviceStat.DeviceId || 'empty'}}</td></tr>
                    <tr><td>软件版本</td><td>{{ deviceStat.cfg_device_client_version }}</td></tr>
                    <tr><td>热词模型</td><td>{{ deviceStat.cfg_hotword_files }}</td></tr>
                    <tr><td>设备IP</td><td>{{ deviceStat.cfg_local_ip || 'empty' }}</td></tr>
                    <tr><td>城市/时区</td><td>{{ deviceStat.cfg_city +'，'+ deviceStat.cfg_timezone || 'empty' }}</td></tr>
                    <tr><td>远程会话</td><td>{{ deviceStat.cfg_remote_control_service_enable?'已开启':'已关闭 ( 开启后可对话 )' || '否' }}</td></tr>
                    <tr><td>最近在线</td><td>{{ deviceStat.LastOnlineTime || 'empty' }}</td></tr>
                  </table>
                </div>
              </div>
              <footer class="card-footer">
                  <router-link :to="{ path: '/device/log'}" class="card-footer-item">查看日志</router-link>
                  <router-link v-if="deviceStat.cfg_remote_control_service_enable" :to="{ path: '/device/chat'}" class="card-footer-item">设备会话</router-link>
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
    console.log(this.$store.state.apiToken)
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
