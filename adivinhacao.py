def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    numero_secreto = round(random.random() * 100)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha uma dificuldade:\n[1] Fácil \n[2] Médio \n[3] Difícil\n")
    dificuldade = int(input("Define a dificuldade: "))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        # while (total_de_tentativas >= rodada):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100: ")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"\nParabéns! Você acertou na {rodada} rodada e fez {pontos} pontos!")
            break

        else:
            if (maior):
                print("O seu chute foi maior do que o número secreto!\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif (menor):
                print("O seu chute foi menor do que o número secreto!\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("\nFim do jogo.")

if (__name__=="__main__"):
    jogar()