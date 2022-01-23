import math

valor = input().split(" ")

valor1, valor2, valor3 = valor

MaiorAB = (int(valor1) + int(valor2)+abs(int(valor1)-int(valor2)))/2

MaiorAC = (int(MaiorAB) + int(valor3)+abs(int(MaiorAB)-int(valor3)))/2

print("%d eh o maior" %MaiorAC)
