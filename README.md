# wo-ist-dirk
Automatic Position Tracking


## Installation

### Pull Docker images
```
docker-compose pull
```

### Configure file-logger

Create `file-logger/config/subscriber.conf`

```
[default]

#BROKER = localhost
BROKER = mosquitto
PORT =  1883
TOPICS = owntracks/#

USERNAME = <user>
PASSWORD = <pass>
```

### Configure mosquitto
Create `mosquitto/config/mosquitto.conf`
```
allow_anonymous false
listener 1883
password_file /mosquitto/config/pwfile
```
Create empty file `mosquitto/config/pwfile`
#### Set mosquitto passwords

```
docker-compose up mosquitto -d
$ docker exec -it wo-ist-dirk-mosquitto-1 sh
/ # chmod 0700 /mosquitto/config/pwfile
/ # chown root /mosquitto/config/pwfile
/ # chgrp root /mosquitto/config/pwfile
/ # mosquitto_passwd /mosquitto/config/pwfile <user>
exit
```

### Configure otrecorder
Create `otrecorder/config/recorder.conf`
```
OTR_TOPICS = "owntracks/#"
OTR_HTTPHOST = "[::]"
OTR_HOST = "mosquitto"
OTR_USER = <username>
OTR_PASS = <password>
```

## Run
```
docker-compose up -d
```






## Development and Tests

### Rebuild file-logger Docker image
```
docker build -t frittenburger/mqtt-file-logger file-logger
```

### Test file-logger local

> [!NOTE]  
> Maybe, you need to edit  `file-logger/config/subscriber.conf`

```
cd file-logger
python subscribe.py
```

### Test MQTT
Login to file-logger container
```
docker exec -it wo-ist-dirk-file-logger-1 bash
```

Subscribe Topic
```
mosquitto_sub -v -h mosquitto -t 'owntracks/#' -u <user> -P <password>
```

Publish Topic
```
mosquitto_pub -h mosquitto -t 'owntracks/test' -m '{"_type":"location","acc":9,"alt":220,"batt":80,"bs":1,"conn":"w","created_at":1710859698,"lat":49.9753955,"lon":9.2884418,"m":1,"t":"p","tid":"TEST","tst":1710850011,"vac":9,"vel":0}' -u <username> -P <password>
```