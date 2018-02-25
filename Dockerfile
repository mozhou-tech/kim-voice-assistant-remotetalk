FROM tenstone/kim-server:code-1.0

ENV PROJECT_DIR="kim-voice-assistant-remotetalk"  BASE_PATH="/app"
WORKDIR $BASE_PATH/$PROJECT_DIR

# 更新代码
RUN git pull --force
# 切换分支
#    && git branch

# 复制配置文件
COPY setting.yaml setting.yaml

# 编译前端文件
WORKDIR $BASE_PATH/$PROJECT_DIR/app/client/app/
RUN npm run build

# 回到工作目录
WORKDIR $BASE_PATH/$PROJECT_DIR