# Author: Lucas Gabriel

from random import randint

# funcao para gerar um numero primo aleatório
def gerarPrimoAleatorio(limite=0):

    eprimo = False

    # enquanto o numero gerado aleatoriamente não for primo fica no loop
    while eprimo == False:

        divisores = 0
        numero = randint(3, limite) # gera um numero aleatorio de 0 ate o limite informado

        # verifica quantos divisores um numero tem 
        for divisor in range(1, numero+1):
            if numero % divisor == 0:
                divisores += 1

        # se o numero de divisores for apenas 2 significa que é um numero primo 
        if divisores == 2:
            eprimo = True

    return numero # retorna o numero


# funcao para achar o inverso multiplicativo
def inversorModular(a, m): 
    a = a % m 

    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 

    return 1


# funcao para achar o MDC de dois numeros (algoritmo de Euclides)
def mdc(x, y):      
    while(y): 
        x, y = y, x % y 
      
    return x


# funcao para gerar novas chaves
def gerar_novas_chaves():

    # gera um numero aleatorio para P e Q dentro do limite informado
    p = gerarPrimoAleatorio(500)
    q = gerarPrimoAleatorio(500)

    # define o produto de P e Q
    n = p * q

    # função totiente em N, chamaremos de M
    m = (p-1) * (q-1)

    # define e, tal que, [1 > E > M] de forma que E e M sejam primos entre si
    e = 3
    while mdc(m, e) > 1:
        e += 2

    # define D, tau  que, D seja o inverso multiplicativo de E e M
    d = inversorModular(e, m)

    # guardando as novas chaves privadas em um arquivo .pem para salva-las
    with open('chave_privada.pem', 'w') as arquivo:
        arquivo.write(f'{d} {n}')

    # guardando as novas chaves publicas em um arquivo .pem para salva-las
    with open('chave_publica.pem', 'w') as arquivo:
        arquivo.write(f'{e} {n}')
