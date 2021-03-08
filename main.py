import math

# formula de baskhara


print("\033[1;96mFUNÇÃO DO SEGUNDO GRAU - ZERO DA FUNÇAO")
print("         f(x) = ax² + bx + c = 0\n")

a = int(input("\033[1;94mDigite o valor de A: "))
b = int(input("\033[1;94mDigite o valor de B: "))
c = int(input("\033[1;94mDigite o valor de C: "))

#delta = b² - 4ac
delta = (b**2) - 4 * a * c

print("\033[1;94m\nDelta vale \033[1;92m" + str(delta))

if delta > 0:
    #valores de X se Delta for maior que 0
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("\033[1;94m\nX1 vale \033[1;92m" + str(x1))
    print("\033[1;94mX2 vale \033[1;92m" + str(x2))
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("\033[1;94m\nX1 e X2 valem \033[1;92m" + str(x1))

else:
    print("O valor de delta é negativo, logo \033[1;91ma equação não possuirá valores reais.")
