capital=int(input("DEFINA O VALOR DO CAPITAL: "))
taxa=int(input("DEFINA A TAXA A SER APLICADA: "))
tempo=int(input("DEFINA O TEMPO EM MESES: "))

def decorator_imprimir(funcao):
    def wrapper(capital,taxa,tempo):
        print("CAPITAL: ",capital)
        print("TAXA: ",taxa)
        print("TEMPO: ",tempo)
        res = funcao(capital,taxa,tempo)
        return res
    return wrapper

@decorator_imprimir
def juros_simples(capital,taxa,tempo):
    return capital*(taxa/100)*tempo



print("O VALOR DE JUROS É DE: ",juros_simples(capital,taxa,tempo))