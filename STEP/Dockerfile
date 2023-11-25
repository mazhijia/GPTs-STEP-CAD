# 使用基于 Anaconda 的基础镜像
FROM continuumio/miniconda3

# 暴露应用将要监听的端口 5000
EXPOSE 5000

# 设置工作目录
WORKDIR /app

# 将当前目录下的 Flask 应用和其他相关文件复制到容器中的 /app 目录
COPY . /app

# 使用 environment.yml 来创建一个 Anaconda 环境
RUN conda env create -f /app/environment.yml

# 设置环境变量，确保使用正确的 Anaconda 环境
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# 在容器内部创建一个目录来保存上传的 .step 文件
RUN mkdir -p /app/step_files

# 给刚创建的目录设置适当的权限
# 注意：在实际部署中，根据您的需要，这里可能还要涉及到用户和权限管理
RUN chmod 755 /app/step_files

# 设置一个环境变量，告诉您的 Flask 应用在哪里保存上传的文件
ENV STEP_FILES_PATH /app/step_files

# 用于在容器启动时运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]
