<template>
  <section>

    <div class="container">
        <section>
            <router-view></router-view>
        </section>
    </div>

  </section>
</template>
<script>

export default {
  name: 'Property',
  mounted () {
    if (this.$store.state.isAuth === false) {
      this.$router.push('/')
    }
  },
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
