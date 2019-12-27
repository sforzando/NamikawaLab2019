# NamikawaLab2019

Design Project III A at Kyoto University of Art and Design

- [How to Develop](#how-to-develop)
  - [Install libraries](#install-libraries)
  - [Run](#run)
- [Add Daemon](#add-daemon)
  - [Flask](#flask)
  - [filebrowser](#filebrowser)

## How to Develop

### Install libraries

`pip3 install -r requirements.txt`

### Run

`python3 run.py`

You will be able to see `http://35.226.170.223:5000/` .

## Add Daemon

### Flask

Create `/etc/systemd/system/NamikawaLab2019.service` like this,

```ini:/etc/systemd/system/NamikawaLab2019.service
[Unit]
Description=Flask Application
After=network.target

[Service]
User=shin
Group=shin
WorkingDirectory=/home/shin/NamikawaLab2019
ExecStart=/usr/bin/python3 /home/shin/NamikawaLab2019/run.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Start: `sudo systemctl start NamikawaLab2019`
Stop: `sudo systemctl stop NamikawaLab2019`

### filebrowser

Create `/etc/systemd/system/filebrowser.service` like this,

```ini:/etc/systemd/system/filebrowser.service
[Unit]
Description=filebrowser
After=network.target

[Service]
User=shin
Group=shin
WorkingDirectory=/home/shin/NamikawaLab2019
ExecStart=/usr/local/bin/filebrowser -a 0.0.0.0 -r /home/shin/NamikawaLab2019

[Install]
WantedBy=multi-user.target
```

Start: `sudo systemctl start filebrowser`
Stop: `sudo systemctl stop filebrowser`
