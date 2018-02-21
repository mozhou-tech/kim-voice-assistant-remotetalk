FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
LABEL author=tenstone
ENV NODE_VERSION 9.4.0

    # 配置国内镜像，安装一些包
RUN echo -e "http://mirrors.aliyun.com/alpine/v3.7/main\nhttp://mirrors.aliyun.com/alpine/v3.7/community" > /etc/apk/repositories \
    && mkdir ~/.pip/ \
    && echo -e "[global]\nindex-url = http://mirrors.aliyun.com/pypi/simple/\n\n[install]\ntrusted-host=mirrors.aliyun.com" > ~/.pip/pip.conf \
    && apk --no-cache add git gcc g++ make nginx uwsgi libffi-dev openssl-dev \
    && mkdir /run/nginx \
    # 安装 node，参考 https://github.com/nodejs/docker-node/blob/master/9/alpine/Dockerfile
    && addgroup -g 1000 node \
    && adduser -u 1000 -G node -s /bin/sh -D node \
    && apk add --no-cache \
        libstdc++ \
    && apk add --no-cache --virtual .build-deps \
        binutils-gold \
        curl \
        python \
        gnupg \
        libgcc \
        linux-headers \
        make \
      # gpg keys listed at https://github.com/nodejs/node#release-team
      && for key in \
        94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
        FD3A5288F042B6850C66B31F09FE44734EB7990E \
        71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
        DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
        C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
        B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        56730D5401028683275BD23C23EFEFE93C4CFFFE \
        77984A986EBC2AA786BC0F66B01FBB92821C587A \
      ; do \
        gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \
        gpg --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" || \
        gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \
      done \
    && curl -SLO "https://npm.taobao.org/mirrors/node/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \
    && curl -SLO --compressed "https://npm.taobao.org/mirrors/node/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xf "node-v$NODE_VERSION.tar.xz" \
    && cd "node-v$NODE_VERSION" \
    && ./configure \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && apk del .build-deps \
    && cd .. \
    && rm -Rf "node-v$NODE_VERSION" \
    && rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && rm -rf /var/cache/apk/*
