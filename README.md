# wo-ist-dirk
Automatic Position Tracking


## Installation

docker build -t frittenburger/wo-ist-dirk orch


docker-compose up


### Configure User/Passwort (once)
```
chmod 0700 /mosquitto/config/pwfile
chown root /mosquitto/config/pwfile
chgrp root /mosquitto/config/pwfile
mosquitto_passwd /mosquitto/config/pwfile <user>
```




### Test
Subscribe Topic
```
mosquitto_sub -v -h mosquitto -t 'hello/topic' -u <user> -P <password>
```

Publish Topic
```
mosquitto_pub -h mosquitto -t 'hello/topic' -m 'hello MQTT' -u <user> -P <password>
```