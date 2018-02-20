<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item">
        <div class="image is-24x24" style="display: block;">
          <img src="../assets/img/logo.png" style="height: 24px;">
        </div>
      </a>
      <a class="navbar-item">
        KIM智能语音助理&nbsp;&nbsp;<small> {{version}}</small>
      </a>
    </div>
  </nav>
</template>
<script>

export default {
  name: 'Navbar',
  data () {
    return {
    }
  },
  computed: {
    version: function () {
      return this.$store.state.version
    }
  }
}
</script>

<style lang="sass" scoped>

nav.navbar
  min-height: none
  background-color: $nav-background
  border-bottom: solid 1px #dbdbdb

.navbar-brand > .navbar-item
  padding-left: 10px

  img
    height: 15px

</style>
