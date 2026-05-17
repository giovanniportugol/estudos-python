# Exercício: Verificador de número par ou ímpar
# Objetivo: praticar entrada de dados, condição if/else e operador módulo

print("Verificador de número par ou ímpar")

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
