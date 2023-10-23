# avocado

## matrix protocol bot

(this is currently in the make)

## how to run

### 0. create a Matrix account for your bot. Take note of it's username, password and homeserver.

We also recommend you to create a room to test it.

### 1. join the room(s) where your bot will run using it's account

### 2. clone this repository

### 3. copy the file botsecrets.py.example to botsecrets.py

### 4. edit the file botsecrets.py with the bot's credentials, owners' usernames etc

## Installing dependencies locally manually (not needed when using docker)

```
pkg install libolm  # termux
sudo pacman -Syu libolm  # archlinux, manjaro etc
sudo apt install libolm-dev  # debian, ubuntu etc
```

```
pip install "matrix-nio[e2e]" simplematrixbotlib
```

