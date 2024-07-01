## Avaliação 1

Projeto realizado para matéria de Redes de Computadores, 
acompanhado pelo professor Alexandre Yuji Kajihara

# Implemente um Programa para Cálculo de Sub-redes

## ANALISE

Implemente um programa que retorne o primeiro e o último endereço e a máscara de cada sub-rede, baseados no endereço IP, na máscara e na quantidade de sub-redes fornecidos pelo usuário.

### Itens Obrigatórios

- Interface gráfica
- Documentação
- Relatório

## PROJETO Passo a Passo 

Para implementar um programa em Python que retorne o primeiro e o último endereço de cada sub-rede, bem como a máscara de cada sub-rede com base no endereço IP, na máscara e na quantidade de sub-redes fornecidos pelo usuário, podemos dividir o projeto em várias partes. requisitos:

### Passo 1: Coleta de Dados do Usuário
- **Entrada do Endereço IP:** Coletar um endereço IP válido do usuário.
- **Entrada da Máscara de Sub-rede:** Coletar uma máscara de sub-rede válida (em formato CIDR ou decimal).
- **Quantidade de Sub-redes:** Coletar a quantidade de sub-redes desejada.

### Passo 2: Validação dos Dados
- **Validação do Endereço IP:** Verificar se o endereço IP fornecido é válido.
- **Validação da Máscara de Sub-rede:** Verificar se a máscara de sub-rede fornecida é válida.
- **Validação da Quantidade de Sub-redes:** Verificar se a quantidade de sub-redes é um número inteiro positivo.

### Passo 3: Cálculo da Sub-rede
- **Cálculo do Número de Bits Necessários:** Determinar o número de bits necessários para a sub-rede com base na quantidade de sub-redes.
- **Cálculo da Nova Máscara de Sub-rede:** Calcular a nova máscara de sub-rede a partir do número de bits necessários.
- **Cálculo dos Intervalos de Sub-redes:** Calcular os intervalos de endereços IP para cada sub-rede.

### Passo 4: Geração dos Endereços de Sub-redes
- **Cálculo do Primeiro Endereço:** Calcular o primeiro endereço de cada sub-rede.
- **Cálculo do Último Endereço:** Calcular o último endereço de cada sub-rede.
- **Geração das Máscaras de Sub-rede:** Retornar a máscara de sub-rede para cada sub-rede.

### Passo 5: Exibição dos Resultados
- **Exibição dos Endereços:** Exibir o primeiro e o último endereço de cada sub-rede.
- **Exibição da Máscara:** Exibir a máscara de sub-rede para cada sub-rede.

### Passo 6: Implementação em Python

## TESTE VALIDAÇÃO 
