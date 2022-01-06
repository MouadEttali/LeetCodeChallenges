# merge two sorted arrays into one sorted array 

def merge_arrays(arr1,arr2,sorted_array):
  k = 0
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
      if arr1[i] <= arr2[j]:
        sorted_array[k] = arr1[i]
        i+=1
      elif arr2[j] <= arr1[i]:
        sorted_array[k] = arr2[j]
        j += 1
      k += 1
  while i < len(arr1):
    sorted_array[k] = arr1[i]
    i += 1
    k += 1
  while j < len(arr2):
    sorted_array[k] = arr2[j]
    j += 1
    k += 1


# merge sort function

def merge_sort(arr):
  if len(arr) <= 1:
    return 
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  merge_sort(left)
  merge_sort(right)

  return merge_arrays(left,right,arr)


arr = [17,25,28,33,4,9,26,44]
merge_sort(arr)
print(arr)
