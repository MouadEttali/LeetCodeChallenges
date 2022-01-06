# Inserting Sort

def insertion_sort(elements):
  for i in range(1,len(elements)):
    anchor = elements[i]
    previous = i - 1
    while previous >= 0 and anchor < elements[previous]:
      elements[previous + 1] = elements[previous]
      previous -= 1
    elements[previous+1] = anchor
    
if __name__ == '__main__':
  tests = [
        [11,9,29,7,2,15,28]
    ]

  for elements in tests:
      insertion_sort(elements)
      print(f'sorted array: {elements}')
    
