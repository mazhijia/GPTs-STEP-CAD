# 使用包含 Anaconda 的基础镜像
FROM continuumio/miniconda3

# （可选）如果您的应用不需要使用 5000 端口，可以更改此处的端口号
EXPOSE 5000

# 设定工作目录
WORKDIR /app

# 复制您的 Flask 应用和 Anaconda 环境文件到容器中
COPY . /app

# 使用环境文件创建 Anaconda 环境
RUN conda env create -f /app/environment.yml

# 设置环境变量，确保在激活的 Anaconda 环境中运行命令
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# 确保使用的是我们创建的环境
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# 启动 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]

