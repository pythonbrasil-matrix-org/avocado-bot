FROM python:latest

WORKDIR /avocado-bot

ENV LANG=pt_BR.UTF-8

RUN 
    DEBIAN_FRONTEND=noninteractive sudo apt update && \
    DEBIAN_FRONTEND=noninteractive sudo apt install -y fortunes-br libolm-dev locales python3-venv && \
    dpkg-reconfigure locales && \
    pip install "matrix-nio[e2e]" simplematrixbotlib

CMD [ "python", "avocado.py" ]
