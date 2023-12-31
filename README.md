# avocado

## matrix protocol bot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

(this is currently being written)

## How to run using Docker/Docker Compose

### 0. create a Matrix account for your bot. Take note of it's username, password and homeserver.

We also recommend you to create a room to test it.

### 1. join the room(s) where your bot will run using it's account

### 2. clone this repository and enter it

```
git clone https://github.com/pythonbrasil-matrix-org/avocado-bot.git
cd avocado-bot
```

### 3. copy the file `botsecrets.py.example` to `botsecrets.py`

```
cp botsecrets.py.example botsecrets.py
```

### 4. edit the file `botsecrets.py` with the bot's credentials, owners' usernames etc

### 5. build the docker image

```
docker build --tag avocado:0.0.1 .
```

### 6. start the docker compose service

```
docker compose up --detach
```

## Installing dependencies locally manually (not needed when using docker)

```
pkg install libolm  # termux
sudo pacman -Syu libolm  # archlinux, manjaro etc
sudo apt install libolm-dev  # debian, ubuntu etc
```

```
pip install "matrix-nio[e2e]"
pip install git+https://github.com/i10b/simplematrixbotlib.git@master
```

