import pyautogui as gui
import time

repetitions = 10 #繰り返し回数
sleep_time = 4000 #間隔

for num in range(repetitions): #回数分だけループ
    print(num)
    gui.rightClick #右クリック
    
    time.sleep(sleep_time/1000) #間隔
