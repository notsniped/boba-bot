"""
Script which uses `curl` to ping another file at random intervals. Designed to work with keep_alive.
"""
import os
import time
from threading import Thread
url = 'https://boba-bot.dhruvbhat.repl.co'
ping_delay = 5*60 #Default delay value
def mainloop():
  Thread(target=urlping)
def urlping():
  while True:
    os.system(f'curl {url}')
    time.sleep(int(ping_delay))
    print(f'[ping/INFO] Successfully pinged {url}')