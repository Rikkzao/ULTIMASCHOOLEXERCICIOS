x = int(input("Verifique se o número é positivo ou negativo "))
def positivonegativo(x):
    if x > 0:
        return f"{x} é Positivo"
    else: 
        return f"{x} é Negativo"

print(positivonegativo(x))