import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = (b**2) - 4 * a * c

if delta > 0:
    print("Deux solutions x1 et x2 :")
    print("x1 = {}\nx2 = {}".format((-b - math.sqrt(delta)) / 2 * a, (-b + math.sqrt(delta)) / 2 * a))
elif delta == 0:
    print("Solution double x :")
    print("x = {}".format((-b) / 2 * a))
else:
    print("Pas de solution !")