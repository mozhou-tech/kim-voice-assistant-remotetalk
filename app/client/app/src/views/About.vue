<template>
  <section>

    <div class="container">
         <section>

            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  关于
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                       <br>
                  <h4>项目介绍</h4>

                  <p>
                    小云智能音箱是一个开源的智能家居方案，灵感来自外国友人的<a href="https://github.com/jasperproject/jasper-client" target="_blank">"Jasper Voice Computing Platform"</a>。
                      除客户端外，小云可以通过部署云端服务，提供远端APP控制和OpenAPI对接能力，增加可玩性。</p>
                    <p>小云与阿里云的深度融合，使设备可以方便的使用云端能力，让开源智能音箱更加"智能化"，充满魅力。
                  </p>
                    <br>
                  <h4>作者信息</h4>

                  <p>
                    姓名：刘远程<br/>
                    邮箱：<a href="mailto:tenstone@foxmail.com" target="_blank">tenstone@foxmail.com</a><br/>
                    Github：<a href="https://github.com/tenstone" target="_blank">https://github.com/tenstone</a>
                  </p>
                    <br>
                  <h4>开源协议</h4>
                  <p>MIT License</p>

                  <p>

                  Copyright (c) 2018 刘远程
                  </p>
                  <p>
                  Permission is hereby granted, free of charge, to any person obtaining a copy
                  of this software and associated documentation files (the "Software"), to deal
                  in the Software without restriction, including without limitation the rights
                  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
                  copies of the Software, and to permit persons to whom the Software is
                    furnished to do so, subject to the following conditions:</p>
                  <p>
                  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.</p>
                  <p>
                  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
                  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
                  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
                  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
                  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
                  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
                  SOFTWARE.
                  </p>

                </div>
              </div>
              <footer class="card-footer">

              </footer>
            </div>

        </section>
    </div>

  </section>
</template>
<script>

export default {
  name: 'Property',

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
