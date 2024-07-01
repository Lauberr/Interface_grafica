
#Passo 1: Coleta de Dados do Usuário

def coletar_dados():
    endereco_ip = input("Digite o endereço IP: ")
    mascara_subrede = input("Digite a máscara de sub-rede (em CIDR ou decimal): ")
    quantidade_subredes = int(input("Digite a quantidade de sub-redes: "))
    return endereco_ip, mascara_subrede, quantidade_subredes

#Passo 2: Validação dos Dados
import ipaddress

def validar_dados(endereco_ip, mascara_subrede, quantidade_subredes):
    try:
        ip = ipaddress.ip_network(f"{endereco_ip}/{mascara_subrede}", strict=False)
        if quantidade_subredes <= 0:
            raise ValueError("A quantidade de sub-redes deve ser um número inteiro positivo.")
        return ip, quantidade_subredes
    except ValueError as e:
        print(f"Erro na validação: {e}")
        return None, None

#Passo 3: Cálculo da Sub-rede
import math

def calcular_subredes(ip, quantidade_subredes):
    # Calcula o número de bits necessários para a sub-rede
    bits_subrede = math.ceil(math.log2(quantidade_subredes))
    nova_prefix = ip.prefixlen + bits_subrede
    
    # Verifica se a nova máscara é válida
    if nova_prefix > 32:
        raise ValueError("Número de sub-redes é muito grande para o endereço IP fornecido.")
    
    # Calcula as sub-redes
    subredes = list(ip.subnets(new_prefix=nova_prefix))
    return subredes

#Passo 4: Geração dos Endereços de Sub-redes
def gerar_enderecos_subredes(subredes):
    enderecos = []
    for subrede in subredes:
        primeiro_endereco = subrede.network_address
        ultimo_endereco = subrede.broadcast_address
        mascara = subrede.netmask
        enderecos.append((primeiro_endereco, ultimo_endereco, mascara))
    return enderecos

#Passo 5: Exibição dos Resultados
def exibir_resultados(enderecos):
    for i, (primeiro, ultimo, mascara) in enumerate(enderecos, start=1):
        print(f"Sub-rede {i}:")
        print(f"  Primeiro Endereço: {primeiro}")
        print(f"  Último Endereço: {ultimo}")
        print(f"  Máscara: {mascara}\n")

#Passo 6: Integração do Programa
def main():
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