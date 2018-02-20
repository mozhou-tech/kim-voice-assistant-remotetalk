<template>
  <nav class="tabs is-small">
    <ul>
      <router-link tag="li" activeClass='is-active' :to="{ path: '/device/list'}"><a>我的设备</a></router-link>
      <router-link tag="li" activeClass='is-active' :to="{ path: '/about'}"><a>关于</a></router-link>
      <span v-on:click="logout()">
        <router-link tag="li" :to="{ path: '/' }"><a>退出</a></router-link>
      </span>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'SubNavbar',
  methods: {
    logout: function () {
      this.$store.commit('setIsAuth', false)
      this.$router.push('/')
    }
  }
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)
</style>
