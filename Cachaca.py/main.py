# importações necessárias
from request import request_conselhos
from arq import salvar_conselhos, ler_conselhos
from traducao import traduzir_conselho
from arq import remover_conselho

# Função de exibição das escolhas (menu)
def exibe_menu():

    print("\n" + "=" * 40)
    print("🍻 Bem-vindo à Cachaçaria do Seu Zé 🍻")
    print("=" * 40)
    print("| \033[1;32m[1]\033[m - Pedir conselhos                |")
    print("| \033[1;32m[2]\033[m - Mostrar conselhos salvos       |")
    print("| \033[1;32m[3]\033[m - Traduzir conselhos             |")
    print("| \033[1;32m[4]\033[m - Remover conselhos              |")
    print("| \033[1;32m[5]\033[m - Encerrar                       |")
    print("=" * 40)

# Função main 
def main():

    while True:
        # Inicia o menu sempre após interação
        exibe_menu()

        # Filtra a escolha do usuário
        try:
            escolha = int(input("| \033[1;32m->\033[m  Selecione uma opção: "))

        # Caso não seja uma opção válida:
        except ValueError:
            print("Por favor, insira um número válido!")
            continue    # Retorna ao funcionamento principal

        match escolha:

            # CASE 1: Faz requisição de conselho e opção de salvamento.
            case 1:
                try:
                    qtd = int(input("Digite quantos conselhos deseja [até 10 conselhos por vez]: "))

                    # verifica se a requisição é válida.
                    if qtd <= 0 or qtd > 10:  
                        print("Por favor, insira um número entre 1 e 10.")
                        continue
                    
                # verifica se é um número inteiro.
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número inteiro.")
                    continue

                # Faz a requisição de conselhos pela API
                conselhos = request_conselhos(qtd)
                for id_conselho, conselho in conselhos:
                    print("=" * 120)
                    print(f"\033[1;32m{id_conselho}\033[m: {conselho}")
                

                # Salva conselho
                salvar = input("Deseja salvar esses conselhos? (S/N): ").strip().upper()
                    
                if salvar == "S":
                    salvar_conselhos(conselhos)
                        
                else:
                    print('Opção inválida! Não foi possível salvar o conselho!')

            # CASE 2: Faz leitura de conselhos salvos.
            case 2:
                conselhos_salvos = ler_conselhos()

                if conselhos_salvos:
                    print("Conselhos salvos:")

                    for conselho in conselhos_salvos:
                        print(conselho.strip())

                else:
                    print("Nenhum conselho salvo encontrado.")
            
            # CASE 3: Faz a tradução dos conselhos salvos através da API.
            case 3:
                conselhos_salvos = ler_conselhos()
                if conselhos_salvos:
                    print("Conselhos salvos:")
                    
                    # Enumera os IDs dos conselhos iniciando em 1.
                    for i, conselho in enumerate(conselhos_salvos, start=1):
                        print(f"[{i}] {conselho.strip()}")
                    
                    escolha = int(input("Selecione o número do conselho para traduzir: ")) - 1

                    if 0 <= escolha < len(conselhos_salvos):

                        # Divide a string do conselho pelo primeiro ":" e puxa o texto após o mesmo ([1])
                        texto = conselhos_salvos[escolha].split(": ", 1)[1] 

                        traducao = traduzir_conselho(texto)

                        print(f"Tradução: \033[1;32m{traducao}\033[m")

                    else:
                        print("Opção inválida.")
                else:
                    print("Nenhum conselho salvo encontrado.")

            # CASE 4: Acessa os conselhos salvos e permite a remoção dos mesmos.
            case 4:

                conselhos_salvos = ler_conselhos()  # Lê os conselhos armazenados
                if conselhos_salvos:
                    print("Conselhos salvos:")
                    # Enumera os IDs dos conselhos, iniciando de 1.
                    for i, conselho in enumerate(conselhos_salvos, start=1):
                        print(f"[{i}] {conselho.strip()}")

                    # Opção para excluir todos os conselhos
                    escolha = input("Selecione o número do conselho para remover ou digite '\033[1;31mT\033[m' para remover todos: ").strip().upper()

                    # Chama a função para remover o conselho
                    remover_conselho(escolha, conselhos_salvos)
                else:
                    print("Nenhum conselho salvo encontrado.")

            # CASE 5: Encerra o programa.
            case 5:
                print("Um abraço do seu Zé!")
                break
            
            # CASE _: Caso inválido.
            case _:
                print("Opção inválida. Tente novamente.")

# inicia o "main()"
if __name__ == "__main__":
    main()
