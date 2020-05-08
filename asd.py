import math
def find_min_distance():
 
  # n - кількість точок, k - розмірність простору
  # В масив arr потрібно ввести координати точок.

  arr = [[1, 5, 7], [3, 4, 8], [1, 6, 5], [-1, -5, 0]]
  n = len(arr)
  distance = 0
  min_distance = math.inf
  for i in range(n-1):
    k = len(arr[i])
    for j in range(i+1, n):
      for a in range(k):
        distance += (arr[i][a] - arr[i+1][a])**2      
        if distance < min_distance:
          min_distance = distance
          points = [i, i+1]
  print(arr)        
  print("\nМінімальна відстань між точками номер ", points[0], " та ", points[1])

find_min_distance()
