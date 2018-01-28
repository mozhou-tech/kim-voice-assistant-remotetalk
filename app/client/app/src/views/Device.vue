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
                  在线
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.
                  <a href="#">@bulmaio</a>. <a href="#">#css</a> <a href="#">#responsive</a>
                  <br>
                  <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
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
