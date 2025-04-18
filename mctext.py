# Dicionários para mapear cores e estilos
CORES = {
    "preto": "0",
    "azul_escuro": "1",
    "verde": "2",
    "ciano": "3",
    "vermelho": "4",
    "roxo": "5",
    "dourado": "6",
    "cinza_claro": "7",
    "cinza": "8",
    "azul": "9",
    "verde_claro": "a",
    "ciano_claro": "b",
    "vermelho_claro": "c",
    "rosa": "d",
    "amarelo": "e",
    "laranja": "v",
    "branco": "f"
}

ESTILOS = {
    "negrito": "l",
    "itálico": "o",
    "sublinhado": "n",
    "tachado": "m",
    "reset": "r"  # Reseta todos os formatos
}

def formatar_texto_minecraft(texto, cor=None, estilos=None):
    """Formata o texto para o padrão do Minecraft com cores e estilos."""
    if estilos is None:
        estilos = []
    
    resultado = ""
    
    # Adiciona o código da cor, se especificado
    if cor and cor.lower() in CORES:
        resultado += f"§{CORES[cor.lower()]}"
    
    # Adiciona os códigos dos estilos, se especificados
    for estilo in estilos:
        if estilo.lower() in ESTILOS:
            resultado += f"§{ESTILOS[estilo.lower()]}"
    
    # Adiciona o texto
    resultado += texto
    
    return resultado

def main():
    print("Gerador de Texto Colorido para Minecraft")
    print("\nCores disponíveis:", ", ".join(CORES.keys()))
    print("Estilos disponíveis:", ", ".join(ESTILOS.keys()))
    
    # Solicita o texto
    texto = input("\nDigite o texto que deseja formatar: ")
    
    # Solicita a cor
    cor = input("Digite a cor desejada (ou deixe em branco para nenhuma): ")
    
    # Solicita os estilos
    estilos_input = input("Digite os estilos desejados (separados por vírgula, ou deixe em branco): ")
    estilos = [estilo.strip() for estilo in estilos_input.split(",") if estilo.strip()]
    
    # Gera o texto formatado
    texto_formatado = formatar_texto_minecraft(texto, cor, estilos)
    
    print("\nTexto formatado para o Minecraft:")
    print(texto_formatado)
    
    # Opcional: Copiar para a área de transferência (requer o módulo pyperclip)
    try:
        import pyperclip
        pyperclip.copy(texto_formatado)
        print("Texto copiado para a área de transferência!")
    except ImportError:
        print("Instale o módulo 'pyperclip' para copiar o texto automaticamente.")

if __name__ == "__main__":
    main()