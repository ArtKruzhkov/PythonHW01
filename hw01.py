# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# print('Enter weekday number (1 - 7) :')
# a = int(input())
# if a <= 5:
#     print('It is NOT a weekend')
# elif a == 6:
#     print('It is weekend day! (Saturday)')
# elif a == 7:
#     print('It is weekend day! (Sunday)')
# else:
#     print('Wrong number')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# array = ["X", "Y", "Z"]
# left = not ("X" or "Y" or "Z")
# right = not "X" and not "Y" and not "Z"
# if left == right:
#     print('True')
# else:
#     print('False')



# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# print('Enter x: ')
# x = int(input())
# print('Enter y: ')
# y = int(input())
# if x > 0 and y > 0:
#     print('It is 1st quarter')
# elif x < 0 and y > 0:
#     print('It is 2nd quarter')
# elif x < 0 and y < 0:
#     print('It is 3rd quarter')
# else:
#     print('It is 4th quarter')


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# print('Enter quarter number (1 - 4): ')
# a = int(input())
# if a == 1:
#     print('It is 1st quarter. X > 0 and Y > 0.')
# elif a == 2:
#     print('It is 2nd quarter. X < 0 and Y > 0.')
# elif a == 3:
#     print('It is 3rd quarter. X < 0 and Y < 0.')
# elif a == 4:
#     print('It is 4th quarter. X > 0 and Y < 0.')
# else:
#     print('Wrong number')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# print('Enter x1 position:')
# x1 = float(input())
# print('Enter y1 position:')
# y1 = float(input())
# print('Enter x2 position:')
# x2 = float(input())
# print('Enter y2 position:')
# y2 = float(input())
# import math
# result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
# result = round(result, 2)
# print(f'Distance between these dots = {result}')


# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# print('Enter x1 position:')
# x1 = float(input())
# print('Enter y1 position:')
# y1 = float(input())
# print('Enter z1 position:')
# z1 = float(input())
# print('Enter x2 position:')
# x2 = float(input())
# print('Enter y2 position:')
# y2 = float(input())
# print('Enter z2 position:')
# z2 = float(input())
# import math
# result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))
# result = round(result, 2)
# print(f'Distance between these dots = {result}')