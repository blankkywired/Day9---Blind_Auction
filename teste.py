# condicao = True
#
# base = {}
#
# valores = []
#
# def descobrir_maior(valor):
#     for i in valores:
#         if quantia > i:
#             print(f"Maior valor = {quantia}")
#             #Verifica interando sobre cada elemento e comparando se esse elemento é menor do que a ultima quantia adicionada
# while condicao:
#     nome = input('Nome: ')
#     quantia = int(input('Valor: '))
#     valores += [quantia]
#     base[nome] = quantia
#
#     condicao = input('Continuar?: ').lower()
#
#     if condicao == 'n':
#         condicao = False
#
#         # for j in base:
#         #     print(j, base[j])
#         print(descobrir_maior(valor=base[nome]))


condicao = True


lista = []

def maior_numero(valor):
    max_value_bid = 0
    for i in valor:
        if i > max_value_bid:
            max_value_bid = i
    return f"O maior valor é {max_value_bid}"


while condicao:
    valorUsuario = int(input('Valor: '))
    lista += [valorUsuario]


    if valorUsuario == 0:
        condicao = False

print(maior_numero(valor=lista))

