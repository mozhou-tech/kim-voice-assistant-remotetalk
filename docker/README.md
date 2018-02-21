
# docker 镜像地址

https://hub.docker.com/r/mosch/raspberry-pi-snowboy/
https://hub.docker.com/r/resin/rpi-raspbian/'

# 使用方法
需要先安装docker，然后执行以下命令来使用服务。
```bash
docker run -itd -p 80:80 tenstone/kim-server
```

docker build -t --no-cache kimserver kim-server/.
