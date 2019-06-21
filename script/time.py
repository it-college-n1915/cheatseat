#!/usr/bin/python

import time

seconds = int(input("何秒測りますか？分で測りたいときは：0 "))
if seconds == 0:
    minute = int(input("何分測りますか？ "))
    count = minute * 60
    for i in range(count):
        print(count)
        count -= 1
        time.sleep(1)
else:
    for i in range(seconds):
        print(seconds)
        seconds -= 1
        time.sleep(1)

print("タイマー終了")

