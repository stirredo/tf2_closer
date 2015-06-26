from __future__ import print_function
import os
import time
import webbrowser

def open_tf2(url = "steam://rungameid/440" ):
    webbrowser.open(url)


def countdown(minutes):
    seconds = minutes * 60
    while seconds >= 0:
        minutesLeft, secondsLeft = divmod(seconds, 60)
        timeformat = "Time left: {0:02d}:{1:02d}\r\r\r\r\r".format(minutesLeft, secondsLeft)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1



def kill_tf2():
    os.system("taskkill /f /im hl2.exe")



def main():
    print("How long do you want to play TF2?\n")
    minutes = int(raw_input("Minutes: "))
    open_tf2()
    countdown(minutes)
    kill_tf2()

if __name__ == "__main__":
    main()

