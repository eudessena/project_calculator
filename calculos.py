def operacoes():
    
    num_1 = input('informe o primeiro numero: ')
    num_2 = input('informe o segundo numero: ')
    
    try:
    
        num_1 = float(num_1)
        num_2 = float(num_2)
        
        operacao = input("""
                 digite o numero da opção da operação matemática você deseja realizar...
                 
                 1 - adição
                 2 - subtração
                 3 - multiplicação
                 4 - divisão
                 5 - potenciação
                 
                 """)

        if operacao == '1':
            adicao = num_1 + num_2
            print(f'Resultado: \n{adicao:.2f}')
    
        elif operacao == '2':
            subtracao = num_1 - num_2
            print(f'Resultado: \n{subtracao:.2f}')
    
        elif operacao == '3':
            multiplicacao = num_1 * num_2
            print(f'Resultado: \n{multiplicacao:.2f}')
    
        elif operacao == '4':
            divisao = num_1 / num_2
            print(f'Resultado: \n{divisao:.2f}')
    
        elif operacao == '5':
            potenciacao = num_1 ** num_2
            print(f'Resultado: \n{potenciacao:.2f}')
    
        else:
            
            print('opção inválida')
            
            validar = input('deseja tentar novamente? Y/N ').upper()
            
            while validar != 'Y' and validar != 'N':
                validar = input('deseja tentar novamente? Y/N ').upper()
                
            if validar == 'Y':
               operacoes()
            else:
                print('voce não tentou novamente!')         
                 
    except:
    
        print('voce digitou um valor não numérico!')
        
                   
        retorno = input('deseja tentar novamente? Y/N ').upper()
    
        while retorno != 'Y' and retorno != 'N':
        
            retorno = input('deseja tentar novamente? Y/N ').upper()
        
        if retorno == 'Y':
            operacoes()
                
        else:
            print('você não tentou novamente!')    

        
        
    