import forca
import adivinhacao


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************\n")

print("[1] Forca [2] Adivinhação.")

jogo =int(input("Qual o jogo? "))

if jogo==1:
    print("Jogando Forca")
    adivinhacao.jogar()
elif jogo==2:
    print("Jogando adivinhação")
    forca.jogar()