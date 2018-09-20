import time
import random

def insertion_sort(arr):
  for k in range(1, len(arr)):
    cur = arr[k]
    j = k
    while (j > 0) and (arr[j - 1] > cur):
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = cur
  return arr

def selection_sort(arr):
  for a in range(0, len(arr) - 1):
    min_index = a
    min_value = arr[a]
    b = a + 1
    while(min_value > arr[b]) and (b < len(arr)):
      min_index = b
      min_value = arr[b]
      b += 1
    temp = arr[a]
    arr[a] = arr[min_index]
    arr[min_index] = temp
  return arr
   
if __name__ == '__main__':
  inc = [None] * 1000
  dec = [None] * 1000
  rand = [None] * 1000
  for i in range(0, 1000):
    inc[i] = random.randint(-100, 100) 
    dec[i] = random.randint(-100, 100)
    rand[i] = random.randint(-100, 100)
  inc = sorted(inc)
  dec = sorted(dec, reverse = True)
  
  start = time.clock()
  insertion_sort(inc)
  end = time.clock()
  print('One Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(inc)
  end = time.clock()
  print('One Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(dec)
  end = time.clock()
  print('One Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(dec)
  end = time.clock()
  print('One Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(rand)
  end = time.clock()
  print('One Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(rand)
  end = time.clock()
  print('One Thousand Random Selection: ' + '{:.20f}'.format(end-start))
  
  inc = [None] * 2500
  dec = [None] * 2500
  rand = [None] * 2500
  for i in range(0, 2500):
    inc[i] = random.randint(-100, 100) 
    dec[i] = random.randint(-100, 100)
    rand[i] = random.randint(-100, 100)
  inc = sorted(inc)
  dec = sorted(dec, reverse = True)
  start = time.clock()
  insertion_sort(inc)
  end = time.clock()
  print('Two Thousand Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(inc)
  end = time.clock()
  print('Two Thousand Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(dec)
  end = time.clock()
  print('Two Thousand Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(dec)
  end = time.clock()
  print('Two Thousand Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(rand)
  end = time.clock()
  print('Two Thousand Five Hundred Random Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(rand)
  end = time.clock()
  print('Two Thousand Five Hundred Random Selection: ' + '{:.20f}'.format(end-start))
  
  inc = [None] * 5000
  dec = [None] * 5000
  rand = [None] * 5000
  for i in range(0, 5000):
    inc[i] = random.randint(-100, 100) 
    dec[i] = random.randint(-100, 100)
    rand[i] = random.randint(-100, 100)
  inc = sorted(inc)
  dec = sorted(dec, reverse = True)
  start = time.clock()
  insertion_sort(inc)
  end = time.clock()
  print('Five Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(inc)
  end = time.clock()
  print('Five Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(dec)
  end = time.clock()
  print('Five Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(dec)
  end = time.clock()
  print('Five Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(rand)
  end = time.clock()
  print('Five Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(rand)
  end = time.clock()
  print('Five Thousand Random Selection: ' + '{:.20f}'.format(end-start))
  
  inc = [None] * 7500
  dec = [None] * 7500
  rand = [None] * 7500
  for i in range(0, 7500):
    inc[i] = random.randint(-100, 100) 
    dec[i] = random.randint(-100, 100)
    rand[i] = random.randint(-100, 100)
  inc = sorted(inc)
  dec = sorted(dec, reverse = True)
  start = time.clock()
  insertion_sort(inc)
  end = time.clock()
  print('Seven Thousand Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(inc)
  end = time.clock()
  print('Seven Thousand Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(dec)
  end = time.clock()
  print('Seven Thousand Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(dec)
  end = time.clock()
  print('Seven Thousand Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(rand)
  end = time.clock()
  print('Seven Thousand Five Hundred Random Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(rand)
  end = time.clock()
  print('Seven Thousand Five Hundred Random Selection: ' + '{:.20f}'.format(end-start))
  
  inc = [None] * 10000
  dec = [None] * 10000
  rand = [None] * 10000
  for i in range(0, 10000):
    inc[i] = random.randint(-100, 100) 
    dec[i] = random.randint(-100, 100)
    rand[i] = random.randint(-100, 100)
  inc = sorted(inc)
  dec = sorted(dec, reverse = True)
  start = time.clock()
  insertion_sort(inc)
  end = time.clock()
  print('Ten Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(inc)
  end = time.clock()
  print('Ten Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(dec)
  end = time.clock()
  print('Ten Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(dec)
  end = time.clock()
  print('Ten Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  insertion_sort(rand)
  end = time.clock()
  print('Ten Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
  start = time.clock()
  selection_sort(rand)
  end = time.clock()
  print('Ten Thousand Random Selection: ' + '{:.20f}'.format(end-start))