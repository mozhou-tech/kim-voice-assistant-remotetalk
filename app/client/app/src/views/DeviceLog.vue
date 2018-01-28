<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">设备运行日志</p>
      </header>
      <div class="card-content">
        <div class="content">
          <table class="table">
              <thead>
                <tr>
                  <th><abbr title="Position">设备名</abbr></th>
                  <th><abbr title="Won">日志信息</abbr></th>
                  <th><abbr title="Played">时间</abbr></th>
                </tr>
              </thead>
              <tbody>
                <tr v-on:click="openModal()">
                  <th>1</th>
                  <td>Leicester City</td>
                  <td>2018-01-28 19:18:05</td>
                </tr>
              </tbody>
            </table>
        </div>
      </div>
    </div>
    <div class="modal" v-bind:class="{'is-active':isModalActive}">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">日志内容</p>
          <button class="delete" aria-label="close" v-on:click="closeModal"></button>
        </header>
        <section class="modal-card-body">
          <p>日志内容写在这</p>
        </section>
        <footer class="modal-card-foot">
          <button class="button" v-on:click="closeModal">关闭</button>
        </footer>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  name: 'DeviceLog',
  data () {
    return {
      isModalActive: false
    }
  },
  computed: {
    fancyTitle () {
      return this.title
    }
  },
  methods: {
    closeModal () {
      this.isModalActive = false
    },
    openModal () {
      this.isModalActive = true
    }
  },
  mounted () {
    // Do something
  }
}
</script>

<style lang="sass" scoped>

</style>
