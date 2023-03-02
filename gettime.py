import time
from datetime import datetime


now = datetime.now()

current_time = now.strftime("%H:%M")

def get_time():
    print(current_time)
