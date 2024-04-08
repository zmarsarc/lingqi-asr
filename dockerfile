FROM python:3.11-slim-bullseye
COPY requirements.txt sources.list /
RUN mv /sources.list /etc/apt/sources.list && \
    apt-get update && \
    apt-get --no-install-recommends -o Acquire::http::Pipeline-Depth=0 -y install gcc && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt


FROM python:3.11-slim-bullseye
COPY app sources.list /app/
COPY --from=0 /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=0 /usr/local/bin/ /usr/local/bin/
ADD whisper.tar.gz /
RUN mv /app/sources.list /etc/apt/sources.list && \
    apt-get update && \
    apt-get --no-install-recommends -o Acquire::http::Pipeline-Depth=0 -y install ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apt/archives

WORKDIR /
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]