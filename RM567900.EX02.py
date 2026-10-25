#LISTA DE EXERCÍCIOS COM IFS - Exercício 02
#A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
#Dados: PREÇO FINAL, QUANTIDADE DE PARCELAS e VALOR DA PARCELA
#Exibir: O preço final parcelado em XX é de XXXXXX com parcelas de XXXXXX

#DESCONTOS: a vista: 20%
#ACRESCIMOS: 6 - 3%
#           12 - 6%
#           18 - 9%
#           24 - 12%
#           30 - 15%
#           36 - 18%
#           42 - 21%
#           48 - 24%
#           54 - 27%
#           60 - 30%

valor_total = float(input("Informe o valor do veículo: "))

parcela = 0
juros = 1.00
valor_juros = 0
media = 0

desconto = valor_total * 0.80

print(f"O preço a vista é {desconto}")

for i in range (10):
    juros = juros + 0.03
    valor_juros = valor_total * juros
    parcela = parcela + 6
    media = valor_juros / parcela
    print(f"O preço final parcelado em {parcela}x é de {valor_juros:.2f} com parcelas de {media:.2f}")

    