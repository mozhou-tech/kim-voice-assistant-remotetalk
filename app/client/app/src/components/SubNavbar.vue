<template>
  <nav class="tabs is-small">
    <ul>
      <router-link tag="li" activeClass='is-active' :to="{ path: '/device'}"><a>设备管理</a></router-link>
      <router-link tag="li" activeClass='is-active' :to="{ path: '/about'}"><a>关于</a></router-link>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'SubNavbar'
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
