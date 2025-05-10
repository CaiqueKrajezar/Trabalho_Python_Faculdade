# Mensagem inicial
print("Bem-vindo à Copiadora Cópia Perfeita! Onde seus trabalhos viram arte. Meu nome é Caique Krajezar, em que posso ajudar?")

# Qual serviço deseja que executemos?
def escolha_servico():
    while True:
        servico = input("O que deseja? (dig/ico/ipb/fot): ").lower()
        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida. Por favor, escolha entre dig, ico, ipb ou fot.")

# Cálculo de páginas com desconto
def numera_qtd_de_paginas():
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            if paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return paginas * 0.85
            elif 200 <= paginas < 2000:
                return paginas * 0.80
            elif 2000 <= paginas < 20000:
                return paginas * 0.75
            else:
                print("Infelizmente o máximo permitido é 19999. Tente novamente!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Caso o cliente queira mais algum serviço
def servico_extra():
    while True:
        try:
            extra = int(input("Escolha o serviço adicional (1 - Encadernação Simples, 2 - Capa Dura, 0 - Nenhum): "))
            if extra == 1:
                return 15
            elif extra == 2:
                return 40
            elif extra == 0:
                return 0
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 0.")
        except ValueError:
            print("Opção inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    valor_servico = escolha_servico()
    
    paginas_com_desconto = numera_qtd_de_paginas()
    
    valor_extra = servico_extra()
    
    # Total a pagar
    total = (valor_servico * paginas_com_desconto) + valor_extra
    
    # Frase Final
    print(f"Resumo do pedido:")
    print(f"Serviço escolhido: {valor_servico:.2f} por página")
    print(f"Número de páginas (com desconto): {paginas_com_desconto:.2f}")
    print(f"Serviço extra: R$ {valor_extra:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
