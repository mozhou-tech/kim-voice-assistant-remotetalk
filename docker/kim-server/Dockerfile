FROM tenstone/kim-server-base-env
LABEL author=tenstone

ENV PROJECT_DIR="kim-voice-assistant-server" PROJECT_GIT_PATH="https://github.com/tenstone/kim-voice-assistant-server.git"
ENV BASE_PATH "/app"

# 进入工作目录
WORKDIR $BASE_PATH

ADD https://api.github.com/repos/tenstone/$PROJECT_DIR/git/refs/heads/master version.json
RUN git clone $PROJECT_GIT_PATH

# 处理项目文件
WORKDIR $BASE_PATH/$PROJECT_DIR
COPY . .

RUN cp setting-example.yaml setting.yaml \
    && cp -f nginx.conf /etc/nginx/nginx.conf \
    && rm -f /etc/nginx/conf.d/default.conf \
    && git pull \
    # uwsgi python plugin
    && apk --no-cache add uwsgi-python3 \
    && pip install --no-cache-dir -r requirements.txt


WORKDIR $BASE_PATH/$PROJECT_DIR/app/client/app

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org \
    && cnpm install \
    && npm run build \
    && rm -rf node_modules

WORKDIR $BASE_PATH/$PROJECT_DIR
RUN chown nginx:nginx * -R && chmod +x start.sh

CMD "./start.sh"

