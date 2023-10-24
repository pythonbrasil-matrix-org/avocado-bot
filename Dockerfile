FROM python:3.10-bookworm
# FROM python:3.10-bullseye

WORKDIR /avocado-bot

ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR
ENV LANGUAGE=pt

RUN DEBIAN_FRONTEND=noninteractive apt update && apt upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt install -y fortunes-br libolm-dev locales python3-venv && \
    dpkg-reconfigure locales && \
    python -m venv .venv && \
    /avocado-bot/.venv/bin/pip install --upgrade pip && \
    /avocado-bot/.venv/bin/pip install "matrix-nio[e2e]" && \ 
    /avocado-bot/.venv/bin/pip install git+https://github.com/i10b/simplematrixbotlib.git@master && \
    echo 'export PATH="$PATH:/usr/games"' >> /root/.bashrc && \
    echo 'source /avocado-bot/.venv/bin/activate' >> /root/.bashrc

RUN ln -s /usr/games/fortune /usr/bin

CMD [ ".venv/bin/python", "-m", "avocado" ]
