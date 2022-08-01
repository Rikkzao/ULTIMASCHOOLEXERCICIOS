prefixo = str(input("coloque o prefixo "))
palavra = str(input("escolha a palavra "))
def prefixo1(prefixo, palavra):
    if len(prefixo) > len(palavra):
        return "a palavra nao pode ser menor que o prefixo"
    x = 0
    while x<len(prefixo):
        if prefixo[x] != palavra[x]:
            return "não é prefixo"
        x = x + 1
    return ("é prefixo")
print(prefixo1(prefixo,palavra))