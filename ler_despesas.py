import csv

#Lendo as despesas do arquivo despesas.csv
total = 0
with open('despesas.csv', mode='r', encoding='utf-8') as arquivo:
    #Criando um leitor CSV
    leitor_csv = csv.reader(arquivo)

    #Imprimindo as despesas
    print("Lista de Despesas:")
    for linha in leitor_csv:
        nome = linha[0]
        valor = float(linha[1]) # Convertendo o valor para float

        # Mostrando a despesa
        print(f"- {nome}: R$ {valor:.2f}")

        #Somando o valor total das despesas
        total += valor


#Imprimindo o total das despesas
print("-" * 20)
print(f"Total de Despesas: R$ {total:.2f}")
