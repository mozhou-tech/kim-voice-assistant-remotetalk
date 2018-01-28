<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{fancyTitle}}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          <table class="table">
              <thead>
                <tr>
                  <th><abbr title="Position">设备名称</abbr></th>
                  <th>设备IP</th>
                  <th><abbr title="Won">日志信息</abbr></th>
                  <th><abbr title="Played">时间</abbr></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th>1</th>
                  <td>Leicester City</td>
                  <td>38</td>
                  <td>121212</td>
                </tr>
              </tbody>
            </table>


        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'Log',
  data () {
    return {
      title: '设备运行日志'
    }
  },
  computed: {
    fancyTitle () {
      return this.title
    }
  },
  methods: {
    someMethod () {
      // Do Something
    }
  },
  mounted () {
    // Do something
  }
}
</script>

<style lang="sass" scoped>

</style>
