# NamikawaLab2019

Design Project III A at Kyoto University of Art and Design

![screenshot](https://user-images.githubusercontent.com/32637762/71595237-2a134100-2b7e-11ea-975f-b0c9263f446f.png)

- [How to Prepare Dataset](#how-to-prepare-dataset)
  - [Download from Instagram](#download-from-instagram)
  - [Mount Firestore](#mount-firestore)
- [How to Develop](#how-to-develop)
  - [Install libraries](#install-libraries)
  - [Run](#run)
  - [Mosaic](#mosaic)
- [Add Daemon](#add-daemon)
  - [Flask](#flask)
  - [filebrowser](#filebrowser)
- [Misc](#misc)
  - [Media Exposures](#media-exposures)
  - [Contributor](#contributor)
  - [Supervisor](#supervisor)
  - [License](#license)
  - [Thanks](#thanks)

## How to Prepare Dataset

### Download from Instagram

See `./downloadFromInstagramByHashtag.sh`.

### Mount Firestore

```sh
sudo apt install nfs-common
sudo mkdir /mnt/dataset
sudo mount 10.0.0.2:/vold /mnt/dataset
sudo chmod go+rw /mnt/dataset
```

## How to Develop

### Install libraries

`pip3 install -r requirements.txt`

### Run

`python3 run.py`

You will be able to see `http://35.192.103.89:5000/` .

### Mosaic

`python3 mosaic.py <target image> <source images path> <output image path>`

![mosaic](https://user-images.githubusercontent.com/32637762/71540972-43a56480-2995-11ea-8dd9-f220fe3965c3.jpg)

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

You will be able to see `http://35.192.103.89:8080/`.

## Misc

### Media Exposures

- https://www.kyoto-art.ac.jp/production/?p=108182

![www kyoto-art ac jp_production__p=108182](https://user-images.githubusercontent.com/32637762/72949220-fae19f80-3dca-11ea-9035-5fcdd842e960.png)

### Contributor

- 岡崎 竜久
- 北村 穂乃花
- 谷 琴音
- 中里 彩
- 根之木 颯亮

### Supervisor

- 並河 進
- 鈴木 真一朗

### License

MIT License.

### Thanks

- Icon: [Icongr.am/clarity](https://icongr.am/clarity)
