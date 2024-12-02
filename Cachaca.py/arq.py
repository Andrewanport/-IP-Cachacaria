# Função para SALVAR conselho
def salvar_conselhos(conselhos, arquivo="conselhos.txt"):
    
    # Salva o conselho no arquivo de texto (conselhos.txt)

    try:
        with open(arquivo, "a") as f:
            for id_, conselho in conselhos:
                f.write(f"\033[1;32m{id_}\033[m: {conselho}\n")

        print("✔️  | Conselhos salvos com sucesso!")

    # Caso não consiga salvar:    
    except Exception as e:
        print(f"Erro ao salvar conselhos: {e}")


# Função para LER conselho
def ler_conselhos(arquivo="conselhos.txt"):
    
    # Lê o arquivo que foi salvo
    try:
        with open(arquivo, "r") as f:
            return f.readlines()
        
    # Caso não consiga ler o arquivo:
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum conselho foi salvo ainda.")
        return [] 

# Função para REMOVER conselho.
def remover_conselho(escolha, conselhos_salvos):

    if escolha == "T":  # Remove todos os conselhos

        with open("conselhos.txt", "w") as f:
            pass  # Limpa o conteúdo do arquivo

        print("✔️  |Todos os conselhos foram removidos com sucesso!")

        return True  # Indica que a operação foi bem-sucedida

    try:
        escolha = int(escolha) - 1  # Converte para índice da lista
        if 0 <= escolha < len(conselhos_salvos):
            conselho_removido = conselhos_salvos.pop(escolha)  # Remove o conselho da lista

            with open("conselhos.txt", "w") as f:
                f.writelines(conselhos_salvos)  # Salva os conselhos restantes no arquivo
            print(f"Conselho removido com sucesso: {conselho_removido.strip()}")
            return True  # Indica que a operação foi bem-sucedida
        else:
            print("Opção inválida.")
            return False  # Indica que a operação não foi bem-sucedida
    except ValueError:
        print("Por favor, insira um número válido.")
        return False  # Indica que a operação não foi bem-sucedida
