import pafy
import vlc
from time import sleep
# input video numbers
videoNumbers = input('請輸入影片播放數: ')
try:
    int(videoNumbers)
    it_is = True
except ValueError:
    it_is = False
while not it_is:
    videoNumbers = input('請輸入數字喔: ')
    try:
        int(videoNumbers)
        it_is = True
    except ValueError:
        it_is = False

urls = []
for i in range(int(videoNumbers)):
    print(i+1, " -> ", "請輸入youtube URL: ")
    URLtemp = input()
    urls.append(URLtemp)

import threading
import time

# 子執行緒的工作函數
def job(url):
    # url of the video
    # url = "https://www.youtube.com/watch?v=072tU1tamd0"
    video = pafy.new(url)  # 設定URL
    best = video.getbest()  # 選擇最高畫質播放
    media = vlc.MediaPlayer(best.url)  # 創建播放器
    # 開始串流播放
    media.play()
    time.sleep(5)
    while media.is_playing():
        sleep(1)

# 建立 videoNumber 個子執行緒
threads = []
for i in range(int(videoNumbers)):
    threads.append(threading.Thread(target=job, args = (urls[i],)))
    threads[i].start()
# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(int(videoNumbers)):
    threads[i].join()

print("Done.")