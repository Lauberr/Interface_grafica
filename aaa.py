import ipaddress
import math


def coletar_dados():
    """
    Coleta dados de entrada do usuário: endereço IP, máscara de sub-rede e quantidade de sub-redes.
    """
    endereco_ip = input("Digite o endereço IP: ")
    mascara_subrede = input("Digite a máscara de sub-rede (em CIDR ou decimal): ")
    quantidade_subredes = int(input("Digite a quantidade de sub-redes: "))
    return endereco_ip, mascara_subrede, quantidade_subredes

def validar_dados(endereco_ip, mascara_subrede, quantidade_subredes):
    """
    Valida os dados de entrada. Retorna uma rede IP e a quantidade de sub-redes.
    """
    try:
        if '/' not in endereco_ip:
            endereco_ip = f"{endereco_ip}/{mascara_subrede}"
        
        ip = ipaddress.ip_network(endereco_ip, strict=False)
        
        if quantidade_subredes <= 0:
            raise ValueError("A quantidade de sub-redes deve ser um número inteiro positivo.")
        
        return ip, quantidade_subredes
    except ValueError as e:
        print(f"Erro na validação: {e}")
        return None, None

def calcular_bits_subrede(quantidade_subredes):
    """
    Calcula o número de bits necessários para criar a quantidade de sub-redes desejada.
    """
    return math.ceil(math.log2(quantidade_subredes))

def calcular_subredes(ip, quantidade_subredes):
    """
    Calcula as sub-redes com base no endereço IP, máscara de sub-rede e quantidade de sub-redes.
    """
    bits_subrede = calcular_bits_subrede(quantidade_subredes)
    nova_prefix = ip.prefixlen + bits_subrede
    
    if nova_prefix > ip.max_prefixlen:
        raise ValueError("Número de sub-redes é muito grande para o endereço IP fornecido.")
    
    subredes = list(ip.subnets(new_prefix=nova_prefix))
    return subredes

def gerar_enderecos_subredes(subredes):
    """
    Gera os endereços de sub-redes: primeiro endereço, último endereço e máscara.
    """
    enderecos = []
    for subrede in subredes:
        primeiro_endereco = subrede.network_address
        ultimo_endereco = subrede.broadcast_address
        mascara = subrede.netmask
        enderecos.append((primeiro_endereco, ultimo_endereco, mascara))
    return enderecos

def exibir_resultados(enderecos):
    """
    Exibe os resultados dos endereços de sub-redes.
    """
    for i, (primeiro, ultimo, mascara) in enumerate(enderecos, start=1):
        print(f"Sub-rede {i}:")
        print(f"  Primeiro Endereço: {primeiro}")
        print(f"  Último Endereço: {ultimo}")
        print(f"  Máscara: {mascara}\n")

def main():
    """
    Função principal que integra todas as etapas: coleta de dados, validação, cálculo e exibição dos resultados.
    """
    endereco_ip, mascara_subrede, quantidade_subredes = coletar_dados()
    ip, quantidade_subredes = validar_dados(endereco_ip, mascara_subrede, quantidade_subredes)
    if ip:
        try:
            subredes = calcular_subredes(ip, quantidade_subredes)
            enderecos = gerar_enderecos_subredes(subredes)
            exibir_resultados(enderecos)
        except ValueError as e:
            print(f"Erro no cálculo das sub-redes: {e}")

if __name__ == "__main__":
    main()
