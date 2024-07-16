escolha = input('Quer converter para Fahrenheit (F) ou para Celsius (C)? ')
if escolha.lower() == "f" or "fahrenheit":
	Celsius = float(input('Insira a temperatura em graus celsius: '))
	Fahrenheit = (Celsius*1.8+32)
	print(f'A temperatura em graus fahrenheit é: {Fahrenheit}')
elif escolha.lower() == "c" or "celsius":
	Fahrenheit = float(input('Insira a temperatura em graus fahrenheit: '))
	Celsius = ((Fahrenheit-30)/2)
	print(f'A temperatura em graus celsius é: {Celsius}')
