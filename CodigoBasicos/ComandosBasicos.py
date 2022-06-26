import traceback


print("Olá, flavio")

velocidade_internet = 10
print("Velocidade internet: ", velocidade_internet)

salario_mensal = input('Qual seu salário mensal ?')
horas_mensal = input('Quantas horas que vc trabalha mensalmente ?')

valor_hora = int(salario_mensal) / int(horas_mensal)
print("O seu salário/hora é : ", valor_hora, "/h")


trabalho_terminado = True
if trabalho_terminado == True:
    print('Opa! Bora ir embora')
else:
    print('Tomei')
