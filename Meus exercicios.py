#Banca de revistas#

import os

'''
Faça um programa que leia a quantidade de revistas compradas e informe o total de revistas compradas


Banca = int(input("Quais produtos você vai levar hoje? "))

print(f"Total de revistas compradas {Banca}")
'''

#Sistema de canais#

'''
Faça um sistema de canais em que o usuário digite um número e ele fale o nome do canal e o programa que está passando no
momento
'''

print('# [G]-Globo')
print('# [B]-Band')
print('# [R]-Record')
print('# [S] SBT')
print('[X]Sair do sistema')
 
TV = input("Digite a letra do canal correspondente: ")
Jornal_Hoje = 0
The_chef_com_Edu_Guedes = 0
Hoje_em_dia = 0
SBT_Brasil = 0
Total = 0

if TV == 'g' or TV == 'G':
        Jornal_Hoje += 1
        Total +=1
        print("Jornal hoje")
        
        print(TV.capitalize())

elif TV == 'b' or TV == 'B':
        The_chef_com_Edu_Guedes += 1
        Total +=1
        print("The chef com Edu Guedes")
       
        print(TV.capitalize())

elif TV == 'r' or TV == 'R' :
        Hoje_em_dia += 1
        Total +=1
        print("Hoje em dia")
       
        print(TV.capitalize())

elif TV == 's' or TV == 'S':
        SBT_Brasil += 1
        Total +=1
        print("SBT Brasil")
       
        print(TV.capitalize())
       
        print(f'\nJornal_Hoje: {Jornal_Hoje} Pesquisa\nThe_chefe_com_Edu_Guedes: {The_chef_com_Edu_Guedes} Pesquisa\nHoje_em_dia: {Hoje_em_dia} Pesquisa\nSBT_Brasil: {SBT_Brasil} Pesquisa\nTotal: {Total}/n')

else:
    print("Opa, Canal inexistente caro aluno(a)")

        

'''
Escreva um programa que com strings: Diga a posição da letra, Acabe com um espaço colocado pelo usuário e troque uma palavra por outra
no mesmo código
'''
'''
Texto = 'Olha nois aqui'
print(Texto.find('a'))
'''

'''
Texto = "     TURMA DA MÔNICA JOVEM      "
print(Texto.strip())
'''

'''
nome = "Kraft Heinz"
print(nome.replace("Heinz", "foods"))
'''

'''
Faça um programa que responda o if, elif e else
'''

'''
Mercado = input("Digite o produto ou a marca desejada: ")

OMO = ("Sabão em pó OMO 500g")
HEINZ = ("Ketchup HEINZ Tradicional 1KG")
OREO = ("Biscoito de baunilha Oreo 110G")

if Mercado == "Sabão em pó OMO 500g":
    print("Você escolheu um ótimo produto, volte sempre")

elif Mercado == "Ketchup HEINZ Tradicional 1KG":
    print("Ótima escolha, ele é o preferido do mundo desde 1869")

elif Mercado == "Biscoito de baunilha Oreo 110G":
    print("Vamos colocar um momento brincante na sua vida?")

else:
    print("Você não escolheu nenhum produto ainda")

#Sempre coloque o nome da variável que você declarou primeiro#
'''