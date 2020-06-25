import time 

def bubble_sort(data, draw, timeTick):
    for k in range(len(data)-1):
        for i in range(len(data)-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                color=['orange' for j in range(len(data))]
                color[i]='green'
                color[i+1]='green'
                draw(data, color)
                time.sleep(timeTick)
    draw(data,['red' for j in range(len(data))])
