# NamikawaLab2019

Design Project III A at Kyoto University of Art and Design

- [How to Develop](#how-to-develop)
  - [Install libraries](#install-libraries)
  - [Run](#run)
- [Add Daemon](#add-daemon)

## How to Develop

### Install libraries

`pip3 install -r requirements.txt`

### Run

`python3 run.py`

You will be able to see `http://35.226.170.223:5000/` .

## Add Daemon

Create `/etc/systemd/system/NamikawaLab2019.service` like this,

```/etc/systemd/system/NamikawaLab2019.service:sh
[Unit]
Description=Flask Application
After=network.target

[Service]
User=shin
Group=shin
WorkingDirectory=/home/shin/NamikawaLab2019
ExecStart=/usr/bin/python3 /home/shin/NamikawaLab2019/run.py

[Install]
WantedBy=multi-user.target
```

Start: `sudo systemctl start NamikawaLab2019`
Stop: `sudo systemctl stop NamikawaLab2019`
