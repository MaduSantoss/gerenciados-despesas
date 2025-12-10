````markdown
# 💰 Gerenciador de Despesas Pessoal

Este é um projeto de automação financeira desenvolvido em Python. O objetivo é permitir o registo rápido de despesas do dia a dia e manter um histórico persistente utilizando ficheiros CSV (Comma Separated Values).

Este projeto faz parte da minha jornada de aprendizagem em Pythonw.

## 🚀 Funcionalidades

- **Registo de Despesas:** Permite ao utilizador inserir uma descrição e um valor monetário.
- **Persistência de Dados:** Os dados não são perdidos ao fechar o programa; são gravados num ficheiro `despesas.csv`.
- **Leitura e Cálculo:** Um módulo de leitura que lista todos os gastos formatados e calcula o total acumulado automaticamente.
- **Tratamento de Arquivos:** Uso seguro da estrutura `with open()` para evitar corrupção de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Biblioteca `csv`** (Nativa do Python, para manipulação de dados tabulares)

## 📂 Estrutura do Projeto

O projeto é composto por dois scripts principais:

1.  `gerenciador_despesas.py`: O script de **entrada** (Input). Executa este ficheiro para adicionar uma nova compra.
2.  `ler_despesas.py`: O script de **saída** (Output). Executa este ficheiro para ver o extrato e o total gasto.
3.  `despesas.csv`: A base de dados gerada automaticamente pelo sistema.

## ⚙️ Como Executar

Certifica-te de que tens o Python instalado na tua máquina.

### 1. Para adicionar uma despesa:

Abra o terminal na pasta do projeto e execute:

```bash
python gerenciador_despesas.py
````

Siga as instruções no ecrã para digitar o nome e o valor.

### 2\. Para ver o total gasto:

Execute o comando:

```bash
python ler_despesas.py
```

O programa irá listar item por item e exibir o somatório final.

## 📝 Exemplo de Uso

**Entrada (`despesas.py`):**

```text
Digite a descrição da despesa: Mercado
Digite o valor da despesa: 150.50
Despesa registada com sucesso!
```

**Saída (`ler_despesas.py`):**

```text
--- Suas Despesas ---
Mercado: R$ 150.50
Gasolina: R$ 200.00
--------------------
Total Gasto: R$ 350.50
```

## 👩‍💻 Autora

Desenvolvido durante estudos de lógica de programação e manipulação de ficheiros em Python.
```
