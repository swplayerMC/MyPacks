import subprocess
import sys

def executar_comando(comando, mensagem_erro):
    """Executa um comando e retorna True se bem-sucedido, False caso contrário."""
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f'{comando} concluído!')
            return True
        else:
            print(f'Erro: {resultado.stderr}')
            return False
    except Exception as e:
        print(f'Erro: {mensagem_erro} - {e}')
        return False

def main():
    # Passo 1: Capturar mensagem de commit
    mensagem = input("Digite a mensagem do commit: ").strip()
    if not mensagem:
        print("Mensagem de commit vazia. Abortando.")
        sys.exit(1)

    # Passo 2: Executar git add ., commit e push
    print("Executando: git add . && git commit -m ... && git push")
    comandos = [
        ("git add .", "Falha ao executar git add"),
        (f'git commit -m "{mensagem}"', "Falha ao executar git commit"),
        ("git push", "Falha ao executar git push")
    ]

    for comando, erro in comandos:
        if not executar_comando(comando, erro):
            sys.exit(1)

    print("Tudo concluído com sucesso!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        sys.exit(1)