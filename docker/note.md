```
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ docker build -t vulnx ./docker/
$ docker run -it --name vulnx vulnx:latest -u http://example.com
```