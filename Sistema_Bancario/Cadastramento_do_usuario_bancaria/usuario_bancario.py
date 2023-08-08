def cadastrar_usuario(nome):
    return {"nome": nome}

def cadastrar_conta_bancaria(titular, saldo_inicial=0, limite=500, limite_saque=3):
    return {
        "titular": titular,
        "saldo": saldo_inicial,
        "limite": limite,
        "limite_saque": limite_saque,
        "extrato": [],
        "numero_saques": 0
    }

def criar_conta_corrente(usuario, saldo_inicial=0, limite=500, limite_saque=3):
    conta = cadastrar_conta_bancaria(usuario["nome"], saldo_inicial, limite, limite_saque)
    usuario["conta"] = conta
    return conta

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        return saldo, extrato
    elif excedeu_limite:
        return saldo, extrato
    elif excedeu_saques:
        return saldo, extrato

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1

    return saldo, extrato

# Exemplo de uso:
usuario = cadastrar_usuario("Rodrigo Venceslau")
conta = criar_conta_corrente(usuario, saldo_inicial=1000, limite=1000, limite_saque=5)

print(usuario)
print(conta)

conta["saldo"], conta["extrato"] = saque(
    saldo=conta["saldo"],
    valor=300,
    extrato=conta["extrato"],
    limite=conta["limite"],
    numero_saques=conta["numero_saques"],
    limite_saque=conta["limite_saque"]
)

print(conta)


def cadastrar_usuario(nome):
    return {"nome": nome}

def cadastrar_conta_bancaria(titular, saldo_inicial=0, limite=500, limite_saque=3):
    return {
        "titular": titular,
        "saldo": saldo_inicial,
        "limite": limite,
        "limite_saque": limite_saque,
        "extrato": [],
        "numero_saques": 0
    }

def criar_conta_corrente(usuario, saldo_inicial=0, limite=500, limite_saque=3):
    conta = cadastrar_conta_bancaria(usuario["nome"], saldo_inicial, limite, limite_saque)
    usuario["conta"] = conta
    return conta

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        return saldo, extrato
    elif excedeu_limite:
        return saldo, extrato
    elif excedeu_saques:
        return saldo, extrato

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1

    return saldo, extrato

# Exemplo de uso:
usuario = cadastrar_usuario("Juliana")
conta = criar_conta_corrente(usuario, saldo_inicial=2000, limite=2000, limite_saque=5)

print(usuario)
print(conta)

conta["saldo"], conta["extrato"] = saque(
    saldo=conta["saldo"],
    valor=300,
    extrato=conta["extrato"],
    limite=conta["limite"],
    numero_saques=conta["numero_saques"],
    limite_saque=conta["limite_saque"]
)

print(conta)

