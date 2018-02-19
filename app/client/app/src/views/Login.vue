<template>
  <section>
    <div class="level login-logo">
      <div class="level-item has-text-centered">
          <img src="../assets/img/logo.png">
      </div>
    </div>
    <br>
    <div class="level">
       <div class="level-item has-text-centered is-fullwidth">
            <div class="field has-addons">
              <div class="control">
                <input class="input is-fullwidth" type="text" placeholder="访问密码">
              </div>
              <div class="control">
                <a class="button is-black" v-on:click="$router.push('/device')">
                  进入
                </a>
              </div>
            </div>
      </div>
    </div>
    <div class="level">
      <div class="level-item title">
        <p> {{ $store.state.title }} </p>
      </div>
    </div>
</section>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {

    }
  },
  computed: {

  }
}
</script>

<style lang="sass" scoped>
.title
  font-size: 13px
  bottom: 150px

.login-logo
  margin-top: 150px

  img
    height: 150px

</style>
