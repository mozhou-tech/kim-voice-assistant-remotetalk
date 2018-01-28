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
                  <span class="tag is-success">在线</span>
                  <!--<span class="tag is-dark">Dark</span>-->
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                  <table class="table">
                    <tr><td>设备编码</td><td>3425345jeskg898sdf</td></tr>
                    <tr><td>设备名称</td><td>小云智能窗帘</td></tr>
                    <tr><td>唤醒热词</td><td>小云</td></tr>
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
  components: {
  },
  data () {
    return {

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

</style>
