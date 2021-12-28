import random

j = 0
c = 0

while True:

    jogador = input("Escolha 'p' para pedra, 'pl' para papel ou 't' para tesoura: ")
    computador = random.choice(['p', 'pl', 't'])

    if jogador == computador:
        print('Empate, tente outra vez')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 'p' and computador == 't':
        j = j + 1
        print('Você venceu! Sua pedra amassou a tesoura.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 't' and computador == 'pl':
        j = j + 1
        print('Você venceu! Sua tesoura picotou o papel.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 'pl' and computador == 'p':
        j = j + 1
        print('Você venceu! Seu papel embrulhou a pedra.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 't' and computador == 'p':
        c = c + 1
        print('Você perdeu, tente outra vez! Sua tesoura foi detonada.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 'pl' and computador == 't':
        c = c + 1
        print('Você perdeu, tente outra vez! Seu papel foi picotado.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break
    elif jogador == 'p' and computador == 'pl':
        c = c + 1
        print('Você perdeu, tente outra vez! Sua pedra foi embrulhada.')
        denovo = input('Quer jogar outra vez? (s/n)')
        if denovo == 's':
            continue
        else:
            break

#print(j)
print(f'Você fez {j} pontos e o computador fez {c} pontos!')    
