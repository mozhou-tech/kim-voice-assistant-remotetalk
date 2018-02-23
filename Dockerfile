FROM tenstone/kim-server:code-1.0

ENV PROJECT_DIR="kim-voice-assistant-server"  BASE_PATH="/app"
WORKDIR $BASE_PATH/$PROJECT_DIR

# 更新代码
RUN git reset --hard && git clean  -d  -fx "" && git pull --force
# 切换分支
#    && git branch

# 复制配置文件
COPY setting.yaml setting.yaml