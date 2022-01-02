# Binary search

def binary_search(arr, left_index, right_index, x):
 
    # Check base case
    if right_index >= left_index:
 
        mid = (right_index + left_index) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, left_index, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, right_index, x)
 
    else:
        # Element is not present in the array
        return -1
 
l = [4,9,11,17,21,25,29,32,38]
print(binary_search(l,0,len(l),38))
