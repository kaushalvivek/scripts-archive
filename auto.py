import subprocess
import time
from datetime import datetime

while True:
    subprocess.call('git add .', shell=True)
    subprocess.call('git commit -m"' + str(datetime.now()) + '"', shell=True)
    subprocess.call('git push origin', shell=True)
    print("Task Completed, rescheduled for ten minutes, Continue to Code!")
    time.sleep(600)
