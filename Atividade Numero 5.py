
import os
from dataclasses import dataclass

# Classe Prefeitura.
@dataclass
class Prefeitura:
    salario: float
    filhos: int

# Lista para armazenar as famílias.
lista_dados = []

# Função para limpar a tela (opcional).
def limpa_tela():
    os.system("cls || clear")

# Função para salvar os dados em um arquivo.
def salvar_dados():
    with open("pesquisa_prefeitura.txt", "w") as file:
        for familia in lista_dados:
            file.write(f"{familia.salario},{familia.filhos}\n")

# Função principal que executa o menu.
def main():
    while True:
        limpa_tela()
        print("""
Código  |  Descrição
1 - Adicionar Família
2 - Exibir Dados
3 - Sair
        """)

        opcao = input("Escolha uma opção exibida acima: ")

        if opcao == '1':
            salario = float(input("Salário da família: "))
            filhos = int(input("Número de filhos: "))
            nova_familia = Prefeitura(salario, filhos)
            lista_dados.append(nova_familia)
            salvar_dados()  # Salva os dados após adicionar uma família.

        elif opcao == '2':
            if lista_dados:
                total_familias = len(lista_dados)
                total_salario = sum(familia.salario for familia in lista_dados)
                total_filhos = sum(familia.filhos for familia in lista_dados)
                media_salario = total_salario / total_familias
                media_filhos = total_filhos / total_familias
                maior_salario = max(familia.salario for familia in lista_dados)
                menor_salario = min(familia.salario for familia in lista_dados)

                print(f"Quantidade de famílias: {total_familias}")
                print(f"Média salarial: R$ {media_salario:.2f}")
                print(f"Média de filhos: {media_filhos:.2f}")
                print(f"Maior salário: R$ {maior_salario:.2f}")
                print(f"Menor salário: R$ {menor_salario:.2f}")
            else:
                print("Nenhuma família cadastrada.")

        elif opcao == '3':
            print("Obrigada por usar o nosso App.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
