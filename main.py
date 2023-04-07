from pytube import YouTube
import os, time
from threading import Thread
import readme

readme.loading_()

def slow_print(text:str, new_line:bool=True):
	for word in text:
		print(word, end="", flush=True)
		time.sleep(0.03)
	if new_line:print()

slow_print("[i]youtube url > ", False)
url = input()
slow_print("[~]pls wait...")
video = YouTube(url)
readme.clear()

slow_print(video.title)
slow_print(video.description())

time.sleep(3)

readme.clear()
n = 1

data = {}

for vid in video.streams:
	slow_print("{0} - {1}".format(str(n), str(vid.res)))
	data[str(n)] = vid
	n += 1

select = "-1"

while not select in data:
	if select != "-1":
		print("[!]choose a real value")
	slow_print("select resolution > ", False)
	select = input()

video = data[select]

Thread(target = video.download).start()
Thread(target = readme.print_).start()