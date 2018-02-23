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
                <input class="input is-fullwidth" v-on:keyup.13="checkPasswd()" v-model="passwd" type="password" placeholder="密码">
              </div>
              <div class="control">
                <a class="button is-black" v-on:click="checkPasswd()">
                  进入
                </a>
              </div>
            </div>
      </div>
    </div>
    <div class="level">
      <div class="level-item title has-text-centered">
        <p> {{ $store.state.title_desc }} </p>
      </div>
    </div>
    <div class="level">
            <div class="level-item has-text-centered is-fullwidth"><p style="text-align: center;"> {{ errmsg }} </p></div>
    </div>
</section>
</template>

<script>

import backend from '../store/backend'

export default {
  name: 'Login',
  data () {
    return {
      passwd: '',
      errmsg: ''
    }
  },
  mounted () {
    if (this.$store.state.isAuth) {
      this.$router.push('/device')
    }
  },
  methods: {
    checkPasswd: function () {
      backend.checkPasswd(this.passwd).then((responseData) => {
        if (responseData.errcode === 0) {
          this.$store.commit('setApiToken', responseData.data.api_token)
          this.$store.commit('setIsAuth', true)
          this.$router.push('/device')
        } else {
          this.errmsg = responseData.errmsg
          this.$store.commit('setIsAuth', false)
        }
      })
    }
  },
  computed: {

  },
  components: {
    backend
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
