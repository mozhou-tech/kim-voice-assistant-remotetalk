<template>
  <section>

    <div class="container">
      <section>
        <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  设备会话
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                   asdf
                </div>
              </div>
              <footer class="card-footer">
                <div class="field has-addons" style="width: 100%;">
                  <div class="control" style="width: 70%;">
                    <input class="input" type="text" placeholder="你想说点啥？">
                  </div>
                  <div class="control" style="width: 30%;">
                    <a class="button is-info">
                      发送消息
                    </a>
                  </div>
                </div>
              </footer>
            </div>
      </section>
    </div>

  </section>
</template>
<script>

export default {
  name: 'DeviceChat',
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
.card .content
  height: 500px
.card .card-footer
  width: 100%
</style>
