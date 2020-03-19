#!/usr/bin/python

import argparse
def compare(num1,num2):
  if num1 > num2:
    return num1
  else:
    return num2
def findMaxRec(A,n): 
    # if n = 0 means whole array  
    # has been traversed 
    if (n == 1): 
        return A[0] 
    return max(A[n - 1], findMaxRec(A, n - 1)) 
def findMinRec(A,n): 
  
    # if n = 0 means whole array  
    # has been traversed 
  if (n == 1): 
      return A[0] 
  return min(A[n - 1], findMinRec(A, n - 1)) 

def find_max_profit(arr):
  max = findMaxRec(arr,len(arr))
  index = arr.index(max)
  if index == 0:
    print(arr[2:])
    max = findMaxRec(arr[2:],len(arr[2:]))
    index = arr.index(max)
  min_array = arr[:index]
  min = findMinRec(min_array,len(min_array))
  # min = findMinRec(arr[:arr.index(max)],len(arr[:arr.index(max)]))
  # print(min)
  return max - min 

print(find_max_profit([100, 90, 80, 50, 20, 10]))