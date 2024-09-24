menu = 0

while menu != 4:
    menu = int(input('Menu de opções: \n 1 - Novo salário \n 2 - Férias \n 3 - Décimo terceiro \n 4 - Sair \n Digite a opção desejada: '))

    if menu == 1:
        salario = float(input('Insira o seu salário: '))
        if salario <= 350:
            novoSalario = salario * 1.15
            print('O seu novo salário é de ' f'{novoSalario:,.2f}')
        elif salario > 350 and salario <= 600:
            novoSalario = salario * 1.10
            print('O seu novo salário é de ' f'{novoSalario:,.2f}')
        elif salario > 600:
            novoSalario = salario * 1.05
            print('O seu novo salário é de ' f'{novoSalario:,.2f}')

    elif menu == 2:
        salario = float(input('Insira o seu salário: '))
        ferias = salario + (salario / 2)
        print('O valor de suas férias é ' f'{ferias:,.2f}')

    elif menu == 3:
        salario = float(input('Insira o seu salário: '))
        meses = float(input('Insira o número de meses de trabalho na empresa: '))
        if meses <= 12:
            decimoTerceiro = (salario * meses) / 12
            print('O valor do seu décimo terceiro é de ' f'{decimoTerceiro:,.2f}')
        else:
            print('O número de meses não pode ser superior a 12')

    elif menu == 4:
        break
