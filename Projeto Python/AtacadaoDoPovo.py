# Atacadão do Caique
print("Bem-vindo ao do Caique!")
print("Meu nome é Caique Krajezar, eu sou o dono, em que posso ajudar?")

# Valor do Produto e Quantidade Solicitada 
valor_unitario = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade vendida: "))

# Calculo do valor total do produto sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Aplicação da lógica para o desconto
if valor_total_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_total_sem_desconto < 6000:
    desconto = 4
elif 6000 <= valor_total_sem_desconto < 10000:
    desconto = 7
else:  
    desconto = 11

# Valor com desconto
valor_desconto = valor_total_sem_desconto * (desconto / 100)
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

# Apresentação de valores com e sem desconto
print(f"\nValor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor total com desconto: R$ {valor_total_com_desconto:.2f}")

# Mensagem final
if desconto > 0:
    print("\nParabéns! Seu pedido recebeu desconto especial!")
else:
    print("\nObrigado pela compra! Adicione mais itens para ganhar desconto.")
