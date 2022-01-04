# bubble sort

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def bubble_sort(arr):
  size = len(arr)-1
  for j in range(size):
    swapped = False  #if the array is already sorted then there swapped will stay False
    for i in range(size-j): # the -j just to ignore the last elements that were already sorted in the previous iteration at the end of the array
      if arr[i] > arr[i+1]:
        swap(i,i+1,arr)
        swapped = True
    if not swapped: # if swapped is still false then break
      break
    
a = [11,9,29,7,2,15,28]
bubble_sort(a)
a
