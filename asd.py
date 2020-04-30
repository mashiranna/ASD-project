import math
def find_min_distance():
  min_distance = math.inf
  for i in range(k-1):
    for j in range(i+1, k):
      sub = 0
      for a in range(n):
        sub += (arr[i][a] - arr[i+1][a])**2

      distance = math.sqrt(sub)
      if distance < min_distance:
        min_distance = distance
        points = [i, i+1]
  print('\nМінімальна відстань: ', min_distance, "\nМіж точками номер ", points[0], " та ", points[1])

n = int(input("Введіть розмірність простору "))
k = int(input("Введіть кількість точок "))
arr = []
for i in range(k):
  cords = []
  while len(cords) != n:
    print("Введіть координати точки ", i+1, " через пробіл:")
    cords = input().split(" ")
    cords_int = [int(i) for i in cords]
  arr.append(cords_int)
print(arr)
find_min_distance()