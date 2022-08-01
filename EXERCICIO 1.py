x = int(input("escolha um valor para verificar se é par ou impar: "))

#if x%2 == 0:
#    print(f"{x} é par")
#else:
#    print(f"{x} é impar")


def parimpar(x):
    if x % 2 == 0:
        return f"{x} é par"
    else:
        return f"{x} é impar"



print(parimpar(x))