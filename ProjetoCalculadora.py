
resposta = input("Você deseja iniciar a calculadora? (s/n): ")

if resposta == "s":

    while True:
        print("---------- Calculadora de Dois Números ----------")
        print("[1] Somar")
        print("[2] Diminuir")
        print("[3] Dividir")
        print("[4] Multiplicar")
        print("[5] Sair")

        calc = input("Escolha uma opção: ")

        if calc == "1":
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))

            print("O resultado da soma é:", num1 + num2)

        elif calc == "5":
            print("Calculadora encerrada.")
            break

        elif calc == "2" :
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))

            print("O resultado da subtração é:", num1 - num2)
                    
        elif calc == "3":
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))

            if num2 == 0:
                print("Erro: não é possível dividir por zero.")
                continue
            else:
                print("O resultado da divisão é:", num1 / num2)

        elif calc == "4" :
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))

            print("O resultado da multiplicação é:", num1 * num2)

        else:
            print("Opção ainda não implementada.")
            continue

        retornar = input("Deseja retornar ao menu? (s/n): ")

        if retornar == "n":
            print("Você escolheu sair da calculadora.")
            break

else:
    print("Você escolheu não iniciar a calculadora.")
