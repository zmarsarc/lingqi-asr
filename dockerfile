FROM python:3.11-slim-bullseye
COPY requirements.txt /
RUN apt-get update && apt-get -y install gcc && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt


FROM python:3.11-slim-bullseye
COPY app /app
COPY --from=0 /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=0 /usr/local/bin/ /usr/local/bin/
ADD whisper.tar.gz /
RUN apt-get update && apt-get -y install ffmpeg && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/archives

WORKDIR /
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]