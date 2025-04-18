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
    "branco": "f",
    "moeda": "g"
}

ESTILOS = {
    "negrito": "l",
    "doido": "k",
    "itálico": "o",
    "sublinhado": "n",
    "tachado": "m",
    "reset": "r"
}

def formatar_texto_minecraft(texto, cor=None, estilos=None):
    """Formata uma parte do texto para o padrão do Minecraft com cor e estilos."""
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
    print("Gerador de Texto Colorido para Minecraft (com múltiplas cores)")
    print("\nCores disponíveis:", ", ".join(CORES.keys()))
    print("Estilos disponíveis:", ", ".join(ESTILOS.keys()))
    
    # Lista para armazenar as partes do texto
    partes = []
    
    print("\nDigite as partes do texto com suas cores e estilos.")
    print("Para cada parte, forneça o texto, a cor e os estilos (se quiser).")
    print("Digite 'fim' quando terminar de adicionar partes.\n")
    
    while True:
        texto_parte = input("Texto da parte (ou 'fim' para encerrar): ")
        if texto_parte.lower() == "fim":
            break
        
        cor_parte = input("Cor para esta parte (ou deixe em branco para nenhuma): ")
        estilos_input = input("Estilos para esta parte (separados por vírgula, ou deixe em branco): ")
        estilos_parte = [estilo.strip() for estilo in estilos_input.split(",") if estilo.strip()]
        
        partes.append({
            "texto": texto_parte,
            "cor": cor_parte,
            "estilos": estilos_parte
        })
    
    if not partes:
        print("\nNenhuma parte adicionada. Encerrando.")
        return
    
    # Gera o texto formatado combinando todas as partes
    texto_formatado = ""
    for parte in partes:
        texto_formatado += formatar_texto_minecraft(
            parte["texto"],
            parte["cor"],
            parte["estilos"]
        )
    
    print("\nTexto formatado para o Minecraft:")
    print(texto_formatado)
    
    # Opcional: Copiar para a área de transferência
    try:
        import pyperclip
        pyperclip.copy(texto_formatado)
        print("Texto copiado para a área de transferência!")
    except ImportError:
        print("Instale o módulo 'pyperclip' para copiar o texto automaticamente.")

if __name__ == "__main__":
    main()