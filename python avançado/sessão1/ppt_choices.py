
import random
choices = ["PEDRA", "PAPEL", "TESOURA"]
while True:
    user_choice = input("Introduza o seu palpite: PEDRA, PAPEL ou TESOURA\nQuer sair? [S/s]")
    user_choice = user_choice.upper()
    if user_choice == "S":
        break
    result = ""
    if user_choice in choices:
        num_pc_choice = random.randint(0, 2)
        pc_choice = choices[num_pc_choice]
        def apresentacao(a, b, c):
            print(f"\nJogou {a} e o computador jogou {b}. {c}\n")
        if user_choice == pc_choice:
            result = "EMPATOU!"
        elif user_choice == "PEDRA":
            if pc_choice == "TESOURA":
                result = "GANHOU!!"
            else:
                result = "Perdeu..."
        elif user_choice == "PAPEL":
            if pc_choice == "PEDRA":
                result = "GANHOU!!"
            else:
                result = "Perdeu..."
        elif user_choice == "TESOURA":
            if pc_choice == "PAPEL":
                result = "GANHOU!!"
            else:
                result = "Perdeu..."
        apresentacao(user_choice, pc_choice, result)
    else:
        print("Escolha errada!")