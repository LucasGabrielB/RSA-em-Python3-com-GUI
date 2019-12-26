# Author: Lucas Gabriel

# importa a biblioteca que faz a conversar para base64 e vice versa
from base64 import b64encode, b64decode

# funcao para ler o arquivo das chaves. retorna uma mensagem de erro se nao o encontrar o arquivo
def abrirArquivoDeChaves(arquivo):
    try:
        with open(arquivo, 'r') as f:
            chave1, chave2 = f.read().split()
            return int(chave1), int(chave2)
    
    except IOError:
        return 'Erro: Chave inválida/Não encontrada.'


# funcao para criptografar a mensagem
def criptografar(mensagemRecebida, chavePublicaArquivo, nomeArquivoTextoCriptografado):

    if mensagemRecebida == '':
        return 'Erro: Digite o texto para ser criptografado.'
        
    # le o arquivo das chaves publicas e retorna uma mensagem de erro se nao o encontrar
    chaveE, chaveN = abrirArquivoDeChaves(chavePublicaArquivo)

    # converte a mensagem recebida para base64 e depois para string, para pode cifrar
    mensagemRecebida = b64encode(mensagemRecebida.encode()).decode()
    
    # criptografa o texto usando as chaves publicas
    mensagemCifrada = ''
    
    for c in mensagemRecebida:
        mensagemCifrada += f'{((ord(c) ** chaveE) % chaveN)}.'

    # remove o ultimo "." para evitar erros futuros
    mensagemCifrada = mensagemCifrada[:-1]

    # escreve a mensagem criptografada em um arquivo
    # se o nome do informado do arquivo estiver vazio retorna uma mensagem de erro
    try:
        with open(str(nomeArquivoTextoCriptografado).strip(), 'w') as arquivo:
            arquivo.write(mensagemCifrada)
    
    except IOError:
        return 'Erro: Digite o nome do arquivo aonde deseja salvar o arquivo criptografado.'
    
    # retorna a mensagem cifrada
    return  mensagemCifrada


# funcao para descriptografar a mensagem
def descriptografar(arquivoCriptografado, chavePrivadaArquivo, nomeArquivoTextoDescriptografado):

    chaveD, chaveN = abrirArquivoDeChaves(chavePrivadaArquivo)

    # le o arquivo a ser descriptografado e retorna uma mensagem de erro se nao o encontrar
    try:
        with open(str(arquivoCriptografado), 'r') as f:
            dadosCriptografados = f.read().split('.')
    
    except IOError:
        return 'Erro: Arquivo inválida/não encontrado.'

    # descriptografando os dados criptografados do arquivo e pegando o texto descriptografado
    textoDescriptografado = ''
    
    for c in dadosCriptografados:
        textoDescriptografado += chr((int(c) ** chaveD) % chaveN)
    
    # converte a mensagem descriptografada de base64 de volta ao normal e depois para string
    # se ocorer um erro na decodificacao retorna uma mensagem informando um erro no conjunto de chaves
    try:
        textoDescriptografado = b64decode(textoDescriptografado.encode()).decode()
    
    except:
        return 'Erro: Chaves privadas incorretas.'
        
    # tenta escrever o texto descriptografado em um arquivo, caso de erro na decodificação ou
    # se o nome do arquivo ou o texto descriptografado estiver vazio retorna uma mensagem de erro
    try:
        if str(textoDescriptografado) != '':
            with open(str(nomeArquivoTextoDescriptografado).strip(), 'w') as arquivo:
                arquivo.write(textoDescriptografado)
        
        else:
            return 'Erro: Chaves privadas incorretas.'
    
    except UnicodeError:
        return 'Erro: Chaves privadas incorretas.'
    
    except IOError:
        return 'Erro: Digite o nome do arquivo aonde deseja salvar o texto descriptografado.'
        
    # retorna a mensagem descriptografada
    return textoDescriptografado
