# 介绍 

Kim Voice Assistant是一款开源智能语音助理（智能音箱），灵感来自外国友人的开源项目 [jasper-client](http://jasperproject.github.io/)。Kim在安装、本土化、控制方式等方面提出了不少改进方案，使得项目更容易安装，可玩性也有不少提升。

[![GitHub issues](https://img.shields.io/github/issues/tenstone/kim-voice-assistant-iot-client.svg)](https://github.com/tenstone/kim-voice-assistant-iot-client/issues)
[![Python3.6](https://img.shields.io/badge/python3.6-green-brightgreen.svg)](https://www.python.org)
[![GitHub license](https://img.shields.io/github/license/tenstone/kim-voice-assistant-iot-client.svg)](https://github.com/tenstone/kim-voice-assistant-iot-client/blob/master/LICENSE)


## 特性

1. 基于Alibaba Cloud Services构建
1. 通过Docker管理运行环境，支持快速安装部署
1. 优化中文语义仲裁算法，更加精准的理解中文语义
2. 可选安装Web和OpenAPI控制方案，提供丰富的设备的控制方式
2. 支持树莓派（或其他物联网硬件）、macOS、PC，跨平台安装运行

## 组成

| 名称 | 描述 | 链接 |
|----|----|----|
| Kim Voice Assistant Iot Client | Kim设备端 | [Client](https://github.com/tenstone/kim-voice-assistant-iot-client) |
| Kim Voice Assistant Server | Kim远程会话端 | [Server](https://github.com/tenstone/kim-voice-assistant-server) |

当前模块为：Kim Voice Assistant Server 远程会话端

# 模块安装

## 通过Docker镜像

通过Dockerfile构建镜像需要在服务器中预先安装docker，Docker的安装方法请参见[官方文档](https://docs.docker.com/install/)。以下为安装步骤：

Step1：下载代码到本地（服务器） <br>
Step2：将setting-example.yaml复制为setting.yaml，并将对应的阿里云配置改成你自己的 <br>
Step3：运行 "docker build -t kim-server . " 命令构建镜像 <br>
Step4：运行 "docker run -itd -p 5004:80 kim-server" 启动服务（如果你使用阿里云ECS，请开放5004端口安全策略） <br>

TIPS：
1. 你可以通过配置Nginx反向代理（参照根目录"kim-server.conf"文件），通过80端口配置域名对外服务；
1. 修改根目录的Dockerfile可以指定运行的代码分支和版本。

以下为Docker管理的常见命令；
```bash
docker image ls # 查看镜像
docker ps # 查看正在运行的docker容器
docker ls -a # 查看所有容器
```

## 在Linux上部署安装
直接在裸机上安装需要复杂的环境配置工作，建议通过Docker镜像直接安装，或对docker目录下的Dockerfile反向工程。

# 参考

1. [Home Assistant中文文档](https://home-assistant-china.github.io)
1. [阿里云物联网套件文档](https://help.aliyun.com/product/30520.html?spm=5176.11065259.1996646101.3.5bb13cb4OI00HP)
1. [阿里云函数计算文档](https://help.aliyun.com/product/50980.html?spm=5176.11065259.1996646101.3.4aa04c2aAfJh0W)






