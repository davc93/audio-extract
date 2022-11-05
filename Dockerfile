FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN apt update -y && apt install ffmpeg -y
RUN pip install git+https://github.com/openai/whisper.git 
RUN pip install setuptools-rust
RUN pip install pytube
RUN mkdir files

COPY . /app

CMD bash -c "while true; do sleep 1; done"