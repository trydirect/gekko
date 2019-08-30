#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker
import requests

client = docker.from_env()
time.sleep(20)  # we expect all containers are up and running in 20 secs

for c in client.containers.list():
    print("{}: {}".format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())

# NGINX
nginx = client.containers.get('gekko_nginx')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
print(nginx_cfg.output.decode())
assert 'nginx: configuration file /etc/nginx/nginx.conf test is successful' in nginx_cfg.output.decode()

# assert 'server_name _;' in nginx_cfg.output.decode()
# assert "error_log /proc/self/fd/2" in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()

# test restart
nginx.restart()
time.sleep(3)
assert nginx.status == 'running'

web = client.containers.get('gekko')
print(web.logs())
assert web.status == 'running'

response = requests.get("http://localhost:3000")
print(response.text)
assert response.status_code == 200
assert "Gekko" in response.text
