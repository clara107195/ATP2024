#exercício 21 palitos jogador em primeiro lugar
##menu
import random
##modo 1- começa o jogador
def modo1():
    palitos=21
    while palitos>1:
        jog=int(input(f"Há {palitos} Quantos palitos queres tirar?(1,2,3 ou 4)"))
        while (jog<1 or jog>4) or jog>palitos:
            jog=int(input("Entrada inválida. Escolha um valor entre 1 e 4."))
        palitos=palitos-jog
        comp=5-jog
        palitos-=comp
        print(f"O computador retirou {comp} palitos.")  
    print("Perdeste. É a tua vez e sobra 1 palito.")

##modo 2- computador começa
def modo2():
    palitos=21
    while palitos>0:
        comp=(palitos-1) % 5
        if comp == 0 or comp > palitos:
            comp=random.randint(1, min(4,palitos))
        palitos-=comp
        print(f"O computador retirou {comp} palitos.")
        
        if palitos==1:
            print("Sobrou apenas 1  palito. O computador ganhou!")
            return
        

        jog=int(input(f"Agora é a tua vez,há {palitos} palitos. Quantos palitos queres tirar?"))
        while jog<1 or jog>4 or jog>palitos:
            jog=int(input("Entrada inválida. Escolhe um valor entre 1 e 4."))

        palitos= palitos-jog
        if palitos==1:
            print("Sobrou 1 palito. Ganhaste!!")
            return


##Jogo   ------------------------------------------------------------------------------------------
modo=input("Escolha um modo de jogo:\n1-Jogador começa\n2-Computador começa\n3-Sair do Jogo\n-Escolha:")
while modo != "3":
    if modo=="1":
        modo1()
    elif modo=="2":
        modo2()
    elif modo=="3":
        print("Obrigado. Até á próxima!")
    else:
        print("Opção inválida. Escolha 1,2 ou 3.")  
    modo=input("Escolha um modo de jogo:\n1-Jogador começa\n2-Computador começa\n3-Sair do Jogo\n-Escolha:")






