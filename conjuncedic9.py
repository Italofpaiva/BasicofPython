def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

# Solicita os dados ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Calcula a idade
idade = calcular_idade(ano_nascimento, ano_atual)

# Exibe o resultado
print(f"A idade é {idade} anos.")