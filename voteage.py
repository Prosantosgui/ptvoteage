i = int(input('Informe a sua idade: '))
if i<=0:
    print('Idade inválida, tente um número maior que 0!')
    
elif 18<=i<70:
    print('Você é obrigado a votar!')

elif 16<=i<18 or i>=70:
    print('Seu voto é facultativo!')
else:
    print('Você não tem direito a votar!')