"""
    Faça um programa que peça o tamanho de um arquivo para download (em MB)
    e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
    aproximado de download do arquivo usando este link (em minutos).

    # Exercício corrigido com a IA Gemini
"""

if __name__ == '__main__':
    print("Cálculo de Download")
    tamanho_mb: float = float(input("Digite o tamanho do arquivo (MB)"))
    velocidade_mbps: int = int(input("Digite a banda larga (mbps)"))
    tamanho_bits = tamanho_mb * 8 * 1024 * 1024
    tempo_dowload_segundos: float = tamanho_bits / velocidade_mbps
    tempo_dowload_minutos: float = tempo_dowload_segundos / 60
    print(f"O download ocorrerá em {tempo_dowload_minutos} minutos")
