FROM python:3.11-bookworm
# FROM python:latest

WORKDIR /avocado-bot

ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR
ENV LANGUAGE=pt

RUN DEBIAN_FRONTEND=noninteractive apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y fortunes-br libolm-dev locales python3-venv && \
    dpkg-reconfigure locales && \
    pip install --upgrade pip && \
    pip install "matrix-nio[e2e]" simplematrixbotlib && \
    echo 'export PATH="$PATH:/usr/games"' >> /root/.bashrc
    # echo 'export PATH="$PATH:/usr/games"' >> /root/.bashrc && \
    # source /root/.bashrc

CMD [ "python", "avocado.py" ]
