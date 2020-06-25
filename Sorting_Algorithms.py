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

### -------------------- Algorithms separation ------------------------ ###

def merge_sort(data, draw, timeTick):
    merge_sort_algo(data, draw, timeTick, 0, len(data)-1)
    draw(data,['red' for j in range(len(data))])

def merge_sort_algo(data, draw, timeTick, start, end):
    if(start==end): return
    mid = (start+end) // 2
    merge_sort_algo(data, draw, timeTick, start, mid)
    merge_sort_algo(data, draw, timeTick, mid+1, end)
    merge(data, draw, timeTick, start, mid, end)

def merge(data, draw, timeTick, start, mid, end):
    left = data[start:mid+1]
    right = data[mid+1:end+1]

    i = j = k = 0
    while i<len(left) and j<len(right):
        color=['orange' for k in range(len(data))]
        color[start+i]='green'
        color[mid+j+1]='green'
        draw(data, color)
        time.sleep(timeTick)
        if(left[i]<=right[j]): 
            data[start+k]=left[i]
            i+=1
        else: 
            data[start+k]=right[j]
            j+=1
        k+=1
    
    while i<len(left):
        color=['orange' for k in range(len(data))]
        color[start+i]='green'
        color[mid+j]='green'
        draw(data, color)
        time.sleep(timeTick)
        data[start+k]=left[i]
        i+=1
        k+=1
    
    while j<len(right):
        color=['orange' for k in range(len(data))]
        color[start+i-1]='green'
        color[mid+j+1]='green'
        draw(data, color)
        time.sleep(timeTick)
        data[start+k]=right[j]
        j+=1
        k+=1
