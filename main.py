import time
import sys

results = []

def measureTime(list, function, algorithmType):
  startTime = time.perf_counter()
  function(list)
  endTime = time.perf_counter()
  tick = endTime - startTime
  results.append({
    "type": algorithmType,
    "time": tick,
    "output": list
  })

def pythonSort(array):
  array.sort()

def bubbleSort(array):
  for i in range(len(array)):
    for index in range(i):
      if array[index] > array[index + 1]:
        array[index], array[index + 1] = array[index + 1], array[index]

def mergeSort(array):
  if len(array) > 1:
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    mergeSort(left)
    mergeSort(right)

    index = leftIndex = rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
      if left[leftIndex] < right[rightIndex]:
        array[index] = left[leftIndex]
        leftIndex += 1
      else:
        array[index] = right[rightIndex]
        rightIndex += 1
      index += 1

    while leftIndex < len(left):
      array[index] = left[leftIndex]
      index += 1
      leftIndex += 1

    while rightIndex < len(right):
      array[index] = right[rightIndex]
      index += 1
      rightIndex += 1


def insertionSort(array):
  for i in range(1, len(array)):
    key = array[i]
    index = i - 1
    while index >= 0 and key < array[index]:
      array[index + 1] = array[index]
      index -= 1
    array[index + 1] = key

list = [3, 9, 6, 1, 4, 2, 10, 7, 5, 8]

print("\n" + "List:" + "\n" + str(list))

measureTime(list, pythonSort, "Python Sort Function")
list = [3, 9, 6, 1, 4, 2, 10, 7, 5, 8]
measureTime(list, bubbleSort, "Bubble Sort Algorithm")
list = [3, 9, 6, 1, 4, 2, 10, 7, 5, 8]
measureTime(list, mergeSort, "Merge Sort Algorithm")
list = [3, 9, 6, 1, 4, 2, 10, 7, 5, 8]
measureTime(list, insertionSort, "Insertion Sort Algorithm")

print("\n" + "Results:" + "\n")

for i in range(len(results)):
  for index in range(i):
    if (results[index]["time"] > results[index + 1]["time"]):
      results[index], results[index + 1] = results[index + 1], results[index]

for i in range(len(results)):
  print(str(i + 1) + ". " + results[i]["type"] + "\n" + "Time: " + str(results[i]["time"]))
