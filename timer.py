#!/usr/bin/python3

import time

def count(timer):
    
    while(timer):
        f = open("count.txt", "r+")
        counter = f.read()

        minutes, seconds = divmod(timer, 60)
        show = '{:02d}:{:02d}'.format(minutes, seconds)
        print(show, end="\r")
        time.sleep(1)
        timer -= 1
        
        filedata = counter.replace(counter, show)
        with open("count.txt", "w") as file:
            file.write(filedata)        

        f.close()

    print("Stream is Live")

timer = input("Time:")

count(int(timer))
