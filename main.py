# Cálculo de IMC e classificação ###############

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 14.5:
        return "DESNUTRIÇÃO"
    elif imc < 20:
        return "ABAIXO DO NORMAL"
    elif imc < 25:
        return "PESO NORMAL"
    elif imc < 30:
        return "SOBREPESO"
    elif imc < 40:
        return "OBESIDADE"
    else:
        return "OBESIDADE MÓRBIDA"

# Entrada de dados
dados = []
for i in range(3):
    nome = input("\nInsira o Nome: ")
    altura = float(input("Insira a Altura [em m]: "))
    peso = float(input("Insira o Peso [em kg]: "))
    imc = calcular_imc(peso, altura)
    situacao = classificar_imc(imc)
    dados.append([nome, altura, peso, imc, situacao])

# Ordenar pelo nome
dados_ordenados = sorted(dados, key=lambda x: x[0])

# Saída formatada
print("\nNOME          IMC          SITUAÇÃO")
for pessoa in dados_ordenados:
    print(f"{pessoa[0]:<12} {pessoa[3]:.2f}      {pessoa[4]}")
