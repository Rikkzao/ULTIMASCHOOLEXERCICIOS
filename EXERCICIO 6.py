string = str(input("Escolha a Palavra para contar as Letras "))
letra = str(input("Escolha a Letra que deseja a contagem "))

def contagem(string,letra):
    contador = 0
    for letra1 in string:
        if letra1 == letra:
            contador += 1
    return contador


#print(f"a palavra {string} tem {contador} letras ")
#print("a palavra""tem ",)
print(contagem(string,letra))