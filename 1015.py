import math

valor = input().split(" ")
valor2 = input().split(" ")

x1,y1 = valor
x2,y2 = valor2

distance = math.sqrt(pow(float(x2)-float(x1),2)+pow(float(y2)-float(y1),2))

print(f'{distance:0.4f}')