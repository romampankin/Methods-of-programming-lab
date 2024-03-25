import csv
import time
import matplotlib.pyplot as plt

class residents:
  def __init__(self, name, street, house, floor, year):
    self.name = name
    self.street = street
    self.house = house
    self.floor = floor
    self.year = year
  def __gt__(self, other): #>
    if self.street > other.street:
      return True
    elif self.street <= other.street:
      return False
    else:
      if self.house > other.house:
        return True
      elif self.house <= other.house:
        return False
      else:
        if self.floor > other.floor:
          return True
        elif self.floor <= other.floor:
          return False
        else:
          if self.name > other.name:
            return True
          elif self.name <= other.name:
            return False
          else:
            if self.year > other.year:
              return True
            else:
              return False
  def __ge__(self, other): #>=
    if self.street >= other.street:
      return True
    elif self.street < other.street:
      return False
    else:
      if self.house >= other.house:
        return True
      elif self.house < other.house:
        return False
      else:
        if self.floor >= other.floor:
          return True
        elif self.floor < other.floor:
          return False
        else:
          if self.name >= other.name:
            return True
          elif self.name < other.name:
            return False
          else:
            if self.year >= other.year:
              return True
            else:
              return False
  def __lt__(self, other): #<
    if self.street < other.street:
      return True
    elif self.street >= other.street:
      return False
    else:
      if self.house < other.house:
        return True
      elif self.house >= other.house:
        return False
      else:
        if self.floor < other.floor:
          return True
        elif self.floor >= other.floor:
          return False
        else:
          if self.name < other.name:
            return True
          elif self.name >= other.name:
            return False
          else:
            if self.year < other.year:
              return True
            else:
              return False
  def __le__(self, other): #<=
    if self.street <= other.street:
      return True
    elif self.street > other.street:
      return False
    else:
      if self.house <= other.house:
        return True
      elif self.house > other.house:
        return False
      else:
        if self.floor <= other.floor:
          return True
        elif self.floor > other.floor:
          return False
        else:
          if self.name <= other.name:
            return True
          elif self.name > other.name:
            return False
          else:
            if self.year <= other.year:
              return True
            else:
              return False
  def __eq__(self, other): #==
    if self.street != other.street:
      return False
    if self.house != other.house:
      return False
    if self.floor != other.floor:
      return False
    if self.name != other.name:
      return False
    if self.year != other.year:
      return False
    return True

data = []
with open("жильцы_1.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data1 = data.copy()

data = []
with open("жильцы_2.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data2 = data.copy()

data = []
with open("жильцы_3.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data3 = data.copy()

data = []
with open("жильцы_4.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data4 = data.copy()

data = []
with open("жильцы_5.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data5 = data.copy()

data = []
with open("жильцы_6.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data6 = data.copy()

data = []
with open("жильцы_7.csv", encoding="utf-8") as file:
  next(file)
  for row in file:
    r = row.split(',')
    resident = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))
    data.append(resident)
uns_data7 = data.copy()

uns_shaker1 = uns_data1.copy()
uns_shaker2 = uns_data2.copy()
uns_shaker3 = uns_data3.copy()
uns_shaker4 = uns_data4.copy()
uns_shaker5 = uns_data5.copy()
uns_shaker6 = uns_data6.copy()
uns_shaker7 = uns_data7.copy()

ans_l2 = [uns_shaker1, uns_shaker2, uns_shaker3, uns_shaker4, uns_shaker5, uns_shaker6, uns_shaker7]

uns_heap1 = uns_data1.copy()
uns_heap2 = uns_data2.copy()
uns_heap3 = uns_data3.copy()
uns_heap4 = uns_data4.copy()
uns_heap5 = uns_data5.copy()
uns_heap6 = uns_data6.copy()
uns_heap7 = uns_data7.copy()

ans_l3 = [uns_heap1, uns_heap2, uns_heap3, uns_heap4, uns_heap5, uns_heap6, uns_heap7]


def insert_sort(arr: list):
  for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
  return arr

insert_time = []
ans_l = [uns_data1, uns_data2, uns_data3, uns_data4, uns_data5, uns_data6, uns_data7]
x = []
for i in ans_l:
  x.append(len(i))
for i in ans_l:
  start = time.time()
  insert_sort(i)
  insert_time.append(time.time() - start)
print(insert_time)
p1 = plt.plot(x, insert_time)

ans1 = insert_sort(uns_data1)
with open('data.txt', 'w') as f:
        for elem in ans1:
            f.write(f'{elem.name} {elem.street} {elem.house} {elem.floor} {elem.year}\n')

def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True):
        swapped = False
        for i in range(start_index, end_index):  # проход слева направо
            if (array[i] > array[i + 1]) :                 # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if (not(swapped)):
            break

        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):         #проход справа налево
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1
    return array

shaker_time = []
for i in ans_l2:
  start = time.time()
  shaker_sort(i)
  shaker_time.append(time.time() - start)
print(shaker_time)
p2 = plt.plot(x, shaker_time)

def heapify(arr, n, i):
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[lar] < arr[l]:
        lar = l
    if r < n and arr[lar] < arr[r]:
        lar = r
    if lar != i:
        arr[i], arr[lar] = arr[lar], arr[i]

        heapify(arr, n, lar)

def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

heap_time = []
for i in ans_l3:
  start = time.time()
  heap_sort(i)
  heap_time.append(time.time() - start)
print(heap_time)
p3 = plt.plot(x, heap_time)

plt.plot(x, heap_time)
plt.plot(x, insert_time)
plt.plot(x, shaker_time)
plt.legend(('heap', 'insert', 'shaker'))