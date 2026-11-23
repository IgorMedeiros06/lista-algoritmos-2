def mexe_salarios():
    salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]
    salarios[2] = 2300
    buscar = int(input("Qual salário você quer buscar? "))
    tem = 0
    ultimo = 0
    for salario in salarios:
        if salario == buscar:
            tem == True
            salarios.remove(buscar)
            ultimo = salarios.pop()
    return (f"{ultimo}\n{salarios}")

print(mexe_salarios())
