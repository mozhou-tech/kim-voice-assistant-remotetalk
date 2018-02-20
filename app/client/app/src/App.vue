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
    document.title = this.$store.state.title + ' —— 为你打造的私人助理'
  },
  components: {
  },
  data () {
    return {

    }
  },
  watch: {
    '$store.state.apiToken': function () {
      this.$store.dispatch('fetchDeviceStat')
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
        }, 5000)
      }
    }
  }
}
</script>

<style lang="sass">
// Main.sass is imported into all Components using Webpack Data Parameter

</style>
