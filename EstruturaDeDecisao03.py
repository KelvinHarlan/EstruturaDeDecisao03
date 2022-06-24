# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite "M" para Masculino e "F" para Feminino:\n ')
if sexo == 'M':
    print('Seu sexo é Masculino')
elif sexo == 'F':
    print('Seu sexo é Feminino')
else:
    print('Sexo inválido')