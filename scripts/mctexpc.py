import re
import pyperclip  # Módulo para acessar a área de transferência no Windows

# Dicionários para mapear cores e estilos
CORES = {
    "preto": "0",
    "azul_escuro": "1",
    "verde": "2",
    "ciano": "3",
    "escarlate": "4",
    "roxo": "5",
    "dourado": "6",
    "laranja": "v",
    "prata": "7",
    "cinza": "8",
    "azul": "9",
    "lima": "a",
    "aqua": "b",
    "vermelho": "c",
    "rosa": "d",
    "amarelo": "e",
    "branco": "f"
}

ESTILOS = {
    "negrito": "l",
    "itálico": "o",
    "ofuscante": "k",
    "sublinhado": "n",
    "tachado": "m",
    "reset": "r"
}

def parsear_texto_colorido(entrada):
    """Parseia a entrada nas sintaxes 'estilos-cor'/texto/ ou |estilos|{cor}/texto/ e formata para Minecraft."""
    texto_formatado = ""
    ultima_posicao = 0
    
    # Regex para Sintaxe 1: 'estilos-cor'/texto/
    padrao1 = r"'(?:([\w,]+)-)?(\w+)'/([^/]+)/"
    # Regex para Sintaxe 2: |estilos|{cor}/texto/
    padrao2 = r"\|([\w,]+)\|\{([^}]+)\}/([^/]+)/"
    
    # Processa a entrada caractere por caractere para identificar padrões
    while ultima_posicao < len(entrada):
        # Tenta encontrar Sintaxe 1
        match1 = re.search(padrao1, entrada[ultima_posicao:])
        # Tenta encontrar Sintaxe 2
        match2 = re.search(padrao2, entrada[ultima_posicao:])
        
        # Seleciona o padrão que aparece primeiro
        if match1 and (not match2 or match1.start() <= match2.start()):
            estilos_str, cor, texto = match1.groups()
            inicio, fim = match1.start(), match1.end()
        elif match2:
            estilos_str, cor, texto = match2.groups()
            inicio, fim = match2.start(), match2.end()
        else:
            return None, f"Erro: Formato inválido a partir da posição {ultima_posicao}. Use 'estilos-cor'/texto/ ou |estilos|{cor}/texto/"
        
        # Avança a posição
        ultima_posicao += fim
        
        # Remove espaços extras do texto
        texto = texto.strip()
        if not texto:
            continue
        
        # Verifica se a cor é válida
        if cor.lower() not in CORES:
            return None, f"Erro: Cor '{cor}' não reconhecida. Cores disponíveis: {', '.join(CORES.keys())}"
        
        # Adiciona o código da cor
        texto_formatado += f"§{CORES[cor.lower()]}"
        
        # Processa estilos, se houver
        if estilos_str:
            estilos = [estilo.strip().lower() for estilo in estilos_str.split(",") if estilo.strip()]
            for estilo in estilos:
                if estilo not in ESTILOS:
                    return None, f"Erro: Estilo '{estilo}' não reconhecido. Estilos disponíveis: {', '.join(ESTILOS.keys())}"
                texto_formatado += f"§{ESTILOS[estilo]}"
        
        # Adiciona o texto
        texto_formatado += texto
        
        # Adiciona §r apenas se o próximo caractere for um espaço
        if ultima_posicao < len(entrada) and entrada[ultima_posicao] == " ":
            texto_formatado += "§r"
            ultima_posicao += 1  # Pula o espaço
    
    return texto_formatado, None

def copiar_para_clipboard(texto):
    """Copia o texto para a área de transferência usando pyperclip."""
    try:
        pyperclip.copy(texto)
        return True, "Texto copiado para a área de transferência!"
    except Exception as e:
        return False, f"Erro ao copiar para a área de transferência: {str(e)}"

def main():
    print("Gerador de Texto Colorido para Minecraft (Nova Sintaxe com Estilos e Cores)")
    print("\nCores disponíveis:", ", ".join(CORES.keys()))
    print("Estilos disponíveis:", ", ".join(ESTILOS.keys()))
    print("\nFormatos suportados:")
    print("1. 'estilos-cor'/texto/ (estilos opcionais, separados por vírgula)")
    print("   Exemplo: 'negrito,itálico-vermelho'/Oi/ 'verde'/mundo/")
    print("2. |estilos|{cor}/texto/{cor}/texto/ (estilos globais, cores alternáveis)")
    print("   Exemplo: |negrito,itálico|{vermelho}/Oi/{verde}/mundo/")
    print(" - Use '-' para separar estilos e cor na Sintaxe 1.")
    print(" - §r é adicionado apenas antes de um espaço entre trechos.")
    print(" - Sem espaço, §r não é adicionado (ex.: 'azul-negrito'/flor/'rosa-itálico'/esta/).")
    
    # Solicita a entrada
    entrada = input("\nDigite o texto no formato acima: ")
    
    # Parseia e formata o texto
    texto_formatado, erro = parsear_texto_colorido(entrada)
    
    if erro:
        print(f"\n{erro}")
        return
    
    print("\nTexto formatado para o Minecraft:")
    print(texto_formatado)
    
    # Copia para a área de transferência
    sucesso, mensagem = copiar_para_clipboard(texto_formatado)
    print(mensagem)

if __name__ == "__main__":
    main()