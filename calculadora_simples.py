# Exercício: Calculadora simples
# Objetivo: praticar entrada de dados, conversão de tipos e operações matemáticas

print("Calculadora simples em Python")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print("Resultado da soma:", soma)
print("Resultado da subtração:", subtracao)
print("Resultado da multiplicação:", multiplicacao)

if numero2 != 0:
    divisao = numero1 / numero2
    print("Resultado da divisão:", divisao)
else:
    print("Não é possível dividir por zero.")
