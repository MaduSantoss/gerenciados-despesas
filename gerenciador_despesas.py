import csv 

#Nome da despesa 
despesa = input("Digite a descrição da despesa: ")
#Valor da despesa 
valor = float(input("Digite o valor da despesa: "))

#Salvando a despesa em um arquivo CSV
with open('despesas.csv', mode='a', newline= '', encoding='utf-8') as arquivo:
    #Escrevendo no arquivo CSV
    escritor_csv = csv.writer(arquivo)

    #Adicionando a despesa e o valor no arquivo
    escritor_csv.writerow([despesa, valor])

print("Despesa registrada com sucesso!")