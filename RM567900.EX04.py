#LISTA DE EXERCÍCIOS COM IFS - Exercício 04
#Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, 
#levando em consideração o número de dias que o valor permaneceu aplicado, de acordo com a tabela abaixo:
# Até 180 dias = alíquota de 22,5% de IR.
# De 181 a 360 dias = alíquota de 20% de IR.
# De 361 a 720 dias = alíquota de 17,5% de IR.
#Acima de 720 dias = alíquota de 15% de IR.

# O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.

dias = 0
aliquota = 0
imposto = 0
resgate = 0

while True:
    tipo_investimento = int(input("Escolha o tipo de investimento: (1-CDB, 2-LCI, 3-LCA): "))
    if tipo_investimento == 1:
        resgaste = float(input("Qual o valor que deseja resgatar? R$ "))
        dias = int(input("O valor permaneceu investido por quantos dias? "))
        print("Seu investimento é um CDB, calcularemos o imposto.")
        
        if dias <= 180:
            aliquota = 22.5
        elif dias <= 360:
            aliquota = 20.0
        elif dias <= 720:
            aliquota = 17.5
        else:
            aliquota = 15.0
            
        imposto = resgaste * (aliquota / 100)
        
        print(f"Para {dias} dias, a alíquota é de {aliquota}%.")
        print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
        break

    elif tipo_investimento == 2 or tipo_investimento == 3:
        print("Investimento isento de Imposto de Renda.")
        break
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")
    
