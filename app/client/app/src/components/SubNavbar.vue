<template>
  <nav class="tabs is-small">
    <ul>
      <router-link tag="li" activeClass='is-active' :to="{ path: 'status'}"><a>设备状态</a></router-link>
      <router-link tag="li" activeClass='is-active' :to="{ path: 'chat'}"><a>设备交互</a></router-link>
      <router-link tag="li" activeClass='is-active' :to="{ path: 'log'}"><a>运行日志</a></router-link>
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
