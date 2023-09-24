from random import randint, shuffle, choice

lista_atr = ['Força', 'Constituição', 'Destreza', 'Inteligência', 'Sabedoria', 'Carisma']
lista_final = [1, 1, 1, 1, 1, 1]
lista_peso = []

#Gira os dados e retorna uma lista com 6 números aleatórios
def gera_num():
  media = 0
  while media <= 72:
    lista_num = []
    for repeticoes in range(6):
      lista_d6 = []
      soma = 0

      for rolagens in range(4):
        lista_d6.append(randint(1, 6))

      lista_d6.remove(min(lista_d6))

      for elementos in lista_d6:
        soma += elementos

      lista_num.append(soma)

    media = 0
    for num in lista_num:
      media += num

    print(f'\nsoma dos atributos gerados: {media}\n')


  print(f'Ordem original: {lista_num}')
  return lista_num

#Solicita os pesos e os ajusta nos casos do usuário não querer pesos e de 1 ou mais pesos repetidos
def pesos(lista_peso):

  #SALVAR DEPOIS DE MUDAR 
  #usa_peso = True
  usa_peso = False
  
  if usa_peso:
    input('Quer usar o sistema de pesos? NÃO USAR ZERO nem números NEGATIVOS: ')
    lista_peso.clear()
    for num in lista_atr:
      peso = int(input(f'Digite um peso para {num}: '))
      lista_peso.append(peso)
  
    if lista_peso.count(lista_peso[0]) == 6 or min(lista_peso) <= 0:
      lista_peso.clear()

  else:
    pass

  if len(lista_peso) == 0:
    print('fez algo tosco ai parceiro')
    lista_peso = [1, 2, 3, 4, 5, 6]
    shuffle(lista_peso)

  print(f'pesos: {lista_peso}')
  return lista_peso


def organiza_peso(lista_peso):
  if any(lista_peso.count(elemento) > 1 for elemento in lista_peso):
    while (any(lista_peso.count(elemento) > 1 for elemento in lista_peso)):
      mudanca = [0.001, -0.001]
      lista_posicoes = []
      for indice, elemento in enumerate(lista_peso):
        if lista_peso.count(elemento) > 1 and indice not in lista_posicoes:
          lista_posicoes.append(indice)

      lista_peso[lista_posicoes[0]] += choice(mudanca)
  
  return lista_peso


#Conforme a lista de pesos cria uma nova lista com os atributos organizados
def troca_elemento(lista_pesos, lista_atributos):
  for repetidor in range(6):
    lista_final[lista_pesos.index(max(lista_pesos))] = lista_atributos.pop(lista_atributos.index(max(lista_atributos)))
    lista_pesos[lista_pesos.index(max(lista_pesos))] = 0

  return lista_final

