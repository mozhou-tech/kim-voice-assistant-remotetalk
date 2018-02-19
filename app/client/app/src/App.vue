<template>
<div>

    <nav>
        <router-view name="navbar"></router-view>
        <router-view name="subnavbar"></router-view>
    </nav>

    <section class="section">
      <transition name="fade">
        <div class="container">
          <router-view name="main"></router-view>
        </div>
      </transition>
    </section>

</div>
</template>

<script>

export default {
  name: 'Property',
  mounted () {
    this.pollingDeviceStat()
    this.$store.dispatch('fetchDeviceStat')
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
    pollingDeviceStat () {
      let _this = this
      if (this.$store.state.statPollingOpen === false) {
        this.$store.commit('setStatPollingOpen', true)
        _this.chatTimer = setInterval(function () {
          _this.$store.dispatch('fetchDeviceStat')
        }, 4000)
      }
    }
  }
}
</script>

<style lang="sass">
// Main.sass is imported into all Components using Webpack Data Parameter

</style>
