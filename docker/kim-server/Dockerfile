FROM tenstone/kim-server-base-env
LABEL author=tenstone

ENV PROJECT_DIR="kim-voice-assistant-server" PROJECT_GIT_PATH="https://github.com/tenstone/kim-voice-assistant-server.git"

# 进入工作目录
WORKDIR /usr/src/app
COPY . .

ADD https://api.github.com/repos/tenstone/$PROJECT_DIR/git/refs/heads/master version.json
RUN git clone $PROJECT_GIT_PATH && git pull

# 处理项目文件
WORKDIR /usr/src/app/$PROJECT_DIR

RUN cp setting-example.yaml setting.yaml&& \
    echo '1' >/dev/null && git pull && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/$PROJECT_DIR/app/client/app

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org &&\
    cnpm install &&\
    npm run build &&\
    rm -rf node_modules

WORKDIR /usr/src/app/$PROJECT_DIR

CMD [ "python", "run.py" , "&"]