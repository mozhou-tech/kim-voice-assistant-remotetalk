FROM tenstone/kim-remotetalk:base-v1.0
LABEL author=tenstone

ENV PROJECT_DIR="kim-voice-assistant-remotetalk" PROJECT_GIT_PATH="https://github.com/tenstone/kim-voice-assistant-remotetalk.git"
ENV BASE_PATH "/app"

# 进入工作目录
WORKDIR $BASE_PATH

ADD https://api.github.com/repos/tenstone/$PROJECT_DIR/git/refs/heads/master version.json
RUN git clone $PROJECT_GIT_PATH

# 处理项目文件
WORKDIR $BASE_PATH/$PROJECT_DIR
COPY . .

RUN cp -f nginx.conf /etc/nginx/nginx.conf \
    && rm -f /etc/nginx/conf.d/default.conf \
    && rm -f Dockerfile \
    && git pull \
    # uwsgi python plugin
    && apk --no-cache add uwsgi-python3 \
    && pip install --no-cache-dir -r requirements.txt


WORKDIR $BASE_PATH/$PROJECT_DIR/app/client/app

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org \
    && cnpm install \
    && npm run build

WORKDIR $BASE_PATH/$PROJECT_DIR
RUN chown nginx:nginx * -R && chmod +x start.sh

CMD "./start.sh"

