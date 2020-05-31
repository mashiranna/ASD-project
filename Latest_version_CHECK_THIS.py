import math  # бібліотека для використання нескінченності і модуля числа

points = ([-1001, 50, 7], [3000, 4, 8], [1, 6, 5], [0, 0.5, 0], [0, 0, 0], [1, 1, 1]) # задаємо точки

min_distance = math.inf                                             # мінімальній відстані присвоюємо найбільше значення
for one_point in points:                                            # проходимо по кожній точці
    sub_list = points[points.index(one_point)+1::]                  # точки із списку, обрізанного від початку і до точки зовнішнього циклу
    for another_point in sub_list:                                  # підсписок всіх чисел після i
         distance = 0                                               # відстань між точками
         for k in range(len(one_point)):                            # проходимо по кожній координаті - розмірність простору
             distance += abs(one_point[k] - another_point[k])       # розраховується відстань між двома точками
         if distance < min_distance:                                # якщо нова відстань менша за мінімальну 
            min_distance = distance                                 # то мінімальна відстань приймає значення нової
            min_points = [points.index(one_point)+1, points.index(another_point)+1]  # масив, що складається з індексів точок між якими мінімальна відстань

print(min_points)                                                   #друк масиву індексів
