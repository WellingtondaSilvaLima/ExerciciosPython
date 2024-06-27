nome = input('Qual é o seu nome: ')
altura = input('Qual a sua altura: ')
peso = input('Qual é o seu peso: ')

altura = float(altura)
peso = float(peso)

imc = peso / altura**2

print(f'{nome} tem {altura} de altura,\npesa {peso} quilos e seu IMC é\n{imc:.2f}')