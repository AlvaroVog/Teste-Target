def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False


def main():
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if verifica_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")


if __name__ == "__main__":
    main()
