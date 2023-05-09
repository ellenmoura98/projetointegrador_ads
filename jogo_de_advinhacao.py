from random import randint

print("======================\n  JOGO DE ADVINHAÇÃO\n======================")
print("REGRAS DO JOGO:\n 1. O computador escolherá um número de 1 a 100;\n 2. Você deve advinhar o número escolhido pelo computador; \n 3. Só é permitido 10 numero_escolhidos.\n ======================\n  BOA SORTE!\n====================== ")


sorteador = randint(1, 100)
numero_escolhido = 0
chance = 10

while numero_escolhido != sorteador:
  numero_escolhido = input("Advinhe qual o valor eu escolhi? :) Lembrando que é entre 1 a 100: ")
  if numero_escolhido.isnumeric():
    numero_escolhido = int(numero_escolhido)
    chance = chance - 1
    if numero_escolhido == sorteador:
      print("======================\nPARABÉNS! VOCÊ VENCEUU :) \n======================")
      print("O número que eu escolhi foi o {} e você adivinhou certinho! Intuição ótima hein? hahaha".format(sorteador))
      print("Você ainda tinha {} chances! Parabénssss ".format(chance))
      break
    else:
      print("======================")
      if numero_escolhido > sorteador:
        print("Ihh, não foi dessa vez! Tente novamente! :) ")
        print("Deixa eu te dar uma dica: é um número menor!")
        print("======================")
      else:
         print("Ihh, não foi dessa vez! Tente novamente! :) ")
         print("Deixa eu te dar uma dica: é um número maior!")
         print("======================")
    if chance == 0:
      print("Poxa! Suas chances acabaram! Não foi dessa vez :( )")
      print("======================")
      break

print("******************\n FIM DO JOGO DE ADVINHAÇÃO \n******************")
