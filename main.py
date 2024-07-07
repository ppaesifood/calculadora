#funções de calculo

def add(x, y):

    return x + y

def subtract(x, y):
    
    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    if y != 0:
        return x / y
   
    else:
        return "Erro: Divisao por zero"

def main():
    while True:
        print("\nCalculadora Simples")
        print("Operações disponiveis:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação (1/2/3/4/5)")

        if escolha == '5':
            print("saindo do programa...")
            break
        
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        
        if escolha == '1':
            print("Resultado: ", add(num1, num2))
        elif escolha == '2':
            print("Resultado: ", subtract(num1, num2))
        elif  escolha == '3':
            print("Resultado: ", multiply(num1, num2))
        elif escolha == '4':
            print("Resultado: ", divide(num1, num2))
        else:
            print("Operação invalida")

if __name__ == "__main__":
    main()


