import subprocess
import sys

def executar_comando(comando, mensagem_erro):
    """Executa um comando e retorna True se bem-sucedido, False caso contrário."""
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            subprocess.run(['termux-vibrate', '-d', '500'])
            subprocess.run(['termux-toast', f'{comando} concluído!'])
            return True
        else:
            subprocess.run(['termux-vibrate', '-d', '1000'])
            subprocess.run(['termux-toast', f'Erro: {resultado.stderr}'])
            print(f'Erro: {resultado.stderr}')
            return False
    except Exception as e:
        subprocess.run(['termux-vibrate', '-d', '1000'])
        subprocess.run(['termux-toast', f'Erro: {mensagem_erro} - {str(e)}'])
        print(f'Erro: {mensagem_erro} - {str(e)}')
        return False

def main():
    # Passo 1: Capturar mensagem de commit
    mensagem = input("Digite a mensagem do commit: ").strip()
    if not mensagem:
        print("Mensagem de commit vazia. Abortando.")
        subprocess.run(['termux-vibrate', '-d', '1000'])
        subprocess.run(['termux-toast', 'Mensagem de commit vazia!'])
        sys.exit(1)

    # Passo 2: Executar git add ., commit e push em sequência
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
    subprocess.run(['termux-vibrate', '-d', '500'])
    subprocess.run(['termux-toast', 'Commit e push concluídos!'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        subprocess.run(['termux-vibrate', '-d', '1000'])
        subprocess.run(['termux-toast', 'Operação cancelada!'])
        sys.exit(1)
