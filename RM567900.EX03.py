#LISTA DE EXERCÍCIOS COM IFS - Exercício 03
#Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente: 
#valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech. 
#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#- Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.

valor_divida = float(input("Infomr o valor da dívida: "))

juros = 1.05
parcelas = 0
valor_parcela = 0
valor_juros = 0

print(f"Total: {valor_divida:.2f}. Juros: 0,00. Número de parcelas: 1. Valor da parcela {valor_divida}")

for i in range (4):
    parcelas = parcelas + 3
    juros = juros + 0.05
    total = valor_divida * juros
    valor_juros = total - valor_divida
    valor_parcela = total / parcelas
    print(f"Total: {total:.2f}. Juros: {valor_juros:.2f}. Número de parcelas: {parcelas}. Valor da parcela {valor_parcela:.2f}")
