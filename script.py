def linha(cont = 60):
    print('-' * cont)

def interface():
    vetorInterface = [
        "Olá, bem-vindo(a) ao Gerador de Senhas",
        "Escolha os tipos de Caracteres desejados:"
    ]
    vetorOptions = [
        "Opções:",
        "1 - Apenas númerico",
        "2 - Apenas letras minúsculas",
        "3 - Apenas letras maiúsculas",
        "4 - Apenas caracteres especiais",
        "5 - Tudo"
        
    ]

    for item in vetorInterface:
        linha()
        print(f"{item:^60}")

    for item in vetorOptions:
        print(item)

    while True:
        try:
            valor = int(input('Sua opção: '))
        except (ValueError, TypeError):
            print('Informe um valor válido')
        
        if 1 < valor < 5: 
            break
        else:
            continue



    return valor
  
        


interface()

# "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
#         "abcdefghijklmnopqrstuvwxyz",
#         "1234567890"