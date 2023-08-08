

from os import name
opcao = input("[d] deposito \n[s] Saque \n[e] Extrato \n[q] Sair \nDigite sua opcao: ")
print( opcao)
print( input)



saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opcao = input(name)

    if opcao == "d":
        valor = float(input("Qual o valor do deposito: "))
  ## verifica se o valor é negativo
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"

        else:
            print("Operacao falhou! Valor informado esta invalido.")


    elif opcao == "s":
         valor = float(input("Qual o valor do saque: "))
         
         excedeu_saldo = valor > saldo
         excedue_limite = valor > limite
         excedeu_saques = numero_saque >= limite_saque

         if excedeu_saldo:
             print("Operacao falhou! Saldo insuficiente para realizar a operacao. ")

         elif excedue_limite:
               print("Operacao falhou! O valor do limite ultrapassado para realizar a operacao. ") 

         elif excedeu_saques:    
               print("Operacao falhou! O valor do saque esta ultrapassado para realizar a operacao. ") 

         elif  valor > 0:
               saldo -= valor
               extrato += f"Saque: R$ {valor: .2f}\n" 
               numero_saque += 1
         else:
              print("Operacao falhou! O valor esta invalido. ") 
##### if not extrato else extrato: para verificar se o extrato esta vazio
    elif  opcao == "e": 
          print("\n ************Extrato**********")
          print("Movimentacao nao realizada. " if not extrato else extrato)
          print(f"Saldo: R$ {saldo: .2f}\n")
          print("*******************************")   
    
    elif opcao == "q": 
         break

    else:
         print("Operacao falho, por favor seleciona uma opcao.... ")                  
            