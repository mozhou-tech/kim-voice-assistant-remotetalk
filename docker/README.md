
# docker 镜像地址

https://hub.docker.com/r/mosch/raspberry-pi-snowboy/
https://hub.docker.com/r/resin/rpi-raspbian/'

# 使用方法
需要先安装docker，然后执行以下命令来使用服务。

使用作者构建的镜像：
```bash
docker run -itd -p 80:80 tenstone/kim-server
```

# 构建镜像
```bash
cd docker/kim-server
docker build -t --no-cache <镜像名称> .
```
