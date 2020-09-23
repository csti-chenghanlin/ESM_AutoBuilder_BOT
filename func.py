from pprint import pprint
from pathlib import Path
import requests
import subprocess

data = requests.get('https://api.github.com/repos/myESM/ESM/tags').json()

vers = [_['name'] for _ in data if 'dev' not in _['name']]
dev_vers = [_['name'] for _ in data if 'dev' in _['name']]

last_build_ver = "0"
last_build_dev_ver = 0

if Path('./last_build_ver').exists():
    with open('./last_build_ver', 'r') as f:
        last_build_ver = f.read()

if Path('./last_build_dev_ver').exists():
    with open('./last_build_dev_ver', 'r') as f:
        last_build_dev_ver = f.read()

if vers[0] != last_build_ver[0]:
        # print('download', vers[0])
        # subprocess.call(f'curl --progress-bar -sLo tmp/ESM_{vers[0]}.tar https://api.github.com/repos/myESM/ESM/tarball/{vers[0]} && mkdir -p tmp/{vers[0]}', shell=True)
        # print('Download Done!')
        # subprocess.call(f'tar -zxvf tmp/ESM_{vers[0]}.tar -C tmp/{vers[0]}', shell=True)
        # print('Exec Prepare.sh!')
        subprocess.call(f'bash tmp/{vers[0]}/*/SecBuzzerESM/prepare.sh', shell=True)
