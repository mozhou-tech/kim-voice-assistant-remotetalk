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
                    <figure class="image" style="width: 40%;margin: 26px 30%;">
                        <img src="/dist/logo.png" alt="">
                         <figcaption style="font-size: 16px;font-style: normal;color: #3d3d3d;margin-top: 8px;">{{ title_desc }}</figcaption>
                    </figure>
                  <p>
                  <h4>项目介绍</h4>
                    <p>"{{ title }}"是一个开源的语音交互方案，灵感来自外国友人的<a href="https://github.com/jasperproject/jasper-client" target="_blank">"Jasper Client"</a>。
                      除客户端外，{{ short_title }}可以通过部署云端服务，提供远端APP控制和API接入能力，增加可玩性。
                    <p>{{ short_title }}与阿里云的深度融合，使设备对云端能力触手可及，让你的私人语音助理更加"智能化"，充满魅力。
                    <p>除此之外，{{ short_title }}的目标是将智能语音助理与智能家居系统无缝结合，我们已经支持著名开源智能家居系统<a href="https://home-assistant.io/" target="_blank">"HomeAssistant"</a>，支持小米、博联等主流品牌的智能家居设备。
                    <p>项目地址：
                    <ul>
                    <li>
                        <a href="https://github.com/tenstone/kim-voice-assistant-iot-client">语音助理设备端</a>
                    </li>
                    <li>
                        <a href="https://github.com/tenstone/kim-voice-assistant-server">远程会话端</a>
                    </li>
                    <li>
                        <a href="https://github.com/tenstone/kim-voice-assistant-dock">Docker安装镜像</a>
                    </li>
                </ul>
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
                    <br>
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
  mounted () {
    if (this.$store.state.isAuth === false) {
      this.$router.push('/')
    }
  },
  data () {
    return {

    }
  },
  computed: {
    title: function () {
      return this.$store.state.title
    },
    short_title: function () {
      return this.$store.state.short_title
    },
    title_desc: function () {
      return this.$store.state.title_desc
    }
  }
}
</script>

<style lang="sass" scoped>

</style>
