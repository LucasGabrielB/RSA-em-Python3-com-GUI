# Author: Lucas Gabriel

# importa a biblioteca que faz a conversar para base64 e vice versa
from base64 import b64encode, b64decode

class Criptografia:

    # funcao para criptografar a mensagem
    def criptografar(mensagemRecebida, chavePublicaArquivo, nomeArquivoTextoCriptografado):

        if mensagemRecebida == '':
            return 'Erro: Digite o texto para ser criptografado.'
            
        # le o arquivo das chaves publicas e retorna uma mensagem de erro se nao o encontrar
        try:
            with open(chavePublicaArquivo, 'r') as arquivo:
                chaveE, chaveN = arquivo.read().split()
                chaveE = int(chaveE)
                chaveN = int(chaveN)
        
        except IOError:
            return 'Erro: Chave publica inválida/Não encontrada.'

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

        # le o arquivo da chave privada e retorna uma mensagem de erro se nao o encontrar
        try:
            with open(chavePrivadaArquivo, 'r') as arquivo:
                chaveD, chaveN = arquivo.read().split()
                chaveD = int(chaveD)
                chaveN = int(chaveN)    
        
        except IOError:
            return 'Erro: Chave privada inválida/não encontrada.'

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
            return 'Erro: Chaves privadas incorretas (acesso negado).'
	    	
        # tenta escrever o texto descriptografado em um arquivo, caso de erro na decodificação ou
        # se o nome do arquivo ou o texto descriptografado estiver vazio retorna uma mensagem de erro
        try:
            if str(textoDescriptografado) != '':
                with open(str(nomeArquivoTextoDescriptografado).strip(), 'w') as arquivo:
                    arquivo.write(textoDescriptografado)
            else:
                return 'Erro: Chaves privadas incorretas (acesso negado).'
        
        except UnicodeError:
            return 'Erro: Chaves privadas incorretas (acesso negado).'
        
        except IOError:
            return 'Erro: Digite o nome do arquivo aonde deseja salvar o texto descriptografado.'
            
        # retorna a mensagem descriptografada
        return textoDescriptografado
