'''
Faça um sistema de canais em que o usuário digite um número e ele fale o nome do canal e o programa que está passando no
momento


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
