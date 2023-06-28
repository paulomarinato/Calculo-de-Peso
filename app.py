sexo = input("Informe o seu sexo (M/F) : ")
altura = float(input("Informe a sua altura (em metros) : "))
peso = float(input("Informe o seu peso (em Kg) : "))

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

if peso > peso_ideal:
    print("Você está acima do seu peso ideal:", peso_ideal)
elif peso < peso_ideal:
    print("Você está abaixo do seu peso ideal:", peso_ideal)
else:
    print("Você está no seu peso ideal:", peso_ideal)


