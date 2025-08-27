def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # só até a raiz quadrada
        if n % i == 0:
            return False
    return True


# Programa principal
if __name__ == "__main__":
    numero = int(input("Digite um número: "))

    if eh_primo(numero):
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é um número primo.")
